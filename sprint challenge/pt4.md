## Part Four: Sql and Databases Sprint Challenge

### Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  - _**The relationship is many to many; an employee can have more than one territory, and a territory can have more than one employee. Combining this relationship in the EmployeeTerritories table is utilized to provide lots of unique, interpretable values.**_
- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  - _**A document store is an example of an object oriented database, or 'NoSQL'. These databases are appropriate when data is changing quickly and often, or data is constantly being collected and 'dumped' but complete order and organization of the data is not completely clear or necessary (e.g. a private sector venture capital firm utilizing machine learning and AI to predict successful indicators in the Consumer industry). NoSQL provides flexibility in data collection while sacrificing order. Contrarily, NoSQL dbs are inappropriate when the data collection can or needs to be ordered and rigid. Relational dbs (SQL) provide structure and predictability (e.g. a healthcare provider collecting customer information).**_
