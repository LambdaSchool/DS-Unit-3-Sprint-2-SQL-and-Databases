#!/usr/bin/env python

import sqlite3
import psycopg2 as pg 

# Get the data from sqlite3
sl_conn - sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
results = sl_conn.execute('SELECT * FROM charactercreator_character;').fetchall()

# CReate table and insert data in PostgreSQL
create_character_table = """CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,wisdom int
    );"""

# Assume user defines database params
def make_and_populate_table():
    pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
    pg_cur = pg_conn.cursor()

    pg_curs.execute(create_character_table)

    for result in results:
        insert_result = """INSERT INTO charactercreator_character
        (name, level,exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES""" + str(result[1:])