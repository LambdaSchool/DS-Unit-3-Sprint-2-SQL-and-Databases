
import pymongo
import sqlite3

# Connecting to MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://admin:UkHGft1qF7I3eLWz@cluster0-4qxo0.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# Retrieving rpg data
conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()

# Gathering all the characters info
characters = curs.execute(
    '''SELECT * FROM charactercreator_character;''').fetchall()

# print(characters)

# For loop to insert all characters with each of their traits
'''for character in characters:
    db.test.insert_one({
        'sql_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': characters[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    })'''

print(list(db.test.find()[0]))
print('Checking if the length is correct with 302 characters:',
      len(list(db.test.find())))

'''
Q: How was working with MongoDB different from working with PostgreSQL?
   What was easier, and what was harder?

A: MongoDb allows you to query data easier/faster in my opinion.
   PostgreSQL has alot more steps to insert data
'''
