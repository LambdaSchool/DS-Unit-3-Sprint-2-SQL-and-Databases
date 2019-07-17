
# coding: utf-8

# In[1]:


import sqlite3


# In[3]:


conn = sqlite3.connect('rpg_db.sqlite3')


# In[4]:


c = conn.cursor()
print('Opened as needed')


# Use sqlite3 to load and write queries to explore the data, and answer the following questions:
# 
#     How many total Characters are there?
#     How many of each specific subclass?
#     How many total Items?
#     How many of the Items are weapons? How many are not?
#     How many Items does each character have? (Return first 20 rows)
#     How many Weapons does each character have? (Return first 20 rows)
#     On average, how many Items does each Character have?
#     On average, how many Weapons does each character have?
# 

# In[45]:


c.execute('''SELECT COUNT(character_id) FROM charactercreator_character''')
print(f"The total number of characters is {c.fetchall()[0][0]}")


# In[66]:



c.execute(f'''SELECT COUNT(character_id) FROM charactercreator_character INNER JOIN charactercreator_cleric
WHERE character_id == character_ptr_id ''')
print(f"There are {c.fetchall()[0][0]} clerics")

c.execute(f'''SELECT COUNT(character_id) FROM charactercreator_character INNER JOIN charactercreator_fighter
WHERE character_id == character_ptr_id ''')
print(f"There are {c.fetchall()[0][0]} fighters")


c.execute(f'''SELECT COUNT(character_id) FROM charactercreator_character INNER JOIN charactercreator_mage
WHERE character_id == character_ptr_id ''')
print(f"There are {c.fetchall()[0][0]} magi")


c.execute(f'''SELECT COUNT(character_id) FROM charactercreator_character INNER JOIN  charactercreator_necromancer
WHERE character_id == mage_ptr_id ''')
print(f"There are {c.fetchall()[0][0]} necromancers")


c.execute(f'''SELECT COUNT(character_id) FROM charactercreator_character INNER JOIN charactercreator_thief
WHERE character_id == character_ptr_id ''')
print(f"There are {c.fetchall()[0][0]} thiefs")


# In[20]:


c.execute('''SELECT COUNT(item_id) FROM armory_item''')
arm_item = c.fetchall()
print(f"The total number of armory items is {arm_item[0][0]}")
#print(arm_item[0][0])


# In[21]:


c.execute('''SELECT COUNT(item_ptr_id) FROM armory_weapon''')
arm_wep = c.fetchall()
difference = arm_item[0][0] - arm_wep[0][0]
print(f"The total number of armory weapon items is {arm_wep[0][0]}")
print(f'There are {difference} items that are not weapons')


# In[34]:


c.execute('''SELECT name,  COUNT(item_id) FROM charactercreator_character_inventory INNER JOIN 
charactercreator_character USING (character_id)
GROUP BY name 
ORDER BY character_id LIMIT 20
''');

item_per_character = c.fetchall()
print(f"The total number of armory items per character is {item_per_character}")


# In[92]:


c.execute('''SELECT name,  COUNT(item_ptr_id) FROM charactercreator_character INNER JOIN 
armory_weapon, charactercreator_character_inventory USING (character_id)
WHERE item_ptr_id == item_id
GROUP BY name 
ORDER BY character_id LIMIT 20
''');

weapons_per_character = c.fetchall()
print(f"The total number of armory weapon items per character is {weapons_per_character}")


# In[93]:


c.execute('''SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory
''');

item_per_character = c.fetchall()
print(f"The avg number of armory items per character is {item_per_character[0][1]/item_per_character[0][0]}")


# In[96]:


c.execute('''SELECT COUNT(character_id),COUNT(item_ptr_id) FROM charactercreator_character INNER JOIN 
armory_weapon, charactercreator_character_inventory USING (character_id)''');

weapons_avgper_character = c.fetchall()
print(f"The total number of armory weapon items per character is {weapons_avgper_character[0][1]/weapons_avgper_character[0][1]}")

