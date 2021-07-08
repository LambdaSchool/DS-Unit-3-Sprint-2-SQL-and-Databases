#!/usr/bin/python


# Import packages
import sqlite3
import pandas as pd

# Create a connection to data file and set cursor
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor

def select_all_tasks(conn):
    '''
    Query all rows in the table
    '''


# Assignment Questions

# How many total Characters are there?

SELECT COUNT(*) AS total_characters
FROM charactercreator_character;

=302

# How many of each specific subclass?

# CLERICS = 75
SELECT COUNT(*) AS total_clerics
FROM charactercreator_cleric;

# FIGHERS = 68
SELECT COUNT(*) AS total_fighters
FROM charactercreator_fighter;

# MAGES = 108
SELECT COUNT(*) AS total_mages
FROM charactercreator_mage;

# NECROMANCERS = 11
SELECT COUNT(*) AS total_necros
FROM charactercreator_necromancer;

# THIEVES = 51
SELECT COUNT(*) AS total_thieves
FROM charactercreator_thief;

# How many total Items?

SELECT DISTINCT item_id AS item_count
FROM armory_item;

=174


# How many of the Items are weapons? How many are not?

SELECT DISTINCT item_ptr_id AS weapon_count
FROM armory_item;

=37

=174-37

# How many Items does each character have? (Return first 20 rows)

SELECT character_id, COUNT(item_id) as item_num
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;


# How many Weapons does each character have? (Return first 20 rowdef s)






# On average, how many Items does each Character have?

SELECT AVG(items) AS avg_items
FROM (charactercreator_character_inventory
      GROUP BY character_id
# On average, how many Weapons does each character have?