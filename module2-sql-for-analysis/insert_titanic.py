import pandas as pd
import psycopg2 as pg
import sqlite3 as sl
import warnings
import os
from dotenv import load_dotenv
warnings.simplefilter(action='ignore', category=UserWarning)

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

sl_conn = sl.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()
pg_conn = pg.connect(dbname=DB_NAME, user=DB_USER,
                     password=DB_PASSWORD, host=DB_HOST)
pg_curs = pg_conn.cursor()

titanic = pd.read_csv('titanic.csv')

titanic['Name'] = titanic['Name'].str.replace("'", "")

try:
    titanic.to_sql('titanic.sqlite3', con=sl_conn)
except ValueError:
    pass

create_titanic_table = """
CREATE TABLE titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    passenger_class INT,
    name VARCHAR(100),
    sex VARCHAR(10),
    age INT,
    siblings_and_spouses INT,
    parents_and_children INT,
    fare FLOAT
);
"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()

get_passengers = 'SELECT * FROM "titanic.sqlite3"'
passengers = sl_curs.execute(get_passengers).fetchall()

for passenger in passengers:
    insert_passenger = f"""
    INSERT INTO titanic
    (survived, passenger_class, name, sex, age,
    siblings_and_spouses, parents_and_children, fare)
    VALUES {str(passenger[1:])};
    """
    pg_curs.execute(insert_passenger)
pg_conn.commit()
