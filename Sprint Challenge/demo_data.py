

import sqlite3

#Get a cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor

create_table = """ 
CREATE TABLE  demo (
    s varchar(10),
    x int,
    y int
);"""

curs.execute(create_table)
conn.commit()

# Write INSERT INTO statements
curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'g'", 3, 9)
    ;""")

curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'v'", 5, 7)
    ;""")

curs.execute("""
INSERT INTO demo(
    s,x,y) VALUES("'f'", 8, 7)
    ;""")

conn.commit()

# Count how many rows you have
row_count = """SELECT COUNT(*)
FROM demo;"""

# How many rows are there where both x and y are >= 5
at_least_five = """SELECT COUNT(*)
FROM demo
WHERE demo.x >= 5 AND demo.y >= 5;"""

# How many unique values of y are there
unique_y = """ SELECT COUNT(DISTINCT(demo.y))
FROM demo;"""

def part_one(x):
    print(curs.execute(x).fetchall())
