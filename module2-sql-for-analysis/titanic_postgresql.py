"""
Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
thinking about the schema to make sure it is appropriate for the columns.
[Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
be useful. Once it is set up, write a `insert_titanic.py` script that uses
`psycopg2` to connect to and upload the data from the csv, and add the file to
your repo. Then start writing PostgreSQL queries to explore the data!
"""

import psycopg2
import sqlite3
import pandas as pd

pg_conn = psycopg2.connect("dbname=postgres user=postgres password={secret}")
pg_curs = pg_conn.cursor()

df = pd.read_csv("titanic.csv")
df.Name = df.Name.replace("'", '', regex=True)

query_create_table="""
    CREATE TABLE titanic (
    character_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(10),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT(10)
    );
    """
pg_curs.execute(query_create_table)

show_tables="""
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
    """
pg_curs.execute(show_tables)
pg_curs.fetchall()

passengers = df.values.tolist()

for passenger in passengers:
    insert_row="""
        INSERT INTO titanic
        (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
        VALUES ("""+str(passenger)[1:-1]+");"
    pg_curs.execute(insert_row)
