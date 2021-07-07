# %% SQLite3 -> PostgreSQL
# A Python script by Tobias Reaper
# ---
# Connects and interacts with databases
# - SQLite3
# - PostgreSQL
#
# Copies data from sqlite to postgres.

# %% Imports
from pprint import pprint

import psycopg2
import sqlite3
import os

# %% Get Postgres URL from environment variables
# URL includes all necessary info for connection
pg_url = os.environ["RPG_DB_URL"]

# %% Test context managed interaction
# Create a test table

test_table_create = """--- Create `test` table
CREATE TABLE test (
    test_id SERIAL PRIMARY KEY,
    file VARCHAR(30),
    count INT,
    success BOOL
);"""

test_table_insert = """--- Insert data into `test` table
INSERT INTO 
    test (file, count, success)
VALUES
    ('deftools.py', 5, true);"""

test_table_select = """--- Insert data into `test` table
SELECT
    *
FROM
    test;"""

with psycopg2.connect(pg_url) as conn:
    cur = conn.cursor()

    cur.execute(test_table_create)  # Create table
    cur.execute(test_table_insert)  # Insert data
    cur.execute(test_table_select)  # Select data
    select = cur.fetchall()  # To return

    cur.close()
    conn.commit()

# %% Another insert and select, with return

test_table_insert2 = """--- Insert data into `test` table
INSERT INTO 
    test (file, count, success)
VALUES
    ('workflow.py', 3, false);"""

test_table_select2 = """--- Insert data into `test` table
SELECT
    *
FROM
    test;"""

with psycopg2.connect(pg_url) as conn:
    cur = conn.cursor()

    cur.execute(test_table_insert2)  # Insert data
    cur.execute(test_table_select2)  # Select data
    select = cur.fetchall()  # To return
    print(select)

    cur.close()
    conn.commit()

# %% Function to reuse the query code
def quarry(conn, query, returns=True):
    """
    Runs a query against a database and commits changes.
    Does not close the connection - use a context manager if possible.
    
    Parameters
    ----------
    connection : connection object
        The connection object which allows interaction with the db.
    query : string
        SQL query to be run against the db.
    returns : bool
        If query returns a value (such as with SELECT), this should be True.
        If query does not return a value, (CREATE TABLE / INSERT), then False.
    """
    # Create cursor object
    cur = conn.cursor()

    # Execute the query
    cur.execute(query)

    # If returns is True, assign the query to variable
    if returns:
        results = cur.fetchall()
        pprint(results)

    # If not, do not create variable to return
    # Close the cursor and the connection
    cur.close()
    conn.commit()

    # If returns is True, return the return value
    if returns:
        return results


# %% Set up the sqlite3 filepath and query string
path1 = "/Users/Tobias/workshop/dasci/sprints/10-SQL_and_Databases"
path2 = "DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis"
dir_path = os.path.join(path1, path2)

# Specify the location of the db in the filesystem
filename = "rpg_db.sqlite3"
file_path = os.path.join(dir_path, filename)

character_query = """--- Get all rows from sqlite3 character table
SELECT
    *
FROM
    charactercreator_character;"""

# %% Get character data from sqlite3 db
# Open context manager to access / pull from sqlite3 db
with sqlite3.connect(file_path) as conn:
    characters = quarry(conn, character_query)

# %% Create 'character' table in postgres
create_char_table = """--- Create postgres table from sqlite3
CREATE TABLE character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);"""

# Get the quarry! and create the character table
with psycopg2.connect(pg_url) as conn:
    quarry(conn, create_char_table, False)

# %% New version of quarry function
# For parameterized queries
def quarry(conn, query, params=None, returns=True):
    """
    Runs a query against a database and commits changes.
    Does not close the connection - use a context manager if possible.
    
    Parameters
    ----------
    connection : connection object
        The connection object which allows interaction with the db.
    query : string
        SQL query to be run against the db.
    params : object
        Python object(s) to be passed into query as parameter(s).
    returns : bool
        If query returns a value (such as with SELECT), this should be True.
        If query does not return a value, (CREATE TABLE / INSERT), then False.
    """
    # Create cursor object
    cur = conn.cursor()

    # Execute the query
    if params is not None:
        cur.execute(query, params)
    else:
        cur.execute(query)

    # If returns is True, assign the query to variable
    if returns:
        results = cur.fetchall()
        pprint(results)

    # If not, do not create variable to return
    # Close the cursor and the connection
    cur.close()
    conn.commit()

    # If returns is True, return the return value
    if returns:
        return results


# %% Insert the characters data
# Only you can prevent Bobby Tables!
# ...with paramaterized queries.

# Query to confirm insert was successful
select_characters = """
    SELECT
        *
    FROM
        character;"""

with psycopg2.connect(pg_url) as conn:
    for character in characters:
        # Create the query string for each character
        insert_character = """INSERT INTO character
            (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

        char_data = (
            character[1],
            character[2],
            character[3],
            character[4],
            character[5],
            character[6],
            character[7],
            character[8],
        )

        # Create each character record using the quarry function
        quarry(conn, insert_character, char_data, False)

    # Select the table after all characters are added
    pg_characters = quarry(conn, select_characters)

# %%
