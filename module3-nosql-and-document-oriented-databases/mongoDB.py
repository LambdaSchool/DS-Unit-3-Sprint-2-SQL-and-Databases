""" MongoDB """

username = user
pass = pass

import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb://admin:<pass>@cluster0-shard-00-00-tbbec.mongodb.net:27017,cluster0-shard-00-01-tbbec.mongodb.net:27017,cluster0-shard-00-02-tbbec.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

client.nodes

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

query1 = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(query1).fetchall()

# my dictionary for charactercreator_character table
charactercreator_character = {}
for character in characters:
  cc = {
    'character_id' : character[0],
    'name' : character[1],
    'level' : character[2],
    'exp' : character[3],
    'hp' : character[4],
    'strength' : character[5],
    'intelligence' : character[6],
    'dexterity' : character[7],
    'wisdom' : character[8]
  }
  charactercreator_character.update({str(character[0]): cc})

# transfer data to mongoDB
db.test.insert_one(charactercreator_character)

# Confirm that table was added in mongoDB
print(db.test.find_one())

query2 = 'SELECT * FROM armory_item;'
items = sl_curs.execute(query2).fetchall()

# my dictionary for armory_item table
armory_item = {}
for item in items:
  ai = {
    'item_id': item[0],
    'name' : item[1],
    'value' : item[2],
    'weight' : item[3]
}
  armory_item.update({str(item[0]): ai})

# transfer data to mongoDB
db.test.insert_one(armory_item)

# Confirm that table was added in mongoDB
print(db.test.find(armory_item))

query3 = 'SELECT * FROM armory_weapon;'
weapons = sl_curs.execute(query3).fetchall()

# my dictionary for armory_weapon table
armory_weapon = {}
for weapon in weapons:
  aw = {
    'item__ptr_id': item[0],
    'power' : item[1]
}
  armory_weapon.update({str(weapon[0]): aw})

# transfer data to mongoDB
db.test.insert_one(armory_weapon)

# Confirm that table was added in mongoDB
print(db.test.find(armory_weapon))

query4 = 'SELECT * FROM charactercreator_character_inventory;'
stocks = sl_curs.execute(query4).fetchall()

# my dictionary for charactercreator_character_inventory table
charactercreator_character_inventory = {}
for stock in stocks:
  cci = {
    'id': stock[0],
    'character_id' : stock[1],
    'item_id' : stock[2]
}
  charactercreator_character_inventory.update({str(stock[0]): cci}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_character_inventory)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_character_inventory))

query5 = 'SELECT * FROM charactercreator_mage;'
mages = sl_curs.execute(query5).fetchall()

# my dictionary for charactercreator_mage table
charactercreator_mage = {}
for mage in mages:
  ccm = {
    'character_ptr_id': mage[0],
    'has_pet' : mage[1],
    'mana' : mage[2]
}
  charactercreator_mage.update({str(mage[0]): ccm}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_mage)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_mage))

query6 = 'SELECT * FROM charactercreator_thief;'
thieves = sl_curs.execute(query6).fetchall()

# my dictionary for charactercreator_thief table
charactercreator_thief = {}
for thief in thieves:
  cct = {
    'character_ptr_id': thief[0],
    'is_sneaking' : thief[1],
    'energy' : thief[2]
}
  charactercreator_thief.update({str(thief[0]): cct}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_thief)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_thief))

query7 = 'SELECT * FROM charactercreator_cleric;'
clerics = sl_curs.execute(query7).fetchall()

# my dictionary for charactercreator_cleric table
charactercreator_cleric = {}
for cleric in clerics:
  ccc = {
    'character_ptr_id': cleric[0],
    'using_shield' : cleric[1],
    'mana' : cleric[2]
}
  charactercreator_cleric.update({str(cleric[0]): ccc}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_cleric)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_cleric))

query8 = 'SELECT * FROM charactercreator_fighter;'
fighters = sl_curs.execute(query8).fetchall()

# my dictionary for charactercreator_cleric table
charactercreator_fighter = {}
for fighter in fighters:
  ccf = {
    'character_ptr_id': fighter[0],
    'using_shield' : fighter[1],
    'rage' : fighter[2]
}
  charactercreator_fighter.update({str(fighter[0]): ccf}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_fighter)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_fighter))

query9 = 'SELECT * FROM charactercreator_necromancer;'
nmcs = sl_curs.execute(query9).fetchall()

# my dictionary for charactercreator_necromancer table
charactercreator_necromancer = {}
for nmc in nmcs:
  ccn = {
    'mage_ptr_id': nmc[0],
    'talisman_charged' : nmc[1]
}
  charactercreator_necromancer.update({str(nmc[0]): ccn}) 

# transfer data to mongoDB
db.test.insert_one(charactercreator_necromancer)

# Confirm that table was added in mongoDB
print(db.test.find(charactercreator_necromancer))
