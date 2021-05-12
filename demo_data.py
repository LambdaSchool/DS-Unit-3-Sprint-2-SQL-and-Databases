#!/usr/bin/env/ python


import sqlite3


sl_conn = sqlite3.connect('../SQLandDatabases/demo_data.sqlite3')

create_table = """ CREATE TABLE demo (
    s varchar(30),
    x int,
    y int
); """

sl_curs = sl_conn.cursor()
sl_curs.execute(create_table)
sl_curs.execute(""" INSERT INTO demo (
    s, x, y) VALUES ("'g'", 3, 9)
;""")

sl_curs.execute(""" INSERT INTO demo (
    s, x, y) VALUES ("'v'", 5, 7)
;""")

sl_curs.execute(""" INSERT INTO demo (
    s, x, y) VALUES ("'f'", 8, 7)
;""")

sl_conn.commit()

rows_count_query = """SELECT COUNT(*)
FROM demo;"""

greater_than_5_query = """SELECT COUNT(*)
FROM demo
WHERE demo.x >= 5
AND demo.y >= 5;"""

unique_y_query = """SELECT COUNT(DISTINCT(demo.y))
FROM demo;"""

def query(x):
    print(sl_curs.execute(x).fetchall())