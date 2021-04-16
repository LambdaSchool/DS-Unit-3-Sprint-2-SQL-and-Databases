import os
from dotenv import load_dotenv
import psycopg2

import pandas as  pd

#here we will make a new connection

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

titanic = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'

df = pd.DataFrame(titanic)

sql_titanic = df.to_sql(name='sql_titanic')
