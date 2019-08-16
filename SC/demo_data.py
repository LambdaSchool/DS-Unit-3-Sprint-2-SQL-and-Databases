# Part1
import sqlite3

# Creating connection and making sqlite3 file
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Deleting table everytime so code its reproducible
deltable = '''
DROP TABLE IF EXISTS demo;'''
curs.execute(deltable)

# Creating demo table
create_demo_table = """
  CREATE TABLE demo(
  s TEXT,
  x INT,
  y INT
  );
"""

curs.execute(create_demo_table)

# Inserting demo data
insert_data = '''
	INSERT INTO demo(
		s,
		x,
		y)
	VALUES(
		'g', 3, 9),
		('v', 5, 7),
		('f', 8, 7);
		'''

curs.execute(insert_data)

# Query to check the amount of rows in table
count_rows = '''SELECT COUNT(*)
FROM demo;'''

curs.execute(count_rows)
print("Amount of Rows:", curs.fetchall()[0][0])

# Query where bot xand y equal 5
both5 = '''SELECT *
	FROM demo
	WHERE x = 5
	AND y = 5;'''

curs.execute(both5)
print("Amount of Rows where x and y = 5:", curs.fetchall(), 'None')

# Query how many unique values in y column
y_unique = ''' SELECT COUNT(DISTINCT y)
	FROM demo;'''

curs.execute(y_unique)
print("Amount of Unique Values of y:", curs.fetchall()[0][0])

curs.close()
conn.commit()
