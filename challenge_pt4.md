#### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  
 Single (employee) to multiple (territories). The relationship between these tables is indicated in EmployeeTerritory.  Each territory has a minimum of one employee associated with it while many territories are associated with single employees
 
 
- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

MongoDB is suitable for project that require: the ability to be Document oriented, High performance, replication, high scalability, no rigid schema, field addition/deletion have less or no impact on the application, heterogeneous data, no joins, distribution, JSON or BSON, easy integration


MongoDB is not a good fit for: E-commerce product catalog, Blogs and content management, Real-time analytics and high-speed logging, caching, and high scalability.

  
  
- (*Stretch*) What is "NewSQL", and what is it trying to achieve?
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On
other tables (where it is a *foreign* key) it will be `CustomerId`. Also note -
the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
particular table, but it's a good lesson in the danger of keyword conflicts.

Answer the following questions (each is from a single table):

- What are the ten most expensive items (per unit price) in the database?
- What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)
- (*Stretch*) How does the average age of employee at hire vary by city?

Your code (to load and query the data) should be saved in `northwind.py`, and
added to the repository. Do your best to answer in purely SQL, but if necessary
use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at
individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?
- What is the largest category (by number of products in it)?
- (*Stretch*) What are the top five territories (by number of employees), and
  how many employees do they have?

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
- (*Stretch*) What is "NewSQL", and what is it trying to achieve?

### Part 5 - Turn it in!
Add all the files you wrote (`buddymove_holidayiq.py`, `northwind.py`), as well
as this file with your answers to part 7, to your weekly repo
(`DS-Unit-3-Sprint-2-SQL-and-Databases`). Commit, push, and await feedback from
your PM. Thanks for your hard work!

If you got this far, check out the [larger Northwind
database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip) -
your queries should run on it as well, with richer results.
