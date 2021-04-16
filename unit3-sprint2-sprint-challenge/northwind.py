# querys answers for questions


# part 2 answers

question1_part2 = ("""
--What are the ten most expensive items (per unit price) in the database?:
SELECT UnitPrice, ProductName from Product 
ORDER BY UnitPrice DESC; """)

question2_part2 = ("""
--What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.):
SELECT AVG(Hiredate-Birthdate) AS avg_age FROM Employee;""")

# part 3 answers

question1_part3 = ("""
--What are the ten most expensive items (per unit price) in the database and their suppliers?:
SELECT ProductName,UnitPrice,CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC;""")

question2_part3 = ("""
 --What is the largest category (by number of unique products in it)?:
SELECT count(CategoryName),CategoryName
FROM Product
INNER JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY Count(CategoryName) DESC
LIMIT 1;""")

# part 4 answers
# Q1) In the Northwind database, what is the type of relationship between the Employee and Territory tables?

""" 
Ans)    The relation between the employee and territory tables is that it is a many to many relationship. 
        The tables are connected via the EmployeeTerritory table. A 3 way join would be required to connect 
        the Employee and Territory tables using EmployeeTerritory as an intermedium. 
"""

# Q2) What is a situation where a document store (like MongoDB) is appropriate,
#     and what is a situation where it is not appropriate?

"""
ANS) Mongodb is great for storing unstructured mostly read only data. It also has a lot of flexibility in its
    data structure. Which allows the user to manipulate and explore it freely and decide how structure it for use """

# Q3) What is "NewSQL", and what is it trying to achieve?

"""
ANS) We have SQL and we have NoSQL for database management. NewSQL wants to combine the best parts of these
    2 management systems. The transactional ACID guarantees and the horizontal scalability of NoSQL. """