# %% PostgreSQL Connection with Python
# A Python script by Tobias Reaper
# ---
# Connects and interacts with Postgres instance

# %% Imports
import psycopg2
import sqlite3
import os

# %% Grab envirovars
# db_name = os.environ["DB_NAME"]
# db_user = os.environ["DB_USER"]
# db_pass = os.environ["DB_PASS"]
# db_host = os.environ["DB_HOST"]

# Without envirovars
db_name = "wlleldkf"
db_user = "wlleldkf"
db_pass = "twt0_kqVgT98KK3e-LYi9Olj8OjXxR77"
db_host = "salt.db.elephantsql.com"

# %% Create postgres connection
pg_conn = psycopg2.connect(
    dbname=db_name, user=db_user, password=db_pass, host=db_host
)

# %% Create the postgres cursor
pg_cur = pg_conn.cursor()

# %% Execute test query
test_query = "SELECT * FROM testing_table;"

# Execute the query then fetch the data; separate steps
pg_cur.execute(test_query)
pg_cur.fetchall()

# %% Connect to the sqlite3 database
path1 = "/Users/Tobias/workshop/dasci/sprints/10-SQL_and_Databases"
path2 = "DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis"
dir_path = os.path.join(path1, path2)

filename = "rpg_db.sqlite3"
file_path = os.path.join(dir_path, filename)

lite_conn = sqlite3.connect(file_path)

# %% Create the sqlite3 cursor
lite_cur = lite_conn.cursor()

# %% Execute test query
lite_query1 = """--- Count the distinct character names
SELECT *
FROM charactercreator_character;"""

characters = lite_cur.execute(lite_query1).fetchall()
characters

# %%
lite_query_info = """PRAGMA table_info(charactercreator_character);"""

lite_cur.execute(lite_query_info).fetchall()

# %% Create table-creation query for postgres
create_char_table = """
--- Create postgres table from sqlite3
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

pg_cur.execute(create_char_table)

# %% Look at postgres table
show_tables = """
--- Show the postgres tables
SELECT
    *
FROM pg_catalog.pg_tables
WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""

pg_cur.execute(show_tables)
pg_cur.fetchall()

# %% Add a single character
one_char = str(characters[0][1:])

single_insert = (
    """
--- Example insert of one record
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """
    + one_char
)

# %%
for character in characters:
    insert_character = (
        """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """
        + str(character[1:])
        + ";"
    )
    pg_cur.execute(insert_character)

# %% Close the cursor and commit changes
pg_cur.close()
pg_conn.commit()

# %% Create new cursor to confirm INSERTion
pg_curs = pg_conn.cursor()
pg_cur.execute("SELECT * FROM charactercreator_character;")
pg_characters = pg_cur.fetchall()

print(characters[0])
print(pg_characters[0])

# %% Assert to be sure
for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

# %% Close out the cursor and commit changes
pg_cur.close()
pg_conn.commit()

# %% Close out the connections
lite_cur.close()  # First, close out the sqlite cursor
lite_conn.close()

pg_conn.close()
