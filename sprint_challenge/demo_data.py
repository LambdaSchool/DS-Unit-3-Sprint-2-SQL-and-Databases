# ./usr/bin/env python
"""
Sample output (for reference):

Total rows: 3

Rows where x and y are at least 5: 2

Unique values of y: 2

"""
import sqlite3

# Create new database
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

# Create table
schema = """CREATE TABLE "demo" (
    "s" TEXT,
    "x" INT,
    "y" INT
);"""
cur.execute(schema)

# Populate table
insert_data = """
INSERT INTO "demo" 
VALUES ('g',3,9),
       ('v',5,7),
       ('f',8,7);
"""
cur.execute(insert_data)

# Check database contents
cur.execute("""
SELECT COUNT(*)
FROM demo
""")
print()
print(f'Total rows: {cur.fetchall()[0][0]}')

cur.execute("""
SELECT COUNT(*)
FROM demo
WHERE
    x >= 5
AND y >= 5
""")
print()
print(f'Rows where x and y are at least 5: {cur.fetchall()[0][0]}')

cur.execute("""
SELECT COUNT(DISTINCT y)
FROM demo
""")
print()
print(f'Unique values of y: {cur.fetchall()[0][0]}')

# Wrap it up
conn.commit()
cur.close()
conn.close()
