# %% RPG Queries
# A Python script by Tobias Reaper
# ---
# Queries the "rpg_db.sqlite3" database
# Saving and printing the results

# %% Imports
import sqlite3
import os

# %% Create the path object
# Where the database is located
path1 = "/Users/Tobias/workshop/dasci/sprints/10-SQL_and_Databases"
path2 = "DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/"
filename = "rpg_db.sqlite3"
db_fullpath = os.path.join(path1, path2, filename)

print(db_fullpath)

# %% Create the connection object
# Which is the connection to the database
conn = sqlite3.connect(db_fullpath)

# %% Create the cursor object for the connection
cur = conn.cursor()

# %% Set up all of the queries to be run
# First as separate strings
# Then collect them into a list

query1 = """--- Total characters
SELECT COUNT(*) name
FROM charactercreator_character;
"""

query2 = """--- Total: cleric
SELECT COUNT(*)
FROM charactercreator_cleric;
"""

query3 = """--- Total: fighter
SELECT COUNT(*)
FROM charactercreator_fighter;
"""

query4 = """--- Total: mage
SELECT COUNT(*)
FROM charactercreator_mage;
"""

query5 = """--- Total: necromancer
SELECT COUNT(*)
FROM charactercreator_necromancer;
"""

query6 = """--- Total: thief
SELECT COUNT(*)
FROM charactercreator_thief;"""

query7 = """--- How many total Items?
SELECT COUNT(*)
FROM armory_item;"""

query8 = """--- How many of the Items are weapons? 
SELECT
    COUNT(*)
FROM 
    armory_item as ai, 
    armory_weapon as aw
WHERE 
    ai.item_id = aw.item_ptr_id;"""

query9 = """--- How many are not?
SELECT
    COUNT(*) name
FROM 
    armory_item as ai
LEFT JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
WHERE item_ptr_id IS NULL;"""

query10 = """--- How many Items does each character have? (Return first 20 rows)
SELECT 
    COUNT(*) item_id
FROM
    charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;"""

query11 = """--- How many Weapons does each character have? (Return first 20 rows)
SELECT
    COUNT(*) item_ptr_id
FROM
    charactercreator_character_inventory as inv
INNER JOIN armory_weapon as aw 
    ON inv.item_id = aw.item_ptr_id
GROUP BY inv.character_id
LIMIT 20;"""

query12 = """--- On average, how many Items does each Character have?
SELECT
    ROUND(AVG(item_count), 2)
FROM
    (SELECT 
        character_id, COUNT(item_id) item_count
    FROM
        charactercreator_character_inventory
    GROUP BY character_id);"""

query13 = """--- On average, how many Weapons does each character have?
SELECT
    ROUND(AVG(weapon_count), 2)
FROM
    (SELECT 
        character_id, COUNT(item_ptr_id) weapon_count
    FROM
        charactercreator_character_inventory inv
    LEFT JOIN armory_weapon as aw
        ON inv.item_id = aw.item_ptr_id
    GROUP BY character_id);"""

# Create list of queries to run in loop
query_list = [
    query1,
    query2,
    query3,
    query4,
    query5,
    query6,
    query7,
    query8,
    query9,
    query10,
    query11,
    query12,
    query13,
]

# Instantiate a dictionary to hold the results of each query
query_results = {}

# %% Loop through indexes of `query_list`
for q in range(13):
    # Set the name of the query equal to its result in `query_results`
    query_results[f"query{q + 1}"] = cur.execute(query_list[q]).fetchall()
    print()  # Empty line to make it more readable

    # Print out the first line of the query
    # This is a comment saying what the query does
    print(query_list[q].split("\n", 1)[0])

    # Print the results in a more readable format
    for row in query_results[f"query{q + 1}"]:
        print(row[0])

# %% Close the cursor
cur.close()

# %% If needed, the results can be accessed
# without running the queries again
# Simply print out the `query_results` dictionary
