"""
Part One: Sql and Databases Sprint Challenge
"""

import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create Table
curs.execute("""CREATE TABLE demo
                (s, x, y)""")

# Insert Data
curs.execute("INSERT INTO demo VALUES ('g', 3, 9)")
curs.execute("INSERT INTO demo VALUES ('v', 5, 7)")
curs.execute("INSERT INTO demo VALUES ('f', 8, 7)")

# Save (commit) the changes
conn.commit()

# Count Rows (should be 3)
def row_count():
    curs.execute("""SELECT COUNT(*)
                    FROM demo;""")
    return curs.fetchall()

# How many rows where both 'x' and 'y' are at least 5? (should be 2)
def xy_atleast_5():
    curs.execute("""SELECT COUNT (*) FROM demo
                    WHERE x >= 5
                    AND y >= 5;""")
    return curs.fetchall()

# Unique values of 'y' (should be 2)
def y_unique():
    curs.execute("""SELECT COUNT (DISTINCT y) 
                    FROM demo;""")
    return curs.fetchall()

print('There are ', row_count(), ' rows in the demo table')
print('\n')
print('There are ', xy_atleast_5(), ' rows where both x and y are at least 5 in the demo table')
print('\n')
print('There are ', y_unique(), ' unique y values in the demo table')