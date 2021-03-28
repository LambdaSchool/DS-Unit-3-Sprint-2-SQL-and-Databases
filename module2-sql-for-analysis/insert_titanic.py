import psycopg2
import sqlite3
import pandas as pd

dbname = 'lsustohi'
user = 'lsustohi'
password = '?'
host = 'rajje.db.elephantsql.com'

#Create connections and cursors
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()
sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

df = pd.read_csv('titanic.csv')

# Remove apostrophes from Name to prevent parsing erros
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')
#df.to_sql('titanic', sl_conn)   Only Once


# Extract titanic data
query = 'SELECT * FROM titanic'
titanic_sql = sl_curs.execute(query).fetchall()


# Create postgreSQL table
create_titanic_table = """
CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(90),
    sex VARCHAR(10),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare REAL
);
"""
#pg_curs.execute(create_titanic_table)
#pg_conn.commit()  Only Once   


#Insert data into table
for person in titanic_sql:
    insert_person = """
    INSERT INTO titanic
    (survived, pclass, name, sex, age,
    siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES """ + str(person[1:]) + ";"
    pg_curs.execute(insert_person)
#pg_conn.commit()  Only Once

