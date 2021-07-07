#!/usr/bin/env python

# imports
import sqlite3

# establish connection to db
conn = sqlite3.connect('demo_data.sqlite3')

# create table statement
create_table = """
CREATE TABLE demo (
    s CHARACTER(1),
    x INT,
    y INT
)
"""

# establish cursor
cur = conn.cursor()

# create table and commit
cur.execute(create_table)
conn.commit()

# insert rows into table
insert_info = """
INSERT INTO demo (
    s,
    x,
    y
)
VALUES
    ('g',3,9),
    ('v',5,7),
    ('f',8,7)
"""

cur.execute(insert_info)
conn.commit()