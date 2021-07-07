import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query1 = """
SELECT ProductName, UnitPrice FROM Product
         ORDER BY UnitPrice Desc LIMIT 10; """

query2 = """
SELECT AVG(HireDate-BirthDate) AS hire_age FROM Employee; """

query3 = """
SELECT City, AVG(HireDate-BirthDate) AS hire_age FROM Employee
       GROUP BY City; """

query4 = """
SELECT P.ProductName, S.CompanyName, P.UnitPrice 
         FROM Product AS P, Supplier AS S
         WHERE P.SupplierId = S.Id
         ORDER BY P.UnitPrice Desc LIMIT 10; """

query5 = """
SELECT  C.CategoryName, COUNT(DISTINCT P.Id) as PN
         FROM Product AS P, Category AS C
         WHERE P.CategoryId = C.Id
         GROUP BY C.CategoryName
         ORDER BY PN Desc
         LIMIT 1;
         """

#print(curs.execute('SELECT sql FROM sqlite_master WHERE name="Category";').fetchall())
print(curs.execute(query1).fetchall())
print(curs.execute(query2).fetchall())
print(curs.execute(query3).fetchall())
print(curs.execute(query4).fetchall())
print(curs.execute(query5).fetchall())
