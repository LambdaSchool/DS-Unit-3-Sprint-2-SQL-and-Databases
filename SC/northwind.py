import sqlite3


db_name = "northwind_small.sqlite3"

# connect to the db
conn = sqlite3.connect(db_name)
curs = conn.cursor()

#print(curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall())

#print(curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall())

q2_1 = '''SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10'''
a2_1 = curs.execute(q2_1).fetchall()
print(f'The top 10 most expensive items are {[t[0] for t in a2_1]}\n')

q2_2 = '''SELECT AVG(HireDate - BirthDate) FROM Employee'''
a2_2 = curs.execute(q2_2).fetchall()[0][0]
print(f'The average age of employees at the time of hiring is {a2_2}\n')

q2_3 = '''SELECT City, AVG(HireDate - BirthDate) 
          FROM Employee
          GROUP BY City'''
a2_3 = curs.execute(q2_3).fetchall()
print(f'The average age of employees at the time of hiring is {a2_3}\n')

q3_1 = '''SELECT ProductName, UnitPrice
          FROM (
            SELECT Product.ProductName, OrderDetail.UnitPrice 
                FROM Product
                JOIN OrderDetail
                ON Product.ID = OrderDetail.ProductID 
                GROUP BY Product.UnitPrice, OrderDetail.UnitPrice
          ) 
          ORDER BY UnitPrice DESC LIMIT 10'''
a3_1 = curs.execute(q3_1).fetchall()
print(f'The top 10 most expensive items are {a3_1}\n')

q3_2 = '''SELECT CategoryName, COUNT(Product.ID) 
          FROM Product
          JOIN Category
          ON Category.ID = Product.CategoryID
          GROUP BY Category.ID
          ORDER BY COUNT(Product.ID) DESC LIMIT 1
       '''
a3_2 = curs.execute(q3_2).fetchall()
print(f'The largest category by number of unique products is {a3_2[0][0]} with {a3_2[0][1]} products\n')

q3_3 = '''SELECT FirstName, LastName, COUNT(*)
          FROM Employee
          JOIN EmployeeTerritory
          ON Employee.ID = EmployeeTerritory.EmployeeID
          GROUP BY EmployeeID
          ORDER BY COUNT(*) DESC LIMIT 1
       '''
a3_3 = curs.execute(q3_3).fetchall()
print(f'{a3_3[0][0]} {a3_3[0][1]} has the most territories at {a3_3[0][2]}')

