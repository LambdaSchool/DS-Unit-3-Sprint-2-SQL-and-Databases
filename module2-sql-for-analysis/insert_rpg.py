import psycopg2 as pg
import sqlite3 as sl
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("RPG_NAME")
DB_USER = os.getenv("RPG_USER")
DB_PASSWORD = os.getenv("RPG_PASSWORD")
DB_HOST = os.getenv("RPG_HOST")

pg_conn = pg.connect(dbname=DB_NAME, user=DB_USER,
                     password=DB_PASSWORD, host=DB_HOST)
pg_curs = pg_conn.cursor()

sl_conn = sl.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
print(sl_curs.execute(row_count).fetchall())

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""

pg_curs.execute(create_character_table)
pg_conn.commit()

for character in characters:
    insert_character = f"""
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES {str(character[1:])};
    """
    pg_curs.execute(insert_character)
pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
print(pg_curs.fetchall())
