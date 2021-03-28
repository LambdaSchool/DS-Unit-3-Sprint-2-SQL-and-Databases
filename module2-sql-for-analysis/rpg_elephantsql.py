import psycopg2
import sqlite3

dbname = 'lsustohi'
user = 'lsustohi'
password = '?'
host = 'rajje.db.elephantsql.com'


#Create connections and cursors
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn  = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
 

#How many rows?
get_rows = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(get_rows)
row_count = sl_curs.fetchall()[0][0]
print('There are', row_count, 'rows in character table.')


#Extract RPG data
get_characters = 'SELECT * FROM charactercreator_character'
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()
print(characters[:5])

#Create table
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
#pg_curs.execute(create_character_table)
#pg_conn.commit() Only once


#Insert data into table
for char in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(char[1:]) + ";"
    pg_curs.execute(insert_character)
#pg_conn.commit()  Only Once