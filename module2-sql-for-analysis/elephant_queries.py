import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import json 

# my test_table was loaded in via the sql editor on table + 

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
cur = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS test_table (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""


### An example query
cur.execute('SELECT * from test_table;')


### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchone()
print(result)


### insertion query 
###insertion_query = """
###INSERT INTO test_table (name, data) VALUES    
###(     
###    'A row name',     
###    null      
###),    
###(     
###    'Another row, with JSON',     
###    '{"a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB    
###);    
###"""   
### Insertion query 2 
###insertion_query = f"INSERT INTO {table_name} (name, data) VALUES %s"
###execute_values(cursor, insertion_query, [
###  ('A rowwwww', 'null'),
###  ('Another row, with JSONNNNN', json.dumps(my_dict)),
###  ('Third row', "3")
###])

my_dict={"a": 1, "b": ["dog", "cat", 42], "c": 'true' }
# Object oriented approach for insertion, must be in tuples. 
insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cur, insertion_query, [
    ('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict)),
    ('Third row', "3")
])


titanic_df = pd.read_csv('https://raw.githubusercontent.com/timrocar/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')


tuple_list = [] 
tuple_list = [list(row) for row in titanic_df.itertuples(index=False)]


CREATE_TABLE = """ 
    DROP TABLE IF EXISTS titanic_passengers;
    CREATE TABLE titanic_passengers (
        Survived int,
        Pclass int,
        Name varchar(100),
        Sex varchar(100),
        Age float,
        Siblings_Spouses_Aboard int,
        Parents_Children_Aboard int,
        Fare float
    );"""


cur.execute(CREATE_TABLE)


insertion_query = """
INSERT INTO titanic_passengers (
    Survived, Pclass, Name,  Sex, 
    Age, Siblings_Spouses_Aboard, 
    Parents_Children_Aboard, Fare) VALUES %s
"""
execute_values(cur, insertion_query, tuple_list)



conn.commit()

cur.close()
conn.close()