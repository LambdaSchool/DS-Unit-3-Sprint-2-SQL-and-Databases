# My experience with mongodb vs postgres definitely left me with the impression
# that the flexibility of mongodb makes it a lot faster and simpler to
# implement, at the cost of ease and complexity of querying

import pymongo
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

client = pymongo.MongoClient(
    f'mongodb+srv://{DB_USER}:{DB_PASS}'
    f'@lambda-qip5e.mongodb.net/test?retryWrites=true&w=majority')

db = client.rpg

df = pd.read_json('testdata.json')

for model in df['model'].unique():
    data = df[df['model'] == model]
    data_as_list = data['fields'].tolist()
    collection = db[f'{model}']
    collection.insert_many(data_as_list)
