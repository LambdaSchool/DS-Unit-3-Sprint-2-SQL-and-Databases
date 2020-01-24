import pymongo
import sqlite3

client = pymongo.MongoClient(
  "mongodb://ThisIsJorgeLima:<password>@cluster0-shard-00-00-sn2m7.mongodb.net:27017,cluster0-shard-00-01-sn2m7.mongodb.net:27017,cluster0-shard-00-02-sn2m7.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(get_characters).fetchall()
characters[:5]

curs.close()

#302 rows returned 
len(characters)

# for loop from 
for character in characters:
  insert_character = {
    #INSERT INTO charactercreator_character
     'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
  }
    #VALUES """ + str(character[1:]) + ";"
  db.charactercreator_character.insert_one(insert_character)

# for loop is not working...??