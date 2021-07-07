!pip install psycopg2-binary

import psycopg2
import pandas as pd

dbname = 'stgkilft'
user = 'stgkilft'
password = 'qVKlJkmtimHZ2pzhnnxrcqPzwArwgOqQ'  # Don't commit this!
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

!wget https://raw.githubusercontent.com/bkrant/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv

titanic = pd.read_csv('titanic.csv')

create_titanic_table = """
CREATE TABLE titanic (
  passenger_id SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name VARCHAR(60),
  Sex VARCHAR(6),
  Age FLOAT,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare FLOAT
)
"""

pg_curs.execute(create_titanic_table)

# Let's insert the rest of the characters!
for i in range(1, 25):
  insert_character = """
  INSERT INTO titanic
  VALUES """ + '('+str(titanic.index[i]) + ', ' + str(titanic.iloc[i,:].values.tolist()).split('[')[1].split(']')[0]+')'
  pg_curs.execute(insert_character)
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic;')
pg_titanic = pg_curs.fetchall()

print(len(pg_titanic))

print(pg_titanic[-1])
