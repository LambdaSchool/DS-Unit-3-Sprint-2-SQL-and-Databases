import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Q1
query_char = """SELECT count(cc.character_id)
FROM charactercreator_character as cc; 
"""
char_result = curs.execute(query_char)
print('\nQ1')
print('How many total Characters are there?')
print('There are ', char_result.fetchall().pop()[0], 'Characters.')

# Q2
char_tables = ['charactercreator_mage',
'charactercreator_necromancer',
'charactercreator_thief',
'charactercreator_cleric',
'charactercreator_fighter']

num_subs = len(char_tables)
print('\nQ2')
print('How many of each specific subclass?')
print('There are %d subclasses' % (num_subs))


for char in char_tables:
    
    #the necromancer has a different ptr_id so it needs a special case
    if char == 'charactercreator_necromancer':
        query = 'SELECT count(%s.mage_ptr_id) FROM %s' % (char, char)            
        
    else:
        #thief, cleric, fighter query
        query = 'SELECT count(%s.character_ptr_id) FROM %s' % (char, char)

    #execute querries
    result = curs.execute(query)

    # print results
    output = result.fetchall().pop()[0]
    #subract necros from mages
    if char == 'charactercreator_mage':
        necros = curs.execute('SELECT count(charactercreator_necromancer.mage_ptr_id) FROM charactercreator_necromancer').fetchall().pop()[0]
        output = output - necros

    print('There are ', output, ' ', char,'s')


    
# Q3
print('\nQ3')
print('How many total Items?')

query = """SELECT count(ai.item_id)
FROM armory_item as ai; 
"""
result = curs.execute(query)
print('There are ', result.fetchall().pop()[0], 'total Items.')

# Q4 
print('\nQ4')
print('How many of the Items are weapons? How many are not?')

query = """SELECT count(aw.item_ptr_id)
FROM armory_weapon as aw; 
"""
result = curs.execute(query)
num_weapons = result.fetchall().pop()[0]


query = """select count(armory_item.item_id)
from armory_item
where armory_item.item_id
not in 
(SELECT item_id
FROM armory_item
join armory_weapon
ON armory_item.item_id = armory_weapon.item_ptr_id); 
"""
result = curs.execute(query)
num_items = result.fetchall().pop()[0]

print('There are ', num_weapons , ' weapons and ', num_items,' non weapon items.')

# Q5
print('\nQ5')
print('How many Items does each character have? (Return first 20 rows)')

query = """select character_id, count(item_id)
from charactercreator_character_inventory
group by character_id; 
"""
result = curs.execute(query)
num_items = result.fetchmany(20)

print('Char | # of ')
print('ID   | Items')
for x in num_items:
    print(x[0], ' | ', x[1])


# Q6
print('\nQ6')
print('How many Weapons does each character have? (Return first 20 rows)')

query = """select character_id, count(item_ptr_id) 
from charactercreator_character_inventory
join armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
group by character_id;
"""
result = curs.execute(query)
num_items = result.fetchmany(20)

print('Char | # of ')
print('ID   | weapons')
for x in num_items:
    print(x[0], ' | ', x[1])

# Q7
print('\nQ7')
print('On average, how many Items does each Character have?')

query = """select character_id, count(item_id)
from charactercreator_character_inventory
group by character_id; 
"""
result = curs.execute(query)
num_items = result.fetchall()

#get all the item tuples
total_items = 0
for item in num_items:
    total_items += item[1]
average_items = total_items/len(num_items)

print('Each Character on average has %s items' % average_items)

# Q8
print('\nQ8')
print('On average, how many Weapons does each Character have?')

query = """select character_id, count(item_ptr_id) 
from charactercreator_character_inventory
join armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
group by character_id;
"""
result = curs.execute(query)
num_items = result.fetchall()

#get all the item tuples
total_items = 0
for item in num_items:
    total_items += item[1]
average_items = total_items/len(num_items)

print('Each Character on average has %s Weapons' % average_items)