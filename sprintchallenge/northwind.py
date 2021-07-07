import sqlite3 as sql

# Create connetion to the demo data
myconnection = sql.connect('northwind_small.sqlite3')

mycursor = myconnection.cursor()

ten_most_expensive_pup = mycursor.execute(
    "SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 9;"
).fetchall()
print('---')
print('What are the ten most expensive items (per unit price) in the database? And what are their prices?')
print('---')

for product in ten_most_expensive_pup:
    print(product)

mean_age_of_ee = mycursor.execute("SELECT AVG (BirthDate - HireDate) as avg_age FROM Employee")
print('---')
print('What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)')
print('---')
print(-(mean_age_of_ee.fetchall()[0][0]), 'is the average age!')
print('---')

ten_most_expensive_pup_and_the_supplier = mycursor.execute("""
SELECT UnitPrice, Supplier.Id, ProductName, CompanyName
FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id 
ORDER BY UnitPrice DESC LIMIT 9
""").fetchall()

print('What are the ten most expensive items (per unit price) in the database? And what are their prices?')
print('---')
for product in ten_most_expensive_pup_and_the_supplier:
    print(product)
print('---')

largest_category_by_product = mycursor.execute("""
SELECT CategoryName, Count(Category.Id) as cat_count
FROM Product, Category
WHERE Category.Id = Product.CategoryId
GROUP BY Category.Id 
ORDER BY cat_count DESC;
""")

print('What is the largest category (by number of products in it)?')
print('---')
for product in largest_category_by_product:
    print(product)
print('---')

print('woohooo, I did it!')