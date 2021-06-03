import sqlite3

#question 1: How many total characters are there?
conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()
query = 'SELECT COUNT(character_id) FROM charactercreator_character;'
question1 = cursor.execute(query)
print('Question 1:', question1.fetchall())
print('_________')

#question 2: How many of each different subclass?
mage_query = 'SELECT * FROM charactercreator_mage'
mage_total = len(cursor.execute(mage_query).fetchall())

necromancer_query = 'SELECT * FROM charactercreator_necromancer'
necromancer_total = len(cursor.execute(necromancer_query).fetchall())

thief_query = 'SELECT * FROM charactercreator_thief'
thief_total = len(cursor.execute(thief_query).fetchall())

cleric_query = 'SELECT * FROM charactercreator_cleric'
cleric_total = len(cursor.execute(cleric_query).fetchall())

fighter_query = 'SELECT * FROM charactercreator_fighter'
fighter_total = len(cursor.execute(fighter_query).fetchall())

print('Question 2:')
print('Total Different Subclasses:')
print('Mages:', mage_total)
print('Necromancer:', necromancer_total)
print('Thief:', thief_total)
print('Cleric:', cleric_total)
print('Fighter:', fighter_total)
print('____')

#question 3: How many total items
item_query = 'SELECT * FROM armory_item'
item_total = len(cursor.execute(item_query).fetchall())

print('Question 3:', item_total)
print('____')

#question 4: How many are weapons? How many are not?
weapon_query = 'SELECT * FROM armory_weapon'
weapon_total = len(cursor.execute(weapon_query).fetchall())

nonweapon_query = 'SELECT * FROM armory_item'
nonweapon_total = len(cursor.execute(nonweapon_query).fetchall())
print('Question 4:')
print('Total Number of Weapons:', weapon_total)
print('Total Number of Items:', nonweapon_total)
print('____')

#question 5: How many items does each character have *** FIXME
for i in range(0, 20):
    #need to fix bucket and ques
    bucket = []
    question5_query = 'SELECT COUNT(armory_item) FROM charactercreator_character AS CC, armory_item AS AI, charactercreator_character_inventory AS CCI WHERE CC.character_id = CCI.character_id AND AI.item_id = CCI.item_id ORDER BY item_id LIMIT 20; '
    question5_total = cursor.execute(question5_query).fetchall()
    print('Question 5:')
    print('Total Number Items/User (Max 20:)', question5_total)
    print ('____')

#question 6: How many weapons does each character have *** FIXME
    question6_query = 'SELECT COUNT(armory_weapon) FROM charactercreator_character AS CC, armory_item AS AI, charactercreator_character_inventory AS CCI WHERE CC.character_id = CCI.character_id AND AI.item_id = CCI.item_id ORDER BY item_id LIMIT 20; '
    questio65_total = cursor.execute(question6_query).fetchall()
    print('Question 6:')
    print('Total Number Weapons/User (Max 20:)', question5_total)
    print ('____')

# question 7: On average, how many items does each Character Have?


#question 8: On average, how many weapons does each Character have?



##### PART 2: MAKING AND POPULATING DB #####
## BuddyMove DataSet ##
