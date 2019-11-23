#import sqlite, create and connect to data file
import sqlite3 as sq
conn = sq.connect('demo_data.sqlite3')
curs = conn.cursor()

#Create Table
def dd_create():
    a = '''CREATE TABLE demo(
        s text NOT NULL,
        x integer NOT NULL,
        y integer NOT NULL
    )'''
    curs.execute(a)
    
dd_create()

#Add Data Rows
def dd_insert():
    a1 = '''INSERT INTO demo VALUES 
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)'''
    curs.execute(a1)
    
dd_insert()

#Saving
def dd_save():
    conn.commit()
    
dd_save()

#Count Rows
def row_count():
    a2 = '''
    SELECT COUNT (s)
    FROM demo
    '''
    curs.execute(a2)
    return curs.fetchall()

row_count()

[(3,)]

#Count rows greater than 5
def min_count():
    a3 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE x>=5 and y>=5
    '''
    curs.execute(a3)
    return curs.fetchall()

min_count()

[(2,)]

#Count unique y values
def unique_count():
    a4 = '''
    SELECT COUNT (DISTINCT y)
    FROM demo
    '''
    curs.execute(a4)
    return curs.fetchall()

unique_count()

[(2,)]