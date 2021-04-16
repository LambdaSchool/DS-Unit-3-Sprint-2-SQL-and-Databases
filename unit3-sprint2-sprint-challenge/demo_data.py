import sqlite3

create_demo_table = """
    CREATE TABLE demo(
        s VARCHAR(1),
        x INT,
        y INT
    ); 
"""

#make connection and cursor
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_curs = sl_conn.cursor()
#make the table
sl_curs.execute(create_demo_table)
#insert data to table
sl_curs.execute("INSERT INTO demo (s,x,y) Values ('g',3,9);")
sl_curs.execute("INSERT INTO demo (s,x,y) Values ('v',5,7);")
sl_curs.execute("INSERT INTO demo (s,x,y) Values ('f',8,7);")
#commit work
sl_curs.close()
sl_conn.commit()
#reopen connection
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_curs = sl_conn.cursor()
#run commands
sl_curs.execute('SELECT * FROM demo;').fetchall()
sl_curs.execute(count_query).fetchall()
sl_curs.execute(query2).fetchall()
sl_curs.execute(query3).fetchall()