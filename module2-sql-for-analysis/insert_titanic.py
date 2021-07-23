import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

########## Connect to PostGRES ##########

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

########## Create Titanic SQL Table ##########

create_titanic_table = '''
    CREATE TABLE IF NOT EXISTS titanic (
        pass_id SERIAL PRIMARY KEY,
        survived INT,
        pclass INT,
        name VARCHAR(200),
        sex VARCHAR(20),
        age INT,
        siblings_spouses INT,
        parents_children INT,
        fare NUMERIC(30)
    )
'''

cursor.execute(create_titanic_table)
conn.commit()

##########  Read in CSV and populate Titanic Table ##########

titanic_db = pd.read_csv('titanic.csv')
titanic_db['Name'] = titanic_db['Name'].apply(lambda x: x.replace("'",""))

data = list(titanic_db.to_records())

for item in data:

    insert_query = f''' INSERT INTO titanic 
        (pass_id, survived, pclass, name, sex, age, siblings_spouses,
        parents_children, fare) VALUES {item}
    '''

    cursor.execute(insert_query)

conn.commit()

# test edit for push