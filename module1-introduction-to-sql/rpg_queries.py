import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print('\nQ1: How many total Characters are there?')
query = "SELECT COUNT(*) FROM charactercreator_character;"
total_chars = curs.execute(query).fetchall()[0][0]
print(total_chars)

print('\nQ2: How many of each specific subclass?')
subclasses = ['mage', 'thief', 'cleric', 'fighter']
for subclass in subclasses:
    query = "SELECT COUNT(character_ptr_id) FROM charactercreator_" + subclass + ";"
    sub_count = curs.execute(query).fetchall()[0][0]
    print(subclass + ': ' + str(sub_count))

print('\nQ3: How many total Items?')
query = "SELECT COUNT(item_id) FROM armory_item;"
total_items = curs.execute(query).fetchall()[0][0]
print(total_items)

print('\nQ4: How many of the Items are weapons? How many are not?')
query = "SELECT COUNT(*) FROM armory_weapon;"
num_weapons = curs.execute(query).fetchall()[0][0]
print('Number of items that are weapons: ' + str(num_weapons)) 
print('Number of items that are not weapons: ' + str(total_items - num_weapons))

print('\nQ5: How many Items does each character have? (Return first 20 rows)')
query = "SELECT character_id, COUNT(*) as num_items FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;"
first20_char_items = curs.execute(query).fetchall()
print('\nChar ID | # of items')
for row in first20_char_items:
    print(str(row[0]) + '       |      ' + str(row[1]))

print('\nQ6: How many Weapons does each character have? (Return first 20 rows)')
query = "SELECT character_id, COUNT(*) as num_weapons FROM charactercreator_character_inventory as cci, armory_weapon as aw WHERE aw.item_ptr_id = cci.item_id GROUP BY character_id LIMIT 20;"
first20_char_weapons = curs.execute(query).fetchall()
print('\nChar ID | # of weapons')
for row in first20_char_weapons:
    print(str(row[0]) + '       |      ' + str(row[1]))

print('\nQ7: On average, how many Items does each Character have?')
query = "SELECT AVG(num_items) FROM (SELECT character_id, COUNT(*) as num_items FROM charactercreator_character_inventory GROUP BY character_id);"
avg_items = curs.execute(query).fetchall()[0][0]
print(avg_items)

print('\nQ8: On average, how many Weapons does each character have?')
query = "SELECT COUNT(*) AS num_weapons FROM charactercreator_character_inventory AS cci, armory_weapon AS aw WHERE aw.item_ptr_id = cci.item_id"
total_num_weapons = curs.execute(query).fetchall()[0][0]
print(total_num_weapons / total_chars)