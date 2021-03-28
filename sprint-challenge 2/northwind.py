import sqlite3


#Open connection and cursor
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


#What are the ten most expensive items (per unit price) in the database?
curs.execute("""
    SELECT ProductName, UnitPrice 
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
answer = curs.fetchall()
print(f'The ten most expensive items are: \n{answer}\n')


#What is the average age of an employee at the time of their hiring?
curs.execute("""
    SELECT SUM(HireDate - BirthDate) / COUNT(*)
    FROM Employee;
""")
answer = curs.fetchall()[0][0]
print(f'The average hiring age is {answer}.\n')


#Ten most expensive products and their suppliers
curs.execute("""
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product AS p
    LEFT JOIN Supplier AS s
    ON p.ID = s.ID
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
answer = curs.fetchall()
print(f'The ten most expensive products and their suppliers are: \n{answer}\n')


#What is the largest category by number of unique products?
curs.execute("""
    SELECT COUNT(CategoryId), CategoryName
    FROM Product AS p
    INNER JOIN Category As c
    ON p.CategoryId = c.Id
    GROUP By CategoryName
    ORDER By COUNT(CategoryId) DESC;
""")
answer = curs.fetchall()[0][1]
print(f'The largest category by unique products is {answer}\n')


# Close connect and commit
curs.close()
conn.commit()