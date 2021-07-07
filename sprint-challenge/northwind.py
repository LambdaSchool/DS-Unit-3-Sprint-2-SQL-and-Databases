import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")


# Part 2

# Queries
nw_qs = [
    "What are the ten most expensive items (per unit price) in the database?",
    "What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)",
    "(Stretch) How does the average age of employee at hire vary by city?",
]

nw_as = [
    """SELECT ProductName, UnitPrice 
FROM Product 
ORDER BY UnitPrice DESC
LIMIT 10;""",
    """
SELECT AVG(HireDate - BirthDate)
FROM Employee;
""",
    """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City;
""",
]

# answer queries:
print("Part 2")
for q, a in zip(nw_qs, nw_as):

    # print questions
    print("Question ", nw_qs.index(q) + 1)
    print(q)

    # print query
    print("SQL query :")
    print(a)

    # create a connection object and execute query
    curs = conn.cursor()
    curs.execute(a)
    output = curs.fetchall()

    print("Output: ")
    print(output, "\n")

    # close cursor
    curs.close()

# Part 3

# Queries
nw_qs = [
    "What are the ten most expensive items (per unit price) in the database and their suppliers?",
    "What is the largest category (by number of unique products in it)?",
    "(Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.",
]

nw_as = [
    """
SELECT ProductName, 
UnitPrice, CompanyName 
FROM Product
INNER JOIN Supplier ON Supplier.ID = Product.SupplierId
ORDER BY UnitPrice DESC
LIMIT 10;
""",
    """
SELECT COUNT(DISTINCT Product.Id) as NumID, Category.CategoryName
FROM Product
LEFT JOIN Category ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY NumID DESC
LIMIT 1;
""",
    """
SELECT COUNT (DISTINCT EmployeeTerritory.TerritoryId) AS Ters, Employee.FirstName, Employee.LastName, Employee.Id
FROM Employee
LEFT JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY Employee.Id
ORDER BY Ters DESC
LIMIT 1;
""",
]

# answer queries:
print("Part 3")
for q, a in zip(nw_qs, nw_as):

    # print questions
    print("Question ", nw_qs.index(q) + 1)
    print(q)

    # print query
    print("SQL query :")
    print(a)

    # create a connection object and execute query
    curs = conn.cursor()
    curs.execute(a)
    output = curs.fetchall()

    print("Output: ")
    print(output, "\n")

    # close cursor
    curs.close()


# # close any open cursors and connection
curs.close()
conn.close()
