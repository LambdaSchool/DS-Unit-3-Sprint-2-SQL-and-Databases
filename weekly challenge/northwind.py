import sqlite3 as sql

connect = sql.connect('northwind_small.sqlite')
curs = connect.cursor()

high_price = '''SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;'''
curs.execute(high_price)
curs.fetchall()
# Returns
# id ProductName SupplierId CatergoryId QuantitiyPerUnit UnitPrice UnitsInStock UnitsOnOrder ReorderLevel Discontinued 
# "38"	"Côte de Blaye"	"18"	"1"	"12 - 75 cl bottles"	"263.5"	"17"	"0"	"15"	"0"
# "29"	"Thüringer Rostbratwurst"	"12"	"6"	"50 bags x 30 sausgs."	"123.79"	"0"	"0"	"0"	"1"
# "9"	"Mishi Kobe Niku"	"4"	"6"	"18 - 500 g pkgs."	"97"	"29"	"0"	"0"	"1"
# "20"	"Sir Rodney's Marmalade"	"8"	"3"	"30 gift boxes"	"81"	"40"	"0"	"0"	"0"
# "18"	"Carnarvon Tigers"	"7"	"8"	"16 kg pkg."	"62.5"	"42"	"0"	"0"	"0"
# "59"	"Raclette Courdavault"	"28"	"4"	"5 kg pkg."	"55"	"79"	"0"	"0"	"0"
# "51"	"Manjimup Dried Apples"	"24"	"7"	"50 - 300 g pkgs."	"53"	"20"	"0"	"10"	"0"
# "62"	"Tarte au sucre"	"29"	"3"	"48 pies"	"49.3"	"17"	"0"	"0"	"0"
# "43"	"Ipoh Coffee"	"20"	"1"	"16 - 500 g tins"	"46"	"17"	"10"	"25"	"0"
# "28"	"Rössle Sauerkraut"	"12"	"7"	"25 - 825 g cans"	"45.6"	"26"	"0"	"0"	"1"


avg_age_hired = '''SELECT AVG(HireDate - BirthDate)
    FROM employee'''
# Returns 37.2222222222222


age_hire_city = '''SELECT AVG(HireDate - BirthDate)
    FROM employee
    GROUP BY City'''
# Returns 
# "29.0"
# "32.5"
# "56.0"
# "40.0"
# "40.0"

# # # # # # ################ PART 3 #######################


expense_supplier = '''SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice
    FROM Product 
    JOIN Supplier  ON Supplier.Id = Product.SupplierId
    ORDER BY UnitPrice DESC
    LIMIT 10;'''
# Returns
#  CompanyName  ProductName  UnitPrice
#"Aux joyeux ecclésiastiques"	"Côte de Blaye"	"263.5"
# "Plutzer Lebensmittelgroßmärkte AG"	"Thüringer Rostbratwurst"	"123.79"
# "Tokyo Traders"	"Mishi Kobe Niku"	"97"
# "Specialty Biscuits, Ltd."	"Sir Rodney's Marmalade"	"81"
# "Pavlova, Ltd."	"Carnarvon Tigers"	"62.5"
# "Gai pâturage"	"Raclette Courdavault"	"55"
# "G'day, Mate"	"Manjimup Dried Apples"	"53"
# "Forêts d'érables"	"Tarte au sucre"	"49.3"
# "Leka Trading"	"Ipoh Coffee"	"46"
# "Plutzer Lebensmittelgroßmärkte AG"	"Rössle Sauerkraut"	"45.6"



largest_cat = '''SELECT Category.CategoryName, COUNT(Product.Id) prod_count
    FROM Product 
    JOIN Category ON Category.Id = Product.CategoryId
    GROUP BY Category.CategoryName
    ORDER BY COUNT(Product.Id) DESC
    LIMIT 1;'''
# Returns
#  CategoryName  prod_count
# "Confections"	"13"


top_terr = '''SELECT Territory.TerritoryDescription, COUNT(Employee.Id) as employee_count
    FROM EmployeeTerritory 
    JOIN Territory ON Territory.Id = EmployeeTerritory.TerritoryId
    JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY TerritoryDescription
    ORDER BY COUNT(Employee.Id) DESC
    LIMIT 1;'''
# Returns
#  TerritoryDescription  employee_count
# "New York"	"2"


most_terrs = '''SELECT Employee.Id, Employee.LastName, Employee.FirstName,
    COUNT(DISTINCT EmployeeTerritory.TerritoryId) count_territories
    FROM EmployeeTerritory
    JOIN Employee on Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY Employee.Id
    ORDER BY COUNT(distinct EmployeeTerritory.TerritoryId) DESC
    LIMIT 1;'''
# Returns 
# Id  LastName FirstName count_territories
#"7"	"King"	"Robert"	"10"