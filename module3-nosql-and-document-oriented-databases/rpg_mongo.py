import pymongo

client = pymongo.MongoClient('''mongodb://dakotapope:passwrd@
cluster0-shard-00-00-iaoct.mongodb.net:27017,cluster0-shard-00
-01-iaoct.mongodb.net:27017,cluster0-shard-00-02-iaoct.mongodb.
net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=
admin&retryWrites=true''')
# investigate the databases already initialized
client.database_names()
# -->['rpg_data', 'test', 'admin', 'local']

# since I created the table on the Mongo Atlas dashboard I wil use it here
rpgs = client.rpg_data.rpg

# loadout the json file to prep for dumping into a mongo db table

with open('''C:/Users/dakot/Documents/GitHub/DS-Unit-3-Sprint-2-SQL-and-
Databases/module3-nosql-and-document-oriented-databases/rpg.json''') as f:
    file_data = json.load(f)

# make a space for the data to go
rpg_table = rpg['rpg_data']

# Dump the json data into the mongodb cloud.
rpg_table.insert_many(file_data)
# <pymongo.results.InsertManyResult at 0x2c80a7c8688>
# And DONE!
