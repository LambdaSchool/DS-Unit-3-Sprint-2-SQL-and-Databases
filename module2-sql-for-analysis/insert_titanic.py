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

# connect to database
pg_conn = ps.connect(dbname=dbname, user=user,
                password=password, host=host)

# create a new cursor
pg_curs = pg_conn.cursor()

result = pg_curs.execute('SELECT * FROM simple_passenger_table;')
output = result.fetchmany(20)

print(result)




# this was inside the create_pass_table but only run once
# CREATE TYPE sex_enum AS ENUM ('male', 'female');

# describe the table that will hold all values
create_passenger_table = """

CREATE TABLE IF NOT EXISTS simple_passenger_table(
    passenger_id SERIAL PRIMARY KEY,
    survived SMALLINT,
    pclass SMALLINT,
    name VARCHAR(85),
    sex sex_enum,
    age REAL,
    sibs_abd SMALLINT,
    p_c_abd SMALLINT,
    fare REAL
);
"""

table_list = [create_passenger_table]

# create all tables in the database
for table in table_list:
    # create a cursor
    pg_curs = pg_conn.cursor() 
    #EXECUTE!
    pg_curs.execute(table)

# commit
pg_conn.commit()

# clean out my df name strings:
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')

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

tups = gen_row_tuples(df)

# some debugging
# print(tups[0])
# print(tups[28][3])
# print(type(tups[28][3]))
# print(str(tups[25:32]))

# iterate through tuples and insert into db
for tup in tups[:5]:

    # create our inserts
    passenger_insert = """
    INSERT INTO simple_passenger_table
    VALUES """+ str(tup)    

    # print(passenger_insert)

    # create a new cursor
    pg_curs = pg_conn.cursor()

    # attempt to insert
    pg_curs.execute(passenger_insert)
    pg_conn.commit()

# and that totally worked

# create a new cursor
pg_curs = pg_conn.cursor()

result = pg_curs.execute('SELECT * FROM passenger_table;').fetchmany(20)

print(result)