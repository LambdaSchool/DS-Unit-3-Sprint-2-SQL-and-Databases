#import sqlite, create and connect to data file
import sqlite3 as sq
conn = sq.connect('northwind_small.sqlite3')
curs = conn.cursor()

#10 most expensive items
def most_exp():
    a = '''
    SELECT ProductName, UnitPrice, SupplierId
    FROM Product
    ORDER BY UnitPrice desc
    LIMIT 10'''
    curs.execute(a)
    return curs.fetchall()
        
most_exp()  

[('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)]

 #Average hire age
def avg_age():
    a1 = '''
    SELECT AVG
    (HireDate - BirthDate)
    FROM Employee
    '''
    curs.execute(a1)
    return curs.fetchall()

avg_age()

[(37.22222222222222,)]

#add supp names to top 10
def sup_name():
    b = """
    SELECT 
    Product.ProductName AS "ProductName", 
    Product.UnitPrice AS Price, 
    Supplier.CompanyName AS "SupplierName"
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
    curs.execute(b)
    return curs.fetchall()

sup_name()

[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 55, 'Gai pâturage'),
 ('Manjimup Dried Apples', 53, "G'day, Mate"),
 ('Tarte au sucre', 49.3, "Forêts d'érables"),
 ('Ipoh Coffee', 46, 'Leka Trading'),
 ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]

def large_cat():
    b1= """
    SELECT CategoryName
    FROM Category
    WHERE Id = (
    SELECT Product.CategoryId
    FROM Product
    GROUP BY Product.CategoryId
    ORDER BY COUNT (Product.ProductName) DESC
    LIMIT 1)
    """
    curs.execute(b1)
    return curs.fetchall()

large_cat()

[('Confections',)]