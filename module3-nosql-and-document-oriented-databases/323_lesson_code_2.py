# -*- coding: utf-8 -*-
"""
LS_DS8_323_MongoDB :: Code from the live lesson.
"""

import pymongo

client = pymongo.MongoClient(
    "mongodb://admin:tUCTyeW6qy3oWqEa@cluster0-shard-00-00-tjf42.mongodb.net:27017,cluster0-shard-00-01-tjf42.mongodb.net:27017,cluster0-shard-00-02-tjf42.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
)
db = client.test

db

# check how many machines are working
client.nodes

help(db)

dir(db.test)

help(db.test.insert_one)

# Count how many documents
db.test.count_documents({"x": 1})

# Insert a document
db.test.insert_one({"x": 1})

# Do the count again
db.test.count_documents({"x": 1})

db.test.find_one({"x": 1})

db.test.find({"x": 1})

curs = db.test.find({"x": 1})

dir(curs)

list(curs)

samantha_doc = {"favorite animal": ["Kokopo", "Dog"]}

rosie_doc = {"favorite animal": "Snakes", "favorite color": "Cyan"}

amer_doc = {"favorite animal": "Red Panda"}

db.test.insert_many([samantha_doc, rosie_doc, amer_doc])

list(db.test.find())

# Let's make more documents
more_docs = []
for i in range(10):
    doc = {"even": i % 2 == 0}
    doc["value"] = i
    more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({"even": False}))

list(db.test.find({"favorite animal": "Red Panda"}))

help(db.test.update_one)

db.test.update_one({"value": 3}, {"$inc": {"value": 5}})

list(db.test.find())

db.test.update_many({"even": True}, {"$inc": {"value": 100}})

list(db.test.find({"even": True}))

db.test.delete_many({"even": False})

list(db.test.find())

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

# Wrap this in a simple dictionary so that the insert_one method works
db.test.insert_one({"rpg_character": rpg_character})

list(db.test.find())

db.test.insert_one(
    {
        "sql_id": rpg_character[0],
        "name": rpg_character[1],
        "hp": rpg_character[2],
        "level": rpg_character[3],
    }
)

