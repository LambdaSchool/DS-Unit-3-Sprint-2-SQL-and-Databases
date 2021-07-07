# Local install. Go to the desired dir and local install
## pipenv install psycopg2-binary

# Activate
## pipenv shell

import psycopg2


# From help(psycopg2.connect) - Enter the bottom 4.
dbname = 'ximkxdxb'
user = 'ximkxdxb'
password = '' # Don't commit this. delete when you commit/push
host = 'raja.db.elephantsql.com'

# Connect to Elephant Database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Set-up a cursor to read the elephant database
pg_curs = pg_conn.cursor()

# Query and fetchall info in elephant database
pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall())

# ETL - Extract, Transform, Load Pipeline
import sqlite3

# Use sqlite3 and retrieve the RPG database
sl_conn = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
print(sl_conn) # Test to see imported library is retrieved

# Setup a sqlite3 cursor to read the database
sl_curs = sl_conn.cursor()

# Query and fetchall() from rpg database
print(sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall())

# From the rpg database, get all the columns from the table (charcre_char)
# Extract from sqlite3 rpg database
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
print(len(characters)) # Same as COUNT()

# Look at the first characters and last characters
print('First line:', characters[0], 'Last line:', characters[-1])

# CREATE TABLE to load to PostgreSQL - This will be our character schema
# Pre- Load
# Sets up table to be loaded to postgreSQL database
create_character_table = '''
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
'''
############################################################
# Read through the table we created above
#print(pg_curs.execute(create_character_table))

# Define INSERT INTO 
attempted_insert = '''
    INSERT INTO charactercreator_character
    VALUES ''' + str(characters[0])
print(attempted_insert)

# INSERT INTO created table
#print(pg_curs.execute(attempted_insert))

# Changing Databases - CREATE or INSERT a table. You have to commit to make it work
pg_conn.commit() 
###############################################################
# Can't create duplicate so comment out the above ####### to #########

# After commit - Query the newly created and insert info
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
print(pg_curs.fetchall())

# Only INSERT INTO 1 row
print('Row:',pg_characters[0], 'Row Length:', len(pg_characters))

# INSERT INTO the rest of the rows to postgresql database
# for character in characters[1:]:
#     insert_character = '''
#     INSERT INTO charactercreator_character
#     VALUES ''' + str(character)
#     pg_curs.execute(insert_character)
pg_conn.commit() # Can't duplicate so comment out the for loop

# Restart the cursor
pg_curs = pg_conn.cursor()
# Query the finished table from loaded to postgresql database
pg_curs.execute('SELECT * FROM charactercreator_character')
# Fetch all table
pg_characters = pg_curs.fetchall()
print('Row:', pg_characters, 'Row Length:', len(pg_characters))

# Test our RPG database to our PostgreSQL database - No Error
for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character