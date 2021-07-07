import psycopg2

# Re Enter
dbname = 'eczastgf'
user = 'eczastgf'
password = ''
host = 'raja.db.elephantsql.com'

# Connect to ElephantSQL
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Read the ElephantSQL database
pg_curs = pg_conn.cursor()

# Df to titanic database
import pandas as pd
from sqlalchemy import create_engine

# Save df
df = pd.read_csv('titanic.csv')

# Replace ' with an empty space
df['Name'] = df['Name'].str.replace('\'', ' ')

# Create engine - Used to convert a dataframe to database
engine = create_engine('sqlite://', echo=False)

# Create the new table on sql db
df.to_sql('titanic', con=engine)

# Titanic df is now a db - Is a list of tuples
titanic_db = engine.execute('SELECT * FROM titanic;').fetchall()

# Create an empty db for ElephantSQL
create_titanic_table = '''
    CREATE TABLE titanic (
        id integer NOT NULL PRIMARY KEY,
        survived INT,
        pclass INT,
        name VARCHAR(100),
        sex VARCHAR(10),
        age INT,
        siblings_spouses_aboard INT,
        parents_child_aboard INT,
        fare INT
    );
'''

# Read thourgh the table we created
pg_curs.execute(create_titanic_table)

# INSERT INTO the rest of the rows to postgresql database
for row in titanic_db:
    insert_row = '''
    INSERT INTO titanic
    VALUES ''' + str(row)
    pg_curs.execute(insert_row)

# Commit to Elephantsql and test from browser: SELECT * FROM titanic
pg_conn.commit()

# Create a local titanic db then upload to elephant db
"""
import sqlite3

# Reset index to get an index,id
df = df.reset_index().rename(columns={'index':'id'})

# Save a create a titanic database
sl_conn = sqlite3.connect('titanic.sqlite3')

# CREATE TYPE for titanic sex
# CREATE TABLE for titanic database
create_titanic_table = '''
    CREATE TABLE titanic (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        survived INT,
        pclass INT,
        name VARCHAR(100),
        sex VARCHAR(10),
        age INT,
        siblings_spouses_aboard INT,
        parents_child_aboard INT,
        fare INT
    );
'''

# Read the database
sl_curs = sl_conn.cursor()

# Create the table for the titanic database
#sl_curs.execute(create_titanic_table)
## Comment out since already created

# Define INSERT INTO
insert_titanic_db = '''
    INSERT INTO titanic
    VALUES ''' + str(tuple(df.loc[0, :].tolist()))

sl_curs.execute(insert_titanic_db)

# Fetch all data in titanic database
print(sl_curs.execute('SELECT * FROM titanic;').fetchall())
"""