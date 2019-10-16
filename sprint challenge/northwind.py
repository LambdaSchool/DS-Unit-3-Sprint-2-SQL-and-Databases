"""
Part Two: Sql and Databases Sprint Challenge
"""

import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
def expensive_items():
    curs.execute("""SELECT ProductName, UnitPrice
                    FROM Product
                    ORDER BY UnitPrice DESC
                    LIMIT 10;""")
    return curs.fetchall()

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
def avg_hiring_age():
    curs.execute("""SELECT AVG(HireDate - BirthDate)
                FROM Employee;""")
    return curs.fetchall()

print('The ten most expensive items by price are ', expensive_items())
print('\n')
print('The average age of an employee at time of hire is ', avg_hiring_age())

"""
Part Three: Sql and Databases Sprint Challenge
"""

# What are the ten most expensive items (per unit price) in the database and their suppliers?
def expensive_items_suppliers():
    curs.execute("""SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice
                FROM Product
                JOIN Supplier ON Supplier.ID = Product.SupplierID
                ORDER BY UnitPrice DESC
                LIMIT 10;""")
    return curs.fetchall()

# What is the largest category (by number of products in it)?
def largest_category():
    curs.execute("""SELECT Category.CategoryName, COUNT(Product.ID)
                FROM Product
                JOIN Category ON Category.ID = Product.CategoryID
                GROUP BY Category.CategoryName
                ORDER BY COUNT(Product.ID) DESC
                LIMIT 1;""")
    return curs.fetchall()

print('\n')
print('The ten most expensive items by price and the suppliers are ', expensive_items_suppliers())
print('\n')
print('The largest category and its number of products is ', largest_category())
