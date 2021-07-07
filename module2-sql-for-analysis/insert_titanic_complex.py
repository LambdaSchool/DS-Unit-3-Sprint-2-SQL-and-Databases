#imports
import psycopg2 as ps, pandas as pd
import passwords

# DB connection setup
dbname = passwords.dbname
user = passwords.user
password = passwords.password #don't commit this
host = passwords.host

# import titanic df
df = pd.read_csv('titanic.csv')

# check longest name
# n = 0
# for x in df['Name']:
#     if len(x) > n:
#         n=len(x)
# print(n)

# print(df.Survived.unique())

# connect to database
pg_conn = ps.connect(dbname=dbname, user=user,
                password=password, host=host)



# describe the 4 tables that will hold all values
create_passenger_table = """
CREATE TABLE IF NOT EXISTS passenger_table(
    passenger_id SERIAL PRIMARY KEY,
    name VARCHAR(85),
    age SMALLINT,
    sibs_abd SMALLINT,
    p_c_abd SMALLINT,
    fare REAL
)
"""

create_survived_table = """
CREATE TABLE IF NOT EXISTS survived_table(
    passenger_id INT REFERENCES passenger_table(passenger_id) DEFERRABLE INITIALLY DEFERRED,
    survived SMALLINT,
    PRIMARY KEY (passenger_id)
)
"""

create_sex_table = """
CREATE TYPE sex_enum AS ENUM ('male', 'female');

CREATE TABLE IF NOT EXISTS sex_table(
    passenger_id INT REFERENCES passenger_table(passenger_id) DEFERRABLE INITIALLY DEFERRED,
    sex sex_enum,
    PRIMARY KEY (passenger_id)
)
"""

create_pclass_table = """
CREATE TABLE IF NOT EXISTS pclass_table(
    passenger_id INT REFERENCES passenger_table(passenger_id) DEFERRABLE INITIALLY DEFERRED,
    pclass SMALLINT,
    PRIMARY KEY (passenger_id) 
)
"""
    


table_list = [create_passenger_table, create_pclass_table, create_survived_table,
                create_survived_table]

# create all 4 tables in the database
for table in table_list:
    # create a cursor
    pg_curs = pg_conn.cursor() 
    #EXECUTE!
    pg_curs.execute(table)

# commit
pg_conn.commit()

#create rows of tuples from the df
def gen_row_tuples(df):
    rows = []
    for idx, vals in df.iterrows():
        row = [idx]
        for val in vals.values:
            row.append(val)
        row = tuple(row)
        rows.append(row)
    return rows

# turn dataframe into tuples
tups = gen_row_tuples(df)

print(tups[0])
# print(tups[1])
# tup = tups[0]

# passenger_tup = tuple([tup[0]+1, tup[3], tup[5], tup[6], tup[7], tup[8]])

# print(str(passenger_tup))

# load tupples into db
for tup in tups:
    # print('inside tup loop')
    # index = tup[0] +1
    # survived = tup[1]
    # pclass = tup[2]
    # name = tup[3]
    # sex = tup[4]
    # age = tup[5]
    # sibs = tup[6] 
    # p_c = tup[7]
    # fare = tup[8]

    #create tuple insert objects:
    passenger_tup = tuple([tup[0]+1, tup[3], tup[5], tup[6], tup[7], tup[8]])
    survived_tup = tuple([tup[0]+1, tup[1]])
    sex_tup = tuple([tup[0]+1, tup[4]])
    pclass_tup = tuple([tup[0]+1, tup[2]])


    # create our inserts
    passenger_insert = """
    INSERT INTO passenger_table
    VALUES """+ str(passenger_tup)    
 
    survived_insert = """
    INSERT INTO survived_table
    VALUES """+ str(survived_tup)

    sex_insert = """
    INSERT INTO sex_table
    VALUES """+ str(sex_tup)

    pclass_insert = """
    INSERT INTO pclass_table
    VALUES """+ str(pclass_tup)

    insert_list = [passenger_insert, survived_insert,
                    sex_insert, pclass_insert]

    # create a new cursor
    pg_curs = pg_conn.cursor()

    # attempt to insert
    for insert in insert_list:
        print(insert)
        pg_curs.execute(insert)

pg_conn.commit()


# test to see if it worked:

# create a new cursor
pg_curs = pg_conn.cursor()

result = pg_curs.execute('SELECT * FROM passenger_table;').fetchmany(20)

print(result)
