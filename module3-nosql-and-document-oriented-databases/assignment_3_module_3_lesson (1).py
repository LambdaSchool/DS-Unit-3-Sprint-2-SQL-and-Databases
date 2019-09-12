# -*- coding: utf-8 -*-
"""Assignment_3_Module 3 Lesson

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CvCodgKfR_ZfMz0NEUG0seSfAkpykHE4
"""

!curl ipecho.net/plain

username: admin
password: VMmwQoguC5yS6ksa

import sys
print(sys.version)
import sqlite3

!pip install pymongo

import pymongo


client = pymongo.MongoClient("mongodb://admin:VMmwQoguC5yS6ksa@cluster0-shard-00-00-ojcgi.mongodb.net:27017,cluster0-shard-00-01-ojcgi.mongodb.net:27017,cluster0-shard-00-02-ojcgi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db

client.nodes

help(db)

dir(db.test)

help(db.test.insert_one)

db.test.insert_one({'x':1})

db.test.count_documents({'x':1})

db.test.find_one({'x':1})

curs = db.test.find({'x':1})

dir(curs)

list(curs)

jason_doc = {
    'favorite animal': ['Shark', 'Cats']
}

matthew_doc = {
    'favorite animal': 'Platypus'
}

nick_doc = {
    'favorite animal' : 'Hippogriff'
}

db.test.insert_many([jason_doc, matthew_doc, nick_doc])

list(db.test.find())

more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

list(db.test.find({'favorite animal':'Platypus'}))

db.test.update_one({'value':3},
                   {'$inc':{'value':5}})

list(db.test.find())

db.test.update_many({'even': True},
                    {'$inc': {'value': 100}})

list(db.test.find({'even': True}))

db.test.delete_many({'even': False})

list(db.test.find())

rpg_character = (1, 'King Bob', 10, 3, 0, 0, 0)

db.test.insert_one(rpg_character) # throws error because it's a tuple, not a dict

# solution
db.test.insert_one({'rpg_character' : rpg_character})

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'level': rpg_character[2],
    'hp': rpg_character[3]

})

list(db.test.find())

con = sqlite3.connect('/content/rpg_db.sqlite3')
curs = con.cursor()

characters = curs.execute('SELECT * from charactercreator_character;').fetchall()
characters

for character in characters:
    db.test.insert_one({'rpg_character' : character})

list(db.test.find())