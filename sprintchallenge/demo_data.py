import sqlite3 as sql

# Create connetion to the demo data
myconnection = sql.connect('demo_data.sqlite3')

# Create cursor to demo data
mycursor = myconnection.cursor()

# Create SQL table feilds, 1 letter for s, intergers for x and y
create_table = """
CREATE TABLE demo (
    s CHARACTER(1),
    x INT,
    y INT
)
"""

# Create the SQL table
mycursor.execute(create_table)

# Commit the SQL table-so it doesn't disapear in ram
myconnection.commit()

# Add data to the feilds created
add_data = """
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

mycursor.execute(add_data)
myconnection.commit()

#Questions!

rows = 'SELECT COUNT(s) FROM demo'

demo_data_row_total = myconnection.cursor().execute(rows).fetchone()[0]

print('Question 1')
print('---')
print ('Count how many rows you have- it should be 3! It is:', demo_data_row_total)
print('---')

both_x_y_atleast_5 = """SELECT COUNT (s) FROM demo
    WHERE x >= 5
    AND y >= 5;"""

demo_data_x_y_more_than_5 = mycursor.execute(both_x_y_atleast_5).fetchone()

print('Question 2')
print('---')
print ('How many rows are there where both x and y are atleast 5?', demo_data_x_y_more_than_5[0])
print('---')
print('Question 3')
print('---')

y_unique_value = 'SELECT COUNT (DISTINCT y) FROM demo'

demo_data_unique_y_values = mycursor.execute(y_unique_value).fetchone()[0]

print ('How many unique values of y are there?', demo_data_unique_y_values)
