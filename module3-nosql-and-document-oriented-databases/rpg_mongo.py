# ./usr/bin/env python
" Importing from JSON to MongoDB"

from dotenv import load_dotenv
import os
import pymongo
import requests
load_dotenv()
MongoDB_URL = os.getenv("MongoDB_URL")
rpg_URL = 'https://raw.githubusercontent.com/\
    LambdaSchool/Django-RPG/master/testdata.json'

client = pymongo.MongoClient(MongoDB_URL)
database = client.rpg_database
collection = database.rpg_collection
response = requests.get(rpg_URL)
data = response.json()

result = collection.insert_many(data)

# The main difference I experienced between MongoDB and
# SQL is that in SQL I could visualize the data in actual
# tables, the way that I'm used to seeing it.  The relations
# between datapoints on different tables are much clearer,
# which I guess is what I'd expect of relational databases.
