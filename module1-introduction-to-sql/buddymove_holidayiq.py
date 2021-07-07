import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

print('\nQ1: Count how many rows you have - it should be 249!')
query = "SELECT COUNT(*) FROM review;"
num_rows = curs.execute(query).fetchall()[0][0]
print(num_rows)

print('\nQ2: How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
query = "SELECT COUNT(*) FROM review WHERE Nature > 99 AND Shopping > 99;"
result = curs.execute(query).fetchall()[0][0]
print(result)

print('\nStretch Q3: What are the average number of reviews for each category?')
categories = list(df.columns)[1:]
for cat in categories:
    query = "SELECT AVG(" + cat + ") FROM review;"
    cat_avg = curs.execute(query).fetchall()[0][0]
    print(cat + ': ' + str(cat_avg))
