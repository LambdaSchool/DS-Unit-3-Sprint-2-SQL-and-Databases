--- Companion file to titanic_queries.py
--- Created to build the queries in an
--- in an environment with syntax highlighting
--- and other useful tools.

--- Create titanic passengers table in postgres
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(88),
    sex VARCHAR(8),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT
);

--- Drop passengers table to start over
DROP TABLE passengers;


--- ====== Queries for Questions ======

--- How many passengers survived, and how many died?
SELECT
    survived,
    COUNT(*) AS survive_count
FROM
    passengers
GROUP BY 
    survived;

--- How many passengers were in each class?
SELECT
    pclass,
    COUNT(*) AS class_count
FROM
    passengers
GROUP BY 
    pclass


--- How many passengers survived/died within each class?


--- What was the average age of survivors vs nonsurvivors?


--- What was the average age of each passenger class?


--- What was the average fare by passenger class? By survival?


--- How many siblings/spouses aboard on average, by passenger class? By survival?


--- How many parents/children aboard on average, by passenger class? By survival?


--- Do any passengers have the same name?


--- How many married couples were aboard the Titanic? Assume that two people (one `Mr.` and one `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are a married couple.




