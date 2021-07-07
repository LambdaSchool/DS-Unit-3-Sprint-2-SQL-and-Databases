import sqlite3

###Part 2
print('###Part 2:\n')

#Open a connection to northwind_small.sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Put the questions and quesries into lists:
questions = ['Q1: What are the ten most expensive items (per unit price) in the database?',
        	 'Q2: What is the average age of an employee at the time of their hiring?',
			 'Q3: (*Stretch*) How does the average age of employee at hire vary by city?']

queries = ["SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;",
		   "SELECT ROUND(AVG(HireDate - BirthDate),1) AS Avg_Age FROM Employee;",
		   "SELECT CITY, AVG(HireDate - BirthDate) AS Avg_Age FROM Employee GROUP BY CITY;"]

#Iterate and execute the queries and print the questions and results:
for i in range(len(questions)):
	print(questions[i])
	curs.execute(queries[i])
	results = curs.fetchall()
	if len(results) == 1:
		print(results)
	else:
		for res in results:
			print(res)
	print('\n')

### Part 3 - Sailing the Northwind Seas
print('###Part 3:\n')

questions = ['Q1: What are the ten most expensive items (per unit price) in the database *and* their suppliers?',
			 'Q2: What is the largest category (by number of unique products in it)?',
			 "Q3: (*Stretch*) Who's the employee with the most territories?"]

queries = ["SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName AS Supplier FROM Product, Supplier WHERE Product.SupplierID = Supplier.ID ORDER BY UnitPrice DESC LIMIT 10;",
		   "SELECT Category.CategoryName, COUNT(*) FROM Product, Category WHERE Product.CategoryID = Category.ID GROUP BY Product.CategoryID ORDER BY COUNT(*) DESC LIMIT 1;",
		   "SELECT Employee.FirstName, Employee.LastName, COUNT(*) FROM Employee, EmployeeTerritory WHERE EmployeeTerritory.EmployeeID = Employee.ID GROUP BY Employee.ID ORDER BY COUNT(*) DESC LIMIT 1;"]

#Iterate and execute the queries and print the questions and results:
for i in range(len(questions)):
	print(questions[i])
	curs.execute(queries[i])
	results = curs.fetchall()
	if len(results) == 1:
		print(results)
	else:
		for res in results:
			print(res)
	print('\n')

### Part 4 - Questions (and your Answers)
print('###Part 4:\n')

questions = ['Q1: In the Northwind database, what is the type of relationship between the `Employee` & `Territory` tables?',
			 '''Q2: What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where 
it is not appropriate?''',
			 'Q3: What is "NewSQL", and what is it trying to achieve?']

answers = ['A1: The employee to Territory relationship is "one-to-many".',
		   '''A2: A document store such as MongoDB is appropriate for storing large amounts of documents(data), usually 
unstructured or semi-structured. It is a non-relational database paradigm consisting of key-value pairs like JSON files 
or python dictionaries. The data can be broken into subsets and stored across multiple servers (generally someone else's 
machines). Basically, if the amount of data is extremely large, and a organized schema is not necessary, NoSQL paradigm is 
probably the way to go. However, in a situation where a relational approach is a necessity, such as with banking, the 
reliability of SQL is probably more important than the scalability of document oriented databases.''',
		   '''A3: NewSQL is a hybrid approach that seeks to combine the best of both types of database systems, namely by combining 
the transactional and consistency requirements of SQL with the scalability of NoSQL.''']

for i in range(len(questions)):
	print(questions[i])
	print(answers[i])
	print('\n')