# From the cmd prompt set-up a virtual enviornment 
# `pipenv install ...` is the dir

# Run `pipenv shell` to activate

import sqlite3

# Connect to a database and if there's is none it will create one
conn = sqlite3.connect('rpg_db.sqlite3')

# Used to make queries
curs = conn.cursor()

# Execute query and fetch all the data
result = curs.execute('SELECT * FROM armory_item;')
result.fetchall()
# print(result.fetchall())

############### Create a new table ###############

# 'toy_db_sqlite3' doesn't exist so it will create one
conn = sqlite3.connect('toy_db_sqlite3')

# Create a table called toy
create_toy_table = '''CREATE TABLE toy (
    toy_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    toy_name VARCHAR(30),
    price NUMERIC,
    small_parts integer
)
'''

# Create a cursor to make queries
curs = conn.cursor()

# Execute `create_toy_table` to create the table
## Is empty right now since we didn't populate it
#curs.execute(create_toy_table)
## Comment out above line since we can't create duplicates
# print(curs.execute(create_toy_table).fetchall())

# INSERT INTO toy VALUES to create new values of fields/col

insert = "INSERT INTO toy VALUES (1, 'Legos', 10.5, 1), (2, 'Train', 17.6, 0);"

# Execute to insert new values to toy table
curs.execute(insert)

# Fetch all from toy database - toy_db is a list
toy_db = curs.execute('SELECT * FROM toy;').fetchall()

######### Try to launch it to elephantsql #####

import psycopg2

# Enter/Re enter details from elephantsql

dbname = 'oxwfzsio'
user = 'oxwfzsio'
password = ''
host = 'raja.db.elephantsql.com'

# connect to elephantsql
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Used to read the database on elephantsql
pg_curs = pg_conn.cursor()

# Create an empty table for ElephantSQL
create_toy_table_esql = '''CREATE TABLE toy (
    toy_id integer NOT NULL PRIMARY KEY,
    toy_name VARCHAR(30),
    price NUMERIC,
    small_parts integer
)
'''
# Execute to create an empty table for ESQL
pg_curs.execute(create_toy_table_esql)

# # Execute previous created toy database
for row in toy_db:
    insert_row = '''
    INSERT INTO toy VALUES ''' + str(row)
    pg_curs.execute(insert_row)

# Commit to see the changes on elephantsql
pg_conn.commit()