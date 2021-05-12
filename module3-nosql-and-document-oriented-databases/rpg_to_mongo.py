#!/usr/bin/env/ python

# MongoDB was easier to connect the data. 
# Converting sqlite3 to dict was fairly easy to find
# However it just makes more sense intuituvely when moving
# sqlite3 to PostgreSQL


import sqlite3
import pymongo

# Get the data from sqlite3
sl_conn = sqlite3.connect('../joshdsolis/rpg_db.sqlite3')
results = sl_conn.execute('SELECT * FROM charactercreator_character;').fetchall()

# Data to dict form
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

sl_conn.row_factory = dict_factory
curs = sl_conn.cursor()
curs.execute
results = sl_conn.execute('SELECT * FROM charactercreator_character;').fetchall()

# Connecting to MongoDB
connection_string = "mongodb://UserJosh:<TODO>@cluster0-shard-00-00-5wkdx.mongodb.net:27017,cluster0-shard-00-01-5wkdx.mongodb.net:27017,cluster0-shard-00-02-5wkdx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
client = pymongo.MongoClient(connection_string)
db = client.test

for result in results:
    db.test.insert_one(result)

print(list(db.test.find()))