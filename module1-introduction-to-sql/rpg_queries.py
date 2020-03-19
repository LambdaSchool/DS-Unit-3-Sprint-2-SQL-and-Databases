import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')


def execute(sql_query):
    curs = conn.cursor()
    return curs.execute(sql_query).fetchall()


# total characters
query = 'SELECT COUNT(*) FROM charactercreator_character'
print(f'Total Characters: {execute(query)[0][0]}')

# subclass counts
subclass = ['mage', 'thief', 'cleric', 'fighter', 'necromancer']
for x in subclass:
    if x == 'mage':
        query = f'SELECT COUNT(*) FROM charactercreator_{x}'
        query2 = 'SELECT COUNT(*) FROM charactercreator_necromancer'
        query3 = f'SELECT ({query}) - ({query2})'
        print(f'Mage Count: {execute(query3)[0][0]}')
    else:
        query = f'SELECT COUNT(*) FROM charactercreator_{x}'
        print(f'{x.capitalize()} Count: {execute(query)[0][0]}')

# total items
query = 'SELECT COUNT(*) FROM armory_item'
print(f'Total Items: {execute(query)[0][0]}')

# weapons vs not
query = 'SELECT COUNT(*) FROM armory_weapon'
query2 = 'SELECT COUNT(*) FROM armory_item'
query3 = f'SELECT ({query2}) - ({query})'
print(f'Weapon Count: {execute(query)[0][0]}')
print(f'Non-Weapon Item Count: {execute(query3)[0][0]}\n')

# Items per character
query = """
SELECT charactercreator_character.character_id, 
COUNT(charactercreator_character_inventory.item_id)
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory
ON charactercreator_character_inventory.character_id =
charactercreator_character.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""
counts = {f'Character Id: {i[0]}': f'Item Count: {i[1]}'
          for i in execute(query)}
print(pd.DataFrame.from_dict(data=counts, orient='index'))

# Weapons per character
query = """
SELECT charactercreator_character.character_id,
COUNT(armory_weapon.item_ptr_id)
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory
ON charactercreator_character_inventory.character_id =
charactercreator_character.character_id
LEFT JOIN armory_weapon 
ON charactercreator_character_inventory.item_id =
armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""
counts = {f'Character Id: {i[0]}': f'Weapon Count: {i[1]}'
          for i in execute(query)}
print(pd.DataFrame.from_dict(data=counts, orient='index'))

# Average items per character
query = """
SELECT AVG(count)
FROM
(
SELECT charactercreator_character.character_id, 
COUNT(charactercreator_character_inventory.item_id) AS count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory
ON charactercreator_character_inventory.character_id =
charactercreator_character.character_id
GROUP BY charactercreator_character.character_id
)
"""
print(f'Average Items Per Character: {execute(query)[0][0]}')

# Average Weapons Per Character
query = """
SELECT AVG(count)
FROM
(
SELECT charactercreator_character.character_id,
COUNT(armory_weapon.item_ptr_id) AS count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory
ON charactercreator_character_inventory.character_id =
charactercreator_character.character_id
LEFT JOIN armory_weapon 
ON charactercreator_character_inventory.item_id =
armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id
)
"""
print(f'Average Weapons Per Character: {execute(query)[0][0]}')
