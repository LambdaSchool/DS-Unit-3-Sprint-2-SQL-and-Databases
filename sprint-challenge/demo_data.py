import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")


# Part 1

create_statement = """
    CREATE TABLE IF NOT EXIST demo (
    s varchar(1) NOT NULL PRIMARY KEY,
    x SMALLINT,
    y SMALLINT)
"""

# create cursor and execute create statement
curs = conn.cursor()
curs.execute(create_statement)
conn.commit()
curs.close()


insert_statment = """
    INSERT INTO demo VALUES ('g', 3, 9), 
    ('v', 5, 7), ('f', 8, 7);
"""
# create cursor and execute insert statement
curs = conn.cursor()
curs.execute(insert_statment)
conn.commit()
curs.close()

# Queries
demo_qs = [
    "Count how many rows you have - it should be 3!",
    "How many rows are there where both x and y are at least 5?",
    "How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?",
]

demo_as = [
    "SELECT count(s) from demo;",
    "SELECT count(s) FROM demo WHERE x >= 5 AND y >=5;",
    "SELECT count(DISTINCT y) FROM demo;",
]

# answer queries:

for q, a in zip(demo_qs, demo_as):

    # print questions
    print("Question ", demo_qs.index(q) + 1)
    print(q)

    # print query
    print("SQL query :")
    print(a)

    # create a connection object and execute query
    curs = conn.cursor()
    curs.execute(a)
    output = curs.fetchall()

    print("Output: ")
    print(output, "\n")

    # close cursor
    curs.close()

# # close any open cursors and connection
curs.close()
conn.close()
