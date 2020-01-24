import pandas as pd
import numpy as np
import sqlite3
import psycopg2

!pip install psycopg2-binary

df = pd.read_csv('https://raw.githubusercontent.com/EvidenceN/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
df.head()

# In case we have issues with spaces and /:
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')
# Lets get rid of the ' in some of the names
df.Name = df.Name.str.replace("'", " ")
# The longest name in Name column for table creation:
df.Name.map(lambda x: len(x)).max()

sq_conn = sqlite3.connect('titanic.sqlite3')
sq_curs = sq_conn.cursor()

#Database elephantSQL acct. info:

#Our Connection object :
pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Create en# type for Sex
query1 = "CREATE TYPE gender AS ENUM ('male', 'female');"
pg_curs.execute(query1)

# Remember when creating your table add in 
# PRIMARY KEY on first insert.
#Create insert_titanic table:
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
# Lets now exexute this:
pg_curs.execute(create_insert_titanic)

passengers = sq_curs.execute('SELECT * from insert_titanic;').fetchall()

# Lets work on our for loop now and insert our data from sqlite3
# into our postgres table:
for passenger in passengers:
    insert_passenger = """
        INSERT INTO insert_titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ";"
    pg_curs.execute(insert_passenger)

pg_curs.execute('SELECT * from insert_titanic;')
pg_curs.fetchall()

# Make sure rows match between 2 tables:
pg_passengers = pg_curs.fetchall()
for passenger, pg_passenger in zip(passengers, pg_passengers):
    assert passengers == pg_character

# Close connections and commit changes:
pg_curs.close()
pg_conn.commit()
sq_curs.close()
sq_conn.commit()
