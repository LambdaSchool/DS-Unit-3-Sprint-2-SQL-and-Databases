import sqlite3

# Database
conn = sqlite3.connect('rpg_db.sqlite3')

conn
# Goes through the database - can have multiple
curs = conn.cursor()

curs

# Make a query
query = 'SELECT COUNT(*) FROM armory_item;'

# Save results of query
result = curs.execute(query)
result

# Fetch all results from the query
result.fetchall()


# SELECT * selects all
query = 'SELECT * FROM armory_item;'
result = curs.execute(query)
result.fetchall()

# Fetch one result from the query
result = curs.execute(query)
# Once fetched then it'll won't be in there.
result.fetchone()

############## DB Browser for SQLite ###########
'''
# Select all columns from the armory_item table
SELECT * FROM armory_item

# Select the table where item_id is 167, 45, 27
WHERE item_id IN(167, 45, 27);


'''

############## Create a new table ###############

import sqlite3
conn = sqlite3.connect('toy_db_sqlite3')

# Create a table, toy_id, 
create_statement = '''CREATE TALBE toy (
    toy_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    toy_name varchar(30),
    price numeric,
    small_parts integer)'''

# 
curs = conn.cursor()

# Create table
curs.execute(create_statement)

# Create new values for the table
insert = "INSERT INTO toy VALUES (1, 'Legos', 10.5, 1), (2, 'Train', 17.6, 0);"
# Exevute query
curs.execute(insert)


# Explicit Inner Join#
'''
SELECT 
name, mana
FROM charactercreator_mage
INNER JOIN charactercreator_character
ON charactercreator_mage.character_ptr_id = 
charactercreator_character.character_id;
'''
# Implicit Inner Join #
'''
SELECT name, mana
FROM charactercreator_mage, charactercreator_character
WHERE charactercreator_character.character_id =
charactercreator_mage.character_ptr_id;
'''
# Alias by using AS #
'''
SELECT cc.name, cm.mana
FROM charactercreator_mage AS cm, charactercreator_character AS cc
WHERE cc.character_id = cm.character_ptr_id;
'''