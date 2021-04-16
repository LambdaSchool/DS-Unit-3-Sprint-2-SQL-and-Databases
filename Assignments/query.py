# New Query for todays assignment

import os
import sqlite3

datapath = os.path.join(os.path.dirname(__file__), ". .", "rpg_db.sqlite3")

connection = sqlite3.connect(datapath)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

weapon_count = '''
SELECT 
	character_id
	,COUNT(armory_weapon.item_ptr_id) as weapon_count
	FROM armory_weapon
		,charactercreator_character_inventory
		GROUP BY character_id
		LIMIT 20
               ''' 
item_count = '''
SELECT
	character_id
	,count(DISTINCT item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
             ''' 
character_count = '''
SELECT
  count(distinct character_id) as customer_count -- > counts actual unique values
FROM charactercreator_character

                  '''                           

weapons = cursor.execute(weapon_count).fetchall()
print("Weapons per Character:", weapons)  

items = cursor.execute(item_count).fetchall()
print("Items per character:", items)

total_char = cursor.execute(character_count).fetchall()
print("Total of characters:", total_char)