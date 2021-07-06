import sqlite3

DB = '../db/northwind_small.sqlite3'

northwind = sqlite3.connect(DB)

# Part 2
print("Q:", "What are the ten most expensive items (per unit price) in the database?")
print("A:", northwind.execute("select UnitPrice from Product order by UnitPrice desc limit 10").fetchall())

print("Q:", "What is the average age of an employee at the time of their hiring?")
print("A:", northwind.execute("select avg(HireDate - BirthDate) from Employee").fetchall())

print("Q:", "How does the average age of employee at hire vary by city?")
print("A:", northwind.execute("select avg(HireDate - BirthDate), City from Employee group by City").fetchall())

# Part 3
top_ten_unit_price_query = ( 
    """
    select
        o.UnitPrice,
        p.UnitPrice
    from
        (select UnitPrice from OrderDetail order by UnitPrice desc) o,
        (select UnitPrice from Product order by UnitPrice desc) p
    limit 10
    """
)

print("Q:", "What are the ten most expensive items (per unit price) in the database and their suppliers?")
print("A:", northwind.execute(top_ten_unit_price_query).fetchall())

largest_product_category_query = (
    """
    select 
        Category.CategoryName, count(distinct Product.Id) as Count
    from 
        Category
    inner join
        Product
    on
        Product.CategoryId = Category.Id
    group by
        Category.CategoryName
    order by
        Count desc
    limit 1
    """
)

print("Q:", "What is the largest category (by number of unique products in it)?")
print("A:", northwind.execute(largest_product_category_query).fetchall())

employee_with_most_territories_query = (
    """
    select 
        e.EmployeeId, 
        count(distinct t.Id) as TerritoryCount
    from 
        EmployeeTerritory e
    inner join
        Territory t
    on 
        e.TerritoryId = t.Id
    group by
        e.EmployeeId
    order by
        TerritoryCount desc
    limit 1
    """
)

print("Q:", "Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.")
print("A:", northwind.execute(employee_with_most_territories_query).fetchall())
