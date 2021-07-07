#!/usr/bin/env python

# imports
import sqlite3

# establish connection and cursor
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
query_1 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

curs.execute(query_1).fetchall()

# What is the average age of an employee at the time of their hiring? 
query_2 = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""

curs.execute(query_2).fetchall()

# How does the average age of employee at hire vary by city?
query_3 = """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
"""

curs.execute(query_3).fetchall()

# What are the ten most expensive items (per unit price) in the database 
# and their suppliers?
query_4 = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

curs.execute(query_4).fetchall()

# What is the largest category (by number of products in it)?

query_5 = """
SELECT Category.CategoryName, COUNT(Product.ProductName)
FROM Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY Product.CategoryId
ORDER BY COUNT(Product.ProductName) DESC
LIMIT 1
"""

curs.execute(query_5).fetchall()

# Who's the employee with the most territories?
query_6 = """
SELECT Employee.FirstName, Employee.LastName, COUNT(EmployeeTerritory.EmployeeId) 
FROM Employee, EmployeeTerritory
Where Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY Employee.Id
ORDER BY COUNT(EmployeeTerritory.EmployeeId) DESC
LIMIT 1
"""

curs.execute(query_6).fetchall()