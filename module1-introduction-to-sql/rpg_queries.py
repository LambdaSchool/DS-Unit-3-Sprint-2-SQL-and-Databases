"""
Python SLQ queries
"""

import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
import os
os.listdir()
conn
curs = conn.cursor()

# How many total Characters are there?
curs.execute('SELECT count(character_id) FROM charactercreator_character;').fetchall()
#%%

# How many of each specific subclass?
curs.execute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall()
#%%
curs.execute('SELECT count(character_ptr_id) FROM charactercreator_thief;').fecthall()
#%%
curs.execute('SELECT count(character_ptr_id) FROM charactercreator_cleric;').fetchall()
#%%
curs.execute('SELECT count(character_ptr_id) FROM charactercreator_fighter;').fecthall()
#%%
curs.execute('SELECT count(mage_ptr_id) FROM charactercreator_necromancer;').fetchall()
#%%

# How many total Items?
curs.execute('SELECT count(item_id) FROM armory_item;').fetchall()
#%%

# How many of the Items are weapons? How many are not?
curs.execute('SELECT count(item_id) FROM armory_item as ai, armory_weapon as aw WHERE ai.item_id = aw.item_ptr_id;').fetchall()
#%%

curs.execute('SELECT count(item_id) FROM armory_item WHERE item_id NOT IN(SELECT item_ptr_id FROM armory_weapon);').fetchall()
#%%

# How many Items does each character have? (Return first 20 rows)
curs.execute('SELECT count(item_id) FROM charactercreator_character_inventory as cci group by character_id LIMIT 20;').fetchall()
#%%

# How many Weapons does each character have? (Return first 20 rows)
curs.execute('SELECT count(item_ptr_id) FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE ai.item_id = cci.item_id AND ai.item_id = aw.item_ptr_id group by character_id LIMIT 20;').fetchall()
#%%

# On average, how many Items does each Character have?
curs.execute('SELECT avg(count) FROM (SELECT count(item_id) as count FROM charactercreator_character_inventory as cci group by character_id);').fetchall()
#%%

# On average, how many Weapons does each character have?
curs.execute('SELECT avg(count) FROM (SELECT count(item_ptr_id) as count FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE ai.item_id = cci.item_id AND ai.item_id = aw.item_ptr_id group by character_id)').fetchall()
#%%


curs.close()
conn.commit()


