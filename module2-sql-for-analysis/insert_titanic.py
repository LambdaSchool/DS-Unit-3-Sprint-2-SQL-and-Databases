import pandas as pd
import numpy as np
import sqlite3
import psycopg2

#Our Connection object :
pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')

#Read in CSV file:
df = pd.read_csv('titanic.csv')

df.head(3)

#Get rid of the ', \, ' ' in names:
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')
df.to_sql("titanic", sl_conn)

#Get rid of the ' and ` in names:
#def clean(x):
    
#    x['Name'] = x['Name'].str.replace("'","`")
#    return x

#Sqlite3 connection + our Cursor:
sq_conn = sqlite3.connect('titanic.sqlite3[]')
sq_curs = sq_conn.cursor()


sl_curs = s1_conn.cursor()

sl_curs.execute('SELECT * FROM titanic').fetchone()

print(sl_curs.execute('PRAGMA table_info(titanic);').fetchall())

# Lets creat our insert_titanic table:
create_insert_titanic = """
CREATE TABLE insert_titanic (
Passenger_ID SERIAL PRIMARY KEY,
Survived INT,
Pclass INT,
Name VARCHAR(85),
Sex gender,
Age FLOAT,
Siblings_Spouses_Aboard INT,
Parents_Children_Aboard INT,
Fare FLOAT
);
"""

pg_curs.execute(create_insert_titanic)

pg_curs.close()
pg_conn.commit();

get_passegners = 'SELECT * FROM titanic'
#Lets save it to a variable:
passengers = sl_curs.execute('SELECT * from titanic;').fetchall()

sl_curs = pg_conn.cursor()

# For loop lets insert all of our data from sqlite3 table into postgres table:
for passenger in passengers:
    insert_passenger = """
        INSERT INTO insert_titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ";"
    pg_curs.execute(insert_passenger)
 
pg_curs.execute('SELECT * from insert_titanic;')
pg_curs.fetchall()

#Lets check our work and make sure our rows match amongst the two tables:
pg_passengers = pg_curs.fetchall()
for passenger, pg_passenger in zip(passengers, pg_passengers):
    assert passenger == pg_character

#Clossing our connections and commit final changes:
pg_curs.close()
pg_conn.commmit()
sq_curs.close()
sq_conn.commit()