# Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

### In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?

I believe that the `Employee` and `Territory` tables have a one to many relationship. They are connected through the `EmployeeTerritory` table and several employees have multiple territories, so `Employee` and `EmployeeTerritory` has a `one to many` relationship.

`EmployeeTerritory` and `Territory` has a `one to one` relationship since each territory ID is unique. So I believe that `Territory` inherits the `one to many` relationship of `EmployeeTerritory` as one EmployeeID may be associated with several TerritoryIDs.

I demonstrated this with the below query, which reveals that a single Employee.Id maps to several Territory.Id 

SELECT Employee.Id AS Emp, EmployeeTerritory.TerritoryId, 
COUNT(Territory.Id) as Territories
FROM EmployeeTerritory
LEFT JOIN Employee ON Employee.Id = EmployeeTerritory.EmployeeId
LEFT JOIN Territory ON EmployeeTerritory.TerritoryId = Territory.Id
GROUP BY Emp;




### What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

MongoDB designed to handle large unstructured datasets with high performance and accross many parallel machines. It scales well, handles unstable schema, and is robust in an undstable environmnet (such as when demand is increasing quickly).

However, because it is unstructured, if your data is structured (think of rows and columns where each row is an observation or customer) and you need to do a lot of aggregation (groupby, joins, etc), then SQL may be a better choice. 

It should also be mentioned that MongoDB is not necesarily ACID (Atomic Consistency Isolation Durability), it is eventually consistent, doesn't really have isolation since the 2.2 version (database specific write locks) and is perhaps best describved as weakly durable(lol). If ACID is important (banking, finance, etc) then MongoDB is not the best solution.

Also, if your database is relatively small and not going to rapidly increase in size, then a SQL solution may be more appropriate. 

### What is "NewSQL", and what is it trying to achieve?

NewSQL is a term for new relational database management systems that are trying to provide the scalability of NoSQL systems while keeping the stability (ACID) of SQL based systems.