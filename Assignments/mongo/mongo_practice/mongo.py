import pymongo
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3

load_dotenv() #this will load the env variables

#mongo credentials
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

#connection to mongo db 
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

#databases available
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
#print(dir(client))
print("DB NAMES:", client.list_database_names())

#new database to store our records

db = client.luife_db 
print("----------------")
print("DB:", type(db), db)

#the new table we should use

collection = db.table_rpg 
print("----------------")
print("COLLECTION:", type(collection), collection)

#in this line i will find the rpg database we had to use for the assignment

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

#below we create the connections to our sqlite db

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)


#this is the query to use to select the table we would like to use
character_table_query = ''' 
SELECT * 
FROM charactercreator_character

'''
#here we read the sql file through pandas 
character_table = pd.read_sql(character_table_query,connection)

print(character_table.head(5))


# each variable will represent a column of the pandas dataframe object

char_id = {'id':list(character_table.character_id)}
char_names = {'names':list(character_table.name)}
level = {'lvl':list(character_table.level)}
experience = {'exp':list(character_table.exp)}
hp = {'hp':list(character_table.hp)}
strength = {'str':list(character_table.strength)}

mongo_list = [char_id,char_names,level,experience,hp,strength]

collection.insert_many(mongo_list)
# collection.insert_one(char_names)

curs = collection.find({})
print(list(curs)[:5])