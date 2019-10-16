# /usr/bin/env python
" Import rpgdata to MongoDB "

import pymongo

connection_string = 'mongodb://chad_owen:<PASSWORD>@cluster0-shard-00-00-y6wwl.mongodb.net:27017,cluster0-shard-00-01-y6wwl.mongodb.net:27017,cluster0-shard-00-02-y6wwl.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'

client = pymongo.MongoClient(connection_string)
db = client.test 

rpg_testdata = 'INSERT RPGDATA JSON HERE, remove str quotes'

db.test.insert_many(rpg_testdata)