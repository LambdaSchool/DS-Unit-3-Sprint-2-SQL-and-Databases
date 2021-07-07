--- Companion file to titanic_queries.py
--- Created to build the queries in an
--- in an environment with syntax highlighting
--- and other useful tools.

-- --- Create titanic passengers table in postgres
-- CREATE TABLE passengers (
--     id SERIAL PRIMARY KEY,
--     survived INT,
--     pclass INT,
--     name VARCHAR(88),
--     sex VARCHAR(8),
--     age FLOAT,
--     siblings_spouses_aboard INT,
--     parents_children_aboard INT,
--     fare FLOAT
-- );

-- --- Drop passengers table to start over
-- DROP TABLE passengers;


--- ====== Queries for Questions ======

--- How many passengers survived, and how many died?
SELECT
    survived,
    COUNT(*) AS survive_count
FROM passengers
GROUP BY survived;

--- How many passengers were in each class?
SELECT
    pclass,
    COUNT(*) AS class_count
FROM passengers
GROUP BY pclass;

--- How many passengers survived/died within each class?
SELECT
    pclass,
    survived,
    COUNT(*) AS class_count
FROM passengers
GROUP BY 
    pclass,
    survived
ORDER BY
    pclass,
    survived;

--- What was the average age of survivors vs nonsurvivors?
SELECT
    survived,
    AVG(age) AS avg_age
FROM passengers
GROUP BY survived;

--- What was the average age of each passenger class?
SELECT
    pclass,
    AVG(age) AS avg_age
FROM passengers
GROUP BY pclass
ORDER BY pclass;

--- What was the average fare by passenger class? By survival?
SELECT
    pclass,
    survived,
    AVG(fare) as avg_fare
FROM passengers
GROUP BY 
    pclass,
    survived
ORDER BY
    pclass,
    survived;

--- How many siblings/spouses aboard on average, by passenger class? By survival?
SELECT
    pclass,
    survived,
    AVG(siblings_spouses_aboard) as avg_sib_spouse
FROM passengers
GROUP BY 
    pclass,
    survived
ORDER BY
    pclass,
    survived;

--- How many parents/children aboard on average, by passenger class? By survival?
SELECT
    pclass,
    survived,
    AVG(parents_children_aboard) as avg_parent_child
FROM passengers
GROUP BY 
    pclass,
    survived
ORDER BY
    pclass,
    survived;

--- Do any passengers have the same name?
SELECT
    split_part(name, ' ', 2) AS first_name,
    COUNT(*) AS count
FROM passengers
GROUP BY first_name
HAVING COUNT(*) > 1;

--- How many married couples were aboard the Titanic? Assume that two people (one `Mr.` and one `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are a married couple.
SELECT
    reverse(split_part(reverse(name), ' ', 1)) AS last_name,
    COUNT(*) AS count
FROM passengers
WHERE siblings_spouses_aboard >= 1
GROUP BY last_name;

--- Simple select
SELECT * FROM passengers;
