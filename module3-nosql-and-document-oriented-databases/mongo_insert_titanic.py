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

db = client.titanic

df = pd.read_csv('../module2-sql-for-analysis/titanic.csv')

passengers = df.to_dict(orient='records')

collection = db.passengers
collection.insert_many(passengers)
