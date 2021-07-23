import os
import psycopg2
from dotenv import load_dotenv
import sqlite3

load_dotenv()

# Variables saved in .env file
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

# Connect to ElephantSQL-hosted PostgreSQL and instantiate cursor
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)
cursor = conn.cursor()

# An example query
# Note - nothing happened yet! We need to actually *fetch* from the cursor
cursor.execute('SELECT * from test_table;')
results = cursor.fetchone()


# Connect to SQLite3 DB for RPG data
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10').fetchall()
print(characters)

# Create Character Table in PostGRES

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	level INT,
	exp INT,
	hp INT,
	strength INT,
	intelligence INT,
	dexterity INT,
	wisdom INT
)
'''

cursor.execute(create_character_table_query)
conn.commit()

# Insert Character Data in PostGRES

for character in characters:
    insert_query = f''' INSERT INTO rpg_characters 
        (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES 
        {character}
    '''
    cursor.execute(insert_query)

# Commit and close out connection and cursors
conn.commit()
sl_cursor.close()
sl_conn.close()
cursor.close()
conn.close()
