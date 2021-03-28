import sqlite3


#Create connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

#Create table
create_table = """
CREATE TABLE demo (
    s VARCHAR (10),
    x INT,
    y INT
);
"""
#curs.execute(create_table)
#conn.commit()  Only Once

#Insert data into table
demo_insert = """
    INSERT INTO demo (s, x, y) 
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
#curs.execute(demo_insert)
#conn.commit()  Only Once


#Count how many rows you have
curs.execute('SELECT COUNT(*) FROM demo')
answer = curs.fetchall()[0][0]
print(f'There are {answer} rows.\n')


#How many rows are there where both 'x' and 'y' are at least 5?
curs.execute("""
    SELECT COUNT(*) 
    FROM demo
    WHERE x >= 5 
    AND y >= 5;
""")
answer = curs.fetchall()[0][0]
print(f'There are {answer} rows with values of at least 5.\n')


#How many unique values of y are there?
curs.execute("""
    SELECT COUNT(DISTINCT y) 
    FROM demo;
""")
answer = curs.fetchall()[0][0]
print(f'There are {answer} unique values of y.')


#Close connection and commit
curs.close()
conn.commit()