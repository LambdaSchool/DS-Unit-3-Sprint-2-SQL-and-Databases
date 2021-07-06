import sqlite3

DB = "tiny_db"
TABLE = "tiny_table"
DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

# Connect to the database
tiny = sqlite3.connect('../db/{}.sqlite3'.format(DB))

# Remove the table 
tiny.execute("drop table if exists {}".format(TABLE))

# Create the table 
tiny.execute("create table {}(s varchar(1), x int, y int)".format(TABLE))

# Insert the data
tiny.executemany('insert into {} values (?, ?, ?)'.format(TABLE), DATA)

# Save changes
tiny.commit()

print("Q:", "Count how many rows you have - it should be 3!")
print("A:", tiny.execute("select count(*) from {}".format(TABLE)).fetchall()[0])

print("Q:", "How many rows are there where both x and y are at least 5?")
print("A:", tiny.execute("select count(*) from {} where x >= 5 and y >= 5".format(TABLE)).fetchall()[0])

print("Q:", "How many unique values of y are there?")
print("A:", tiny.execute("select count(distinct  y) from {}".format(TABLE)).fetchall()[0])

