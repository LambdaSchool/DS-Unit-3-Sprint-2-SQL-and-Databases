# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import psycopg2


dbname = 'bndoemhv'
user = 'bndoemhv'
password = ''  # Dont commit this
host = 'raja.db.elephantsql.com'

conn = sqlite3.connect('titanic')

df = pd.read_csv("titanic.csv")
df.to_sql(name='titanic', con=conn, if_exists='replace')


pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect("titanic")
sl_curs = sl_conn.cursor()

survivors = sl_curs.execute('''SELECT * FROM titanic;''').fetchall()

create_titanic_table = """
  CREATE TABLE titanic_database (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(10),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT
  );
"""

pg_curs.execute(create_titanic_table)


show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
print(pg_curs.execute(show_tables))
pg_curs.fetchall()


for person in survivors:
    insert_person = """
    INSERT INTO titanic_database
    (survived, pclass, name, sex, age, siblings_spouses_aboard,
     parents_children_aboard, fare)
    VALUES """ + str(person[1:]) + ';'
    # print(insert_character)
    pg_curs.execute(insert_person)

pg_curs.execute('SELECT * FROM titanic_database;')
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()
