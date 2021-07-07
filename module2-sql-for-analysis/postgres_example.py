# ./usr/bin/env python
"""Example of moving data from rpg_db.sqlite3 to PostgreSQL"""

import sqlite3
import psycopg2 as pg
from dotenv import load_dotenv
import os

# Get the data from sqlite3
sl_con = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
results = sl_con.execute(
    'SELECT * FROM charactercreator_character;').fetchall()

create_character_table = """CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,
    wisdom int
);"""

# Get PostgreSQL credentials from .env file
load_dotenv()
dbname = os.getenv('pg_dbname')
user = os.getenv('pg_user')
password = os.getenv('pg_password')
host = os.getenv('pg_host')

pg_conn = pg.connect(dbname=dbname, user=user,
                     password=password, host=host)


def make_and_populate_character_table():
    pg_curs = pg_conn.cursor()

    pg_curs.execute(create_character_table)

    for result in results:
        insert_result = """INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES""" + str(result[1:])
        pg_curs.execute(insert_result)

    pg_conn.commit()
