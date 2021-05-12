#!/usr/bin/env python

"""
RPG Queries for DS1 SQL
"""

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

characters_num_query = """SELECT COUNT(character.character_id)
FROM charactercreator_character AS character"""

subclass_num_query = """ SELECT ( 
			SELECT COUNT(*)
			FROM charactercreator_cleric
			) AS count_cleric,
			(
			SELECT COUNT(*)
			FROM charactercreator_fighter
			) AS count_fighter,
			(
			SELECT COUNT(*)
			FROM charactercreator_mage
			) AS count_mage,
			(
			SELECT COUNT(*)
			FROM charactercreator_necromancer
			) AS count_necromancer,
			(
			SELECT COUNT(*)
			FROM charactercreator_thief
			) AS count_thief;"""

items_num_query = """ SELECT COUNT(armory_item.item_id) 
FROM armory_item AS items;"""

weapons_num_query = """SELECT COUNT(armory_weapon.item_ptr_id) 
FROM armory_weapon AS weapons;"""

non_weapons_num_query = """SELECT (SELECT COUNT(armory_item.item_id) 
FROM armory_item) - (SELECT COUNT(armory_weapon.item_ptr_id) 
FROM armory_weapon) AS non_weapons;"""

characters_items_query =  """SELECT character_id, COUNT(character_id) AS total_items
FROM charactercreator_character_inventory 
GROUP BY character_id 
LIMIT 20;"""

characters_weapons_query = """SELECT charactercreator_character_inventory.character_id, 
COUNT(charactercreator_character_inventory.character_id)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20;"""

avg_items_query = """SELECT AVG(total_items) FROM
(SELECT COUNT(character_id) AS total_items
FROM charactercreator_character_inventory 
GROUP BY character_id)"""

avg_weapons_query = """SELECT AVG(total_weapons) FROM
(
SELECT charactercreator_character_inventory.character_id, 
COUNT(charactercreator_character_inventory.character_id) as total_weapons
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
)"""