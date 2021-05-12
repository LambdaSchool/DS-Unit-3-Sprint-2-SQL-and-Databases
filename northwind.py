#!/usr/bin/env/ python

import sqlite3

sl_conn = sqlite3.connect('../SQLandDatabases/northwind_small.sqlite3')
sl_curs = sl_conn.cursor()

top10_query = """SELECT p.ProductName, p.UnitPrice
FROM Product AS p
ORDER BY p.UnitPrice DESC
LIMIT 10;"""

avg_hiring_age_query = """SELECT AVG(age) FROM (
SELECT Employee.HireDate - Employee.BirthDate AS age
FROM Employee);"""

top10_and_suppliers_query = """SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM Product AS p
INNER JOIN Supplier AS s
ON p.SupplierId = s.Id 
ORDER BY p.UnitPrice DESC
LIMIT 10; """

largest_category_query = """SELECT c.CategoryName, COUNT(p.CategoryId)
FROM Product AS p
INNER JOIN Category AS c
ON p.CategoryID = c.Id 
GROUP BY p.CategoryId
ORDER BY COUNT(p.CategoryId) DESC
LIMIT 1;"""


def query(x):
    print(sl_curs.execute(x).fetchall())