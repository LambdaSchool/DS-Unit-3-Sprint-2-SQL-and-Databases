import psycopg2
import os
from dotenv import load_dotenv


load_dotenv() #> LOADS CONTENTS OF THE .env FILE INTO THE SCRIPTS EVNIRMONT

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)



### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", connection)

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print("CURSOR", cursor)

### An example query
cursor.execute('SELECT * from test_table;')


### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
print(result)