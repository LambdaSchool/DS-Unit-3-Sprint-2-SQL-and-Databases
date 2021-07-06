import sqlite3 as sql

connect = sql.connect('demo_data.sqlite')
curs = connect.cursor()

add_table = '''CREATE TABLE demo (
    s str,
    x int,
    y int
);'''
curs.execute(add_table)
connect.commit()

a_data = '''INSERT INTO demo(s,x,y)
    VALUES('g','3','9');'''

b_data = '''INSERT INTO demo(s,x,y)
    VALUES('v','5','7');'''

c_data = '''INSERT INTO demo(s,x,y)
    VALUES('f','8','7');'''

curs.execute(a_data)
curs.execute(b_data)
curs.execute(c_data)
connect.commit()

count_rows = '''SELECT COUNT(s)
    FROM demo;'''
curs.execute(count_rows)
curs.fetchall()
# Returns 3
xy_over5 = '''SELECT COUNT(s)
    FROM demo
    WHERE x>=5 and y>=5;'''
curs.execute(xy_over5)
curs.fetchall()
# Returns 2

unique_y = '''SELECT COUNT(DISTINCT y)
    FROM demo;'''
curs.execute(unique_y)
curs.fetchall()
# Returns 2