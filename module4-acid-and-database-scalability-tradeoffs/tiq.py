"""
tiq :: titanic_queries :: A package containing functions and more for querying the Titanic dataset.
"""

# %% Imports
import os
from pprint import pprint
import psycopg2


# ====== FuncZone ====== #


def quarry(conn, query, params=None, returns=True):
    """
    Runs a query against a database and commits changes.
    Does not close the connection - use a context manager if possible.
    
    Parameters
    ----------
    connection : connection object
        The connection object which allows interaction with the db.
    query : string
        SQL query to be run against the db.
    params : object (optional); default None.
        Python object(s) to be passed into query as parameter(s).
    returns : bool; default True
        If query returns a value (such as with SELECT), this should be True.
        If query does not return a value, (CREATE TABLE / INSERT), then False.
    """
    # Create cursor object
    cur = conn.cursor()

    # Execute the query
    if params is not None:
        cur.execute(query, params)
    else:
        cur.execute(query)

    # If returns is True, assign the query to variable
    if returns:
        results = cur.fetchall()
        pprint(results)

    # If not, do not create variable to return
    # Close the cursor and the connection
    cur.close()
    conn.commit()

    # If returns is True, return the return value
    if returns:
        return results


# ====== Queries ======

count_survived = """--- How many passengers survived, and how many died?
SELECT
    survived,
    COUNT(*) AS survive_count
FROM
    passengers
GROUP BY 
    survived;"""

count_class = """--- How many passengers were in each class?
SELECT
    pclass,
    COUNT(*) AS class_count
FROM passengers
GROUP BY pclass;"""

count_class_survived = """--- How many passengers survived/died within each class?
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
    survived;"""

avg_age_survived = """--- What was the average age of survivors vs nonsurvivors?
SELECT
    survived,
    AVG(age) AS avg_age
FROM passengers
GROUP BY survived;"""

avg_age_class = """--- What was the average age of each passenger class?
SELECT
    pclass,
    AVG(age) AS avg_age
FROM passengers
GROUP BY pclass
ORDER BY pclass;"""

avg_fare = """--- What was the average fare by passenger class? By survival?
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
    survived;"""

avg_spouse = """--- How many siblings/spouses aboard on average, by passenger class? By survival?
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
    survived;"""

avg_parent_child = """--- How many parents/children aboard on average, by passenger class? By survival?
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
    survived;"""

# Create list of the above queries
qez = [
    count_survived,
    count_class,
    count_class_survived,
    avg_age_survived,
    avg_age_class,
    avg_fare,
    avg_spouse,
    avg_parent_child,
]

same_name = """--- Do any passengers have the same name?
SELECT
    split_part(name, ' ', 2) AS first_name,
    COUNT(*) AS count
FROM passengers
GROUP BY first_name
HAVING COUNT(*) > 1;"""

all_with_sib_spouse = """
--- How many married couples were aboard the Titanic?
SELECT
    reverse(split_part(reverse(name), ' ', 1)) AS last_name,
    COUNT(*) AS count
FROM passengers
WHERE siblings_spouses_aboard >= 1
GROUP BY last_name;"""

