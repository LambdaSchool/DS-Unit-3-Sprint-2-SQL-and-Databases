import sqlite3

# Part 2
# Creating connection and making sqlite3 file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query to find out top 10 expensive items by unit price
expensive_items = ('''SELECT ProductName, UnitPrice FROM Product
	ORDER BY UnitPrice;''')

print("Top Ten Most Expensive Item:\n",
      curs.execute(expensive_items).fetchall()[-11:-1])

# Query to find out avg age of employees when hired
avg_age = ('''SELECT AVG(HireDate - BirthDate) FROM Employee''')

print("\nAverage Employees Age When Hired:\n",
      curs.execute(avg_age).fetchall()[0][0])

# Stretch Goal How does the average age of employee at hire vary by city?
avg_age_by_city = ('''SELECT AVG(HireDate - BirthDate), City FROM Employee
	GROUP BY City''')

print("\nAverage Employees Age When Hired by City:\n",
      curs.execute(avg_age_by_city).fetchall())

# Part 3
# Query of Top Ten Expensive items and their supplier
exp_supp_items = ('''SELECT p.ProductName, p.UnitPrice, s.CompanyName
	FROM Product as p
	INNER JOIN Supplier as s
	ON p.SupplierID = s.ID
	ORDER BY p.UnitPrice;''')

print("\nTop Ten Expensive Items and Supplier Names:\n",
      curs.execute(exp_supp_items).fetchall()[-11:-1])

# Query to find the top unique category
unique_category = ('''SELECT Count(DISTINCT p.ProductName), c.CategoryName
	FROM Product as p
	INNER JOIN Category as c
	ON p.CategoryID = c.ID
	GROUP BY c.CategoryName
	ORDER BY COUNT(*);''')

print("\nTop Category:\n",
      curs.execute(unique_category).fetchall()[-1])

# Stretch Goal Who's the employee with the most territories? Use TerritoryId
# (not name, region, or other fields) as the unique identifier for territories.
employee_terr = ('''SELECT e.FirstName, COUNT(DISTINCT et.TerritoryID)
	FROM Employee as e
	INNER JOIN EmployeeTerritory as et
	ON e.ID = et.EmployeeID
	GROUP BY e.ID
	ORDER BY COUNT(*);''')

print("\nEmployee with the most territories:\n",
      curs.execute(employee_terr).fetchall()[-1])

curs.close()
conn.commit()
