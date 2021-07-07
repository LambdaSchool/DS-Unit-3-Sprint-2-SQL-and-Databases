import sqlite3

# Connect to northwind_small database
conn = sqlite3.connect('northwind_small.sqlite3')

# Read through its database to query later on
curs = conn.cursor()

# Save db in result_product
result_10 = curs.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
print('Top 10 expensive items:', result_10)
print('###################################')

result_avg_age = curs.execute('SELECT ROUND(AVG(HireDate - BirthDate), 2) FROM Employee').fetchall()
print('Avg age of employees at hiring date:', result_avg_age[0][0])
print('###################################')

result_city = curs.execute('SELECT City, HireDate, AVG(HireDate - BirthDate) FROM Employee GROUP BY City;').fetchall()
print('Avg age of employees at hiring date by city:', result_city)
print('###################################')

################## PART 3 ########################

# Note to self - when there's a primary key use Join on supplierid DO NOT use p.supplierid = s.supplierid
result_10_supplier = curs.execute('SELECT p.ProductName, s.CompanyName, p.UnitPrice FROM Supplier AS s INNER JOIN Product AS p ON SupplierID ORDER BY UnitPrice DESC LIMIT 10;').fetchall()
print('Top 10 expensive product and their supplier', result_10_supplier)
print('###################################')

result_large_category = curs.execute('SELECT CategoryID,  COUNT(p.ProductName) FROM Category AS c INNER JOIN Product as p ON CategoryID GROUP BY CategoryID ORDER BY COUNT(p.ProductName) DESC LIMIT 1;').fetchall()
print('Largest category,', result_large_category[0][0], ', with number of unique products:', result_large_category[0][1])
print('###################################')

result_territory = curs.execute('SELECT EmployeeID, COUNT(TerritoryDescription) FROM EmployeeTerritory INNER JOIN Territory ON TerritoryID GROUP BY EmployeeID ORDER BY COUNT(TerritoryDescription) DESC LIMIT 1;').fetchall()

print('EmployeeID:,', result_territory[0][0], ', with the most territory:', result_territory[0][1])
########### PART 4 ############

# The type of relationship between employee and territory tables is none. However once you join the table employee territory to either emplyoee or territory then you will get a one to one relationship. You can join a second time on the primary key, EmployeeID.

# Mongo DB is an object based documentation that handles and stores big data. It creates a dictionary where you're given a unique key and its value is a json dictionary(strings are keys and anything type for values) It is not good for querying data compared to sqlite or other querying languages like postgresql.

# NewSQL tries to blend traditional query language to NOSQL languages. Traditional languages follow the ACID principles and NOSQL is lenient on the A,I, and D principle(the C, consistent, is kept). Basically, try to use traditional query langauages on big data.