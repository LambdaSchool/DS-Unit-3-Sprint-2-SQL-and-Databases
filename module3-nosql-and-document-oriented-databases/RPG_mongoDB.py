

username = user
password = password

import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-tbbec.mongodb.net:27017,cluster0-shard-00-01-tbbec.mongodb.net:27017,cluster0-shard-00-02-tbbec.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

client.nodes

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

query1 = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(query1).fetchall()

# my dictionary for charactercreator_character table
docs = []
for character in characters:
 doc1 = {'table1' : 'charactercreator_character'}
 doc1['character_id'] = character[0]
 doc1['name'] = character[1]
 doc1['level'] = character[2]
 doc1['exp'] = character[3]
 doc1['hp'] = character[4]
 doc1['strength'] = character[5]
 doc1['intelligence'] = character[6]
 doc1['dexterity'] = character[7]
 doc1['wisdom'] = character[8]
 docs.append(doc1)

# transfer data to mongoDB
db.test.insert_many(docs)

# Confirm that table was added in mongoDB
print(db.test.find_one())

query2 = 'SELECT * FROM armory_item;'
items = sl_curs.execute(query2).fetchall()

