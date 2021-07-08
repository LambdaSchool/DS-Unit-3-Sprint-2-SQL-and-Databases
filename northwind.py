#!/usr/bin/env python

import sqlite3

#################################################################
#  Part 2
#################################################################
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()
print(curs.execute("""SELECT name
                    FROM sqlite_master
                    WHERE type='table'
                    ORDER BY name;""").fetchall())

curs.execute("""SELECT Id, ProductName, UnitPrice
                FROM Product
                ORDER BY UnitPrice DESC
                LIMIT 10""")
rows = curs.fetchall()
print("10 most expensive products:")
for row in rows:
    print("  ProductID:", row[0], "ProductName:", row[1], "UnitPrice:", row[2])

curs.execute("""SELECT AVG(HireDate - BirthDate)
                FROM Employee""")
rows = curs.fetchone()
print("Average employee age at hire:", rows[0])

#################################################################
# (Stretch) How does the average age of employee at hire vary by city?
#################################################################

curs.execute("""SELECT City, AVG(HireDate - BirthDate)
                FROM Employee
                GROUP BY City
                ORDER BY AVG(HireDate - BirthDate) DESC""")
rows = curs.fetchall()
print("Average age of employee per city:")
for row in rows:
  print("  City:", row[0] + ",", "Average Age:", row[1])

#################################################################
# Part 3
#################################################################
curs.execute("""SELECT p.Id, ProductName, s.CompanyName, UnitPrice
                FROM Product AS p, Supplier AS s
                WHERE p.SupplierId = s.Id
                ORDER BY UnitPrice DESC
                LIMIT 10""")
rows = curs.fetchall()
print("10 most expensive products with supplier:")
for row in rows:
    print("  ProductID:", row[0], "ProductName:", row[1], "\n",
          "    SupplierName:", row[2], "UnitPrice:", row[3])

curs.execute("""SELECT c.CategoryName, MAX(p.UnitsInStock + p.UnitsOnOrder)
                FROM Product AS p, Category AS c
                WHERE (p.CategoryId = c.Id)
                  AND (p.Discontinued <> 1)""")
row = curs.fetchone()
print("Largest Category:", row[0] + ",", "Number of Units:", row[1])

### New answer, based on Aaron's comment
### Too late - time's up
### curs.execute("""SELECT c.CategoryName, MAX(COUNT(p.Id))
###               FROM Product as p, Category AS c
###               GROUP BY p.CategoryId""")
### row = curs.fetchall()
### print("row:", row)

#################################################################
# (Stretch) Who is the employee with the most territories?
#################################################################

curs.execute("""SELECT FirstName, LastName
                FROM Employee
                WHERE Employee.Id IN (
                  SELECT et.EmployeeId
                  FROM EmployeeTerritory AS et
                  GROUP BY et.EmployeeId
                  ORDER BY COUNT(et.TerritoryId) DESC
                  LIMIT 1)""")
row = curs.fetchone()
print("Employee with most territories:", row[0] + " " + row[1])

