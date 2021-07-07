import sqlite3

###Part 1:

#Open a connection to a new (blank) database file `demo_data.sqlite3`
conn = sqlite3.connect('demo_data.sqlite')

curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS demo")

#crete the demo table
create_demo_table = """
	CREATE TABLE demo (
		s PRIMARY KEY,
		x INT,
		y INT
	)
"""

#execute the table creation 
curs.execute(create_demo_table)

#generate the data to insert into the table
row_tuples = [('g', 3, 9),
              ('v', 5, 7),
              ('f', 8, 7)]

#iterate over each row in the tuples list and insert them into the titanic table:
for row in row_tuples:
	insert_row = "INSERT INTO demo VALUES" + str(row)
	curs.execute(insert_row)

#Commit to save the data
conn.commit()

#Make lists of the questions and corresponding queries:
questions = ['Q1: Count how many rows you have - it should be 3!',
             'Q2: How many rows are there where both `x` and `y` are at least 5?',
             'Q3: How many unique values of `y` are there?']

queries = ["SELECT COUNT(*) FROM demo;",
           "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;",
           "SELECT COUNT(DISTINCT y) FROM demo;"]

#iterate over and print each question, execute the corresponding query, print the result:
for i in range(len(questions)):
	print(questions[i])
	curs.execute(queries[i])
	print(curs.fetchall()[0][0])
	print('\n')
