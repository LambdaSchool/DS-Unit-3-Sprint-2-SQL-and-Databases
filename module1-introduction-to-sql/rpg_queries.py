import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


#How many total Characters are there?
curs.execute("""
    SELECT COUNT(name)
    FROM charactercreator_character;
    """)
characters = curs.fetchall()[0][0]
print('There are', characters, 'characters in total.')


#How many of each specific subclass?
curs.execute("""
    SELECT COUNT(character_ptr_id)
    FROM charactercreator_cleric;
    """)
clerics = curs.fetchall()[0][0]

curs.execute("""
    SELECT COUNT(character_ptr_id)
    FROM charactercreator_fighter;
    """)
fighters = curs.fetchall()[0][0]

curs.execute("""
    SELECT COUNT(character_ptr_id)
    FROM charactercreator_mage;
    """)
mages = curs.fetchall()[0][0]

curs.execute("""
    SELECT COUNT(mage_ptr_id)
    FROM charactercreator_necromancer;
    """)
necromancers = curs.fetchall()[0][0]

curs.execute("""
    SELECT COUNT(character_ptr_id)
    FROM charactercreator_thief;
    """)
thieves = curs.fetchall()[0][0]

print(clerics, 'Clerics,', fighters, 'Fighters,', 
      mages, 'Mages,', necromancers, 'Necromancers, and', thieves, 'Thieves')


#How many total Items?
curs.execute("""
    SELECT COUNT(item_id)
    FROM armory_item;
    """)
items = curs.fetchall()[0][0]
print('There are', items, 'itmes in total.')


#How many of the Items are weapons? How many are not?
curs.execute("""
    SELECT COUNT(item_ptr_id)
    FROM armory_weapon;
    """)
weapons = curs.fetchall()[0][0]
print(weapons, 'weapons, and', items - weapons, 'non-weapons')


#How many Items does each character have? (Return first 20 rows)
curs.execute("""
    SELECT COUNT(item_id), character_id
    FROM charactercreator_character_inventory
    GROUP BY character_id;
    """)
items_per_char = curs.fetchall()
items_df = pd.DataFrame(items_per_char, columns = ['total_items', 'char_id'])
print(items_df.head(20))


#How many Weapons does each character have? (Return first 20 rows)
curs.execute("""
    SELECT COUNT(item_ptr_id), character_id
    FROM charactercreator_character_inventory
    LEFT JOIN armory_weapon
    ON item_ptr_id = item_id
    GROUP BY character_id;
    """)
weap_per_char = curs.fetchall()
weapons_df = pd.DataFrame(weap_per_char, columns = ['total_weapons', 'character_id'])
print(weapons_df.head(20))


#On average, how many Items does each Character have?
average = sum(items_df['total_items']) / len(items_df)
print('Each character has', average, 'items on average.')


#On average, how many Weapons does each character have?
average = sum(weapons_df['total_weapons']) / len(weapons_df)
print('Each character has', average, 'weapons on average.')

curs.close()
conn.commit()