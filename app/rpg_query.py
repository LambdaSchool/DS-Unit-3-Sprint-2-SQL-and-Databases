# app/chinook_query.py

import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print ("Connection", connection)

cursor = connection.cursor()
print ("Cursor", cursor)
# How many total Characters are there?
query_1 =  """
SELECT COUNT (DISTINCT character_id) 
FROM charactercreator_character
"""

result_1 = cursor.execute(query_1).fetchall()
print("How many total Characters are there?", result_1)
# How many of each specific subclass?
# How many total Items?
query_3 = """
SELECT COUNT (DISTINCT item_id)
FROM armory_item
"""

result_3 = cursor.execute(query_3).fetchall()
print("How many total Items?", result_3)

# How many of the Items are weapons?
query_4 = """
SELECT count (DISTINCT item_ptr_id)
FROM armory_weapon
"""

result_4 = cursor.execute(query_4).fetchall()
print("How many of the Items are weapons?", result_4)

# How many Items does each character have? (Return first 20 rows)
query_5 ="""
SELECT c.character_id, c.name, COUNT (i.item_id) as item_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory i
ON c.character_id = i.character_id
GROUP BY c.character_id
LIMIT 20
"""
result_5 = cursor.execute(query_5).fetchall()
print("How many Items does each character have? (Return first 20 rows)", result_5)

# How many Weapons does each character have?
query_6 = """
SELECT c.character_id, c.name, COUNT (w.item_ptr_id) as w_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory i
ON c.character_id = i.character_id
LEFT JOIN armory_weapon w
ON i.item_id = w.item_ptr_id
GROUP BY c.character_id
LIMIT 20
"""

result_6 = cursor.execute(query_6).fetchall()
print("How many Weapons does each character have?", result_6)

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
query_7 = """
-- On average, how many Weapons does each character have? 
-- one single row with the avg as a single col
SELECT 
  count(distinct character_id) as character_count -- 302
  ,avg(item_count) as avg_items -- 2.97
  ,avg(weapon_count) as avg_weapons -- 0.67
FROM (
    -- row per character (302 rows)
    -- one col for the char id, one for the char name, third for the weapon count
    SELECT 
      ch.character_id
      ,ch."name" as char_name
      -- ,inv.id 
      ,count(distinct inv.item_id) as item_count
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character ch
    LEFT JOIN charactercreator_character_inventory inv ON ch.character_id = inv.character_id
    LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
    GROUP BY 1,2
) subq

"""

result_7 = cursor.execute(query_7).fetchall()
print("On average, how many Items does each Character have? On average, how many Weapons does each character have?", result_7)
