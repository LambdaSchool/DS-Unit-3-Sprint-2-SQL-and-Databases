#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()
curs.execute("""DROP TABLE demo""")
conn.commit()
curs.execute("""CREATE TABLE demo (s, x, y)""")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)")
conn.commit()

#################################################################
#  Part 1
#################################################################
curs.execute("SELECT COUNT(*) from demo")
num_rows = curs.fetchone()[0]
print("Num rows in table:", num_rows)
curs.execute("""SELECT COUNT(*)
                FROM demo
                WHERE (x > 5) AND (y > 5)""")
num_rows = curs.fetchone()[0]
print("Num rows where x and y are both > 5:", num_rows)
curs.execute("""SELECT COUNT(DISTINCT y)
                FROM demo""")
num = curs.fetchone()[0]
print("Num distinct y values:", num)

