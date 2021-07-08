import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")

curs = conn.cursor()

# how many total characters are there?
query1 = '''SELECT COUNT(character_id) 
            FROM charactercreator_character;'''
#total_char = 
total_char = curs.execute(query1).fetchall()
print("There are total of {} characters.".format(total_char[0][0]))

# how many of each specific subclass?
query2_1 = '''SELECT COUNT(character_ptr_id)
            FROM charactercreator_mage;'''
mages = curs.execute(query2_1).fetchall()
print("There are total of {} mages.".format(mages[0][0]))

query2_2 = '''SELECT COUNT(character_ptr_id)
            FROM charactercreator_thief;'''

thiefs = curs.execute(query2_2).fetchall()
print("There are total of {} thiefs.".format(thiefs[0][0]))
            
query2_3 = '''SELECT COUNT(character_ptr_id)
            FROM charactercreator_cleric;'''
            
clerics = curs.execute(query2_3).fetchall()
print("There are total of {} clerics.".format(clerics[0][0]))

query2_4 = '''SELECT COUNT(character_ptr_id)
            FROM charactercreator_fighter;'''

fighters = curs.execute(query2_4).fetchall()
print("There are total of {} fighters.".format(fighters[0][0]))

query2_5 = '''SELECT COUNT(mage_ptr_id)
            FROM charactercreator_necromancer;'''
necros = curs.execute(query2_5).fetchall()
print("There are total of {} necromancers.".format(necros[0][0]))

# how many total Items?
query3_1 = '''SELECT COUNT(item_id) 
            FROM charactercreator_character_inventory;'''
items_total = curs.execute(query3_1).fetchall()
print("There are total of {} items.".format(items_total[0][0]))
            
query3_2 = '''SELECT COUNT(item_id) 
              FROM armory_item;'''
unique_items = curs.execute(query3_2).fetchall()
print("There are total of {} unique items.".format(unique_items[0][0]))


# how many of the Items are weapons? How many are not?
query4_1 = '''SELECT COUNT(item_ptr_id) FROM armory_weapon;'''
weapons = curs.execute(query4_1).fetchall()
print("There are total of {} weapons and {} non-weapons.".format(weapons[0][0], unique_items[0][0] - weapons[0][0]))


# how many items does each character have? (return first 20 rows)
query5 = '''SELECT character_id, count(item_id) FROM charactercreator_character_inventory
            GROUP BY character_id LIMIT 20;'''
char_items = curs.execute(query5).fetchall()
print("Number of items that the first 20 characters have: \n {}".format(char_items))

# how many weapons does each character have? (return first 20 rows)
query6 = '''SELECT character_id, count(item_id)
            FROM charactercreator_character_inventory, armory_weapon
            WHERE item_id = item_ptr_id
            GROUP BY character_id LIMIT 20;'''
char_weapons = curs.execute(query6).fetchall()
print("Number of items that the first 20 characters have: \n {}".format(char_weapons))

# on average, how many Items does each character have?
query7 = '''SELECT AVG(item_counts)
            FROM (
                SELECT character_id, count(item_id) as item_counts
                FROM charactercreator_character_inventory
                GROUP BY character_id
            );'''
avg_item = curs.execute(query7).fetchall()
print("On average, each character have {} items.".format(avg_item[0][0]))

# on average, how many Weapons does each character have?
query8 = '''SELECT AVG(weapon_counts)
            FROM (
                SELECT character_id, count(item_id) AS weapon_counts
                FROM charactercreator_character_inventory, armory_weapon
                WHERE item_id = item_ptr_id
                GROUP BY character_id
            );'''
avg_weap = curs.execute(query8).fetchall()
print("On average, each character have {} weapons.".format(avg_weap[0][0]))

curs.close()
conn.commit()
