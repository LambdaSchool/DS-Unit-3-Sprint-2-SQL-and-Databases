# ./usr/bin/env python
"""
Sample output (for reference):

Item                      Price
-------------------------------
Côte de Blaye            $ 263.5
Thüringer Rostbratwurst  $ 123.79
Mishi Kobe Niku          $ 97
Sir Rodney's Marmalade   $ 81
Carnarvon Tigers         $ 62.5
Raclette Courdavault     $ 55
Manjimup Dried Apples    $ 53
Tarte au sucre           $ 49.3
Ipoh Coffee              $ 46
Rössle Sauerkraut        $ 45.6

Most Expensive items
Average age at hiring time: 37.22

City           Age at hire (avg)
--------------------------------
Kirkland             29.0
London               32.5
Redmond              56.0
Seattle              40.0
Tacoma               40.0

Item                      Price     Supplier
--------------------------------------------
Côte de Blaye            $ 263.5    Aux joyeux ecclésiastiques
Thüringer Rostbratwurst  $ 123.79   Plutzer Lebensmittelgroßmärkte AG
Mishi Kobe Niku          $ 97       Tokyo Traders
Sir Rodney's Marmalade   $ 81       Specialty Biscuits, Ltd.
Carnarvon Tigers         $ 62.5     Pavlova, Ltd.
Raclette Courdavault     $ 55       Gai pâturage
Manjimup Dried Apples    $ 53       G'day, Mate
Tarte au sucre           $ 49.3     Forêts d'érables
Ipoh Coffee              $ 46       Leka Trading
Rössle Sauerkraut        $ 45.6     Plutzer Lebensmittelgroßmärkte AG

Largest category: Confections

Robert King has the most territories: 49

"""
import sqlite3

# Create new database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

### Part 2 - The Northwind Database
# ---------------------------------

# What are the ten most expensive items (per unit price) in the database?
curs.execute("""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
""")
print()
print('Item                      Price')
print('-------------------------------')
for x in curs.fetchall():
    print(f'{x[0]:24} $ {x[1]}')

# What is the average age of an employee at the time of their hiring?
curs.execute("""
SELECT AVG(HireDate - BirthDate)
FROM Employee
""")
age = curs.fetchall()[0][0]
print()
print('Most Expensive items')
print(f'Average age at hiring time: {age:.2f}')

# How does the average age of employee at hire vary by city?
curs.execute("""
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
""")
print()
print('City           Age at hire (avg)')
print('--------------------------------')
for x in curs.fetchall():
    print(f'{x[0]:20} {x[1]}')


### Part 3 - Sailing the Northwind Seas
# -------------------------------------

# What are the ten most expensive items (per unit price) 
# in the database and their suppliers?
curs.execute("""
SELECT 
    Product.ProductName AS "Product Name", 
    Product.UnitPrice AS Price, 
    Supplier.CompanyName AS "Supplier Name"
FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
""")
print()
print('Item                      Price     Supplier')
print('--------------------------------------------')
for x in curs.fetchall():
    print(f'{x[0]:24} $ {x[1]:<6}   {x[2]}')


# What is the largest category (by number of products in it)?
curs.execute("""
SELECT CategoryName
FROM Category
WHERE Id = 
        (
        SELECT 
                Product.CategoryId
        FROM Product
        GROUP BY Product.CategoryId
        ORDER BY COUNT (Product.ProductName) DESC
        LIMIT 1
        )
""")
print()
print(f'Largest category: {curs.fetchall()[0][0]}')


# Who's the employee with the most territories?
curs.execute("""
SELECT 
        FirstName, LastName,
        COUNT (TerritoryId) AS "Number of territories"
FROM Employee, EmployeeTerritory
WHERE Employee.Id = 
        (
        SELECT 
                EmployeeId
        FROM EmployeeTerritory
        GROUP BY EmployeeId
        ORDER BY COUNT (TerritoryId) DESC
        LIMIT 1
        )
""")
x = curs.fetchall()
print()
print(f'{x[0][0]} {x[0][1]} has the most territories: {x[0][2]}')