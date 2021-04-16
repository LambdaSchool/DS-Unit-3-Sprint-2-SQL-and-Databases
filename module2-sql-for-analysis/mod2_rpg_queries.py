import os
from dotenv import load_dotenv
import psycopg2
import sqlite3
from psycopg2.extras import execute_values


#conn = sqlite3.connect('rpg_db.sqlite3')
#curs = conn.cursor()
#armory_query = 'SELECT * FROM armory_item;'
#curs.execute(armory_query)
#armory_tuples = curs.fetchone()



load_dotenv() #loads contents of the new.env file into the script's env

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)


### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
curs = conn.cursor()




#saving transactions
conn.commit()

curs.close()
conn.close()