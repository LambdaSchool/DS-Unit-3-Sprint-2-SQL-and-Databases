import pymongo
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Setup connection to MongoDB
DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
connection = ('mongodb+srv://Me:' + DB_PASS + 
              '@cluster0.zrrji.mongodb.net/' + DB_NAME +
              '?retryWrites=true&w=majority')

client = pymongo.MongoClient(connection)
db = client.test

# Set up connection to RPG_DB
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

def table_insert(table):
    document = sl_curs.execute(table).fetchall()
    db.test.insert_one({'document': document)

# Get and copy the charactercreator_character table from
# SQLite3 to MongoDB
get_characters = 'SELECT * FROM charactercreator_character;'
table_insert(get_characters)

# Repeat for classes
get_clerics = 'SELECT * FROM charactercreator_cleric;'
table_insert(get_clericss)

get_fighters = 'SELECT * FROM charactercreator_fighter;'
table_insert(get_fighters)

get_mages = 'SELECT * FROM charactercreator_mage;'
table_insert(get_mages)

get_necros = 'SELECT * FROM charactercreator_necromancer;'
table_insert(get_necros)

get_theives = 'SELECT * FROM charactercreator_thief;'
table_insert(get_thieves)

# And again for items, weapons, and inventories
get_invs = 'SELECT * FROM charactercreator_character_inventory;'
table_insert(get_invs)

get_items = 'SELECT * FROM armory_item;'
table_insert(get_items)

get_weapons = 'SELECT * FROM armory_weapon;'
table_insert(get_weapons)

# Commit and close connections
client.close()
sl_curs.close()
sl_conn.close()

##########################################
# How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?

# I think the biggest difference in dealing with MongoDB vs PostgreSQL
# is the fact that MongoDB can handle NOSQL documents while PostgreSQL cannot.
# While it meant that MongoDB could take in more documents, it also meant that
# we had to be much more careful with the structure and schema of our inserts.
# MongoDB was also more secure, so sometimes I would find myself fighting
# security features when I didn't have to in PostgreSQL. Dotenv helped
# with that, but only to an extent.