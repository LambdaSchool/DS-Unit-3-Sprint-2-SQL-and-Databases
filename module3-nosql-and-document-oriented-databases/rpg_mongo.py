import pymongo
import sqlite3


#connect to Mongo
password = '?'
client = pymongo.MongoClient(
    "mongodb+srv://admin:<password>@cluster0-0ct2c.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


#Create connections and cursors
conn  = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

#Extract RPG data
get_characters = 'SELECT * FROM charactercreator_character'
curs.execute(get_characters)
characters = curs.fetchall()
print(characters[:5])


#Transform data, then insert into Mongo
for char in characters:
    rpg_doc = {
        'sql_key': char[0],
        'name': char[1],
        'level': char[2],
        'exp': char[3],
        'hp': char[4],
        'strength': char[5],
        'intelligence': char[6],
        'dexterity': char[7],
        'wisdom': char[8]
    }
    db.test.insert_one(rpg_doc)


#Create new cursor
curs = db.test.find({})
print(list(curs)[:5])
