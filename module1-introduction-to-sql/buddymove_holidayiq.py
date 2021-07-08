import pandas as pd
import sqlite3


df = pd.read_csv("buddymove_holidayiq.csv")
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

print(df.head())

df.to_sql(name='review', con=conn, if_exists='replace')

curs = conn.cursor()

query1 = '''SELECT COUNT (*) FROM review;'''
rows = curs.execute(query1).fetchall()
print("Total number of rows expected: 249. Rows counted: {}".format(rows[0][0]))

query2 = '''SELECT COUNT(UID) 
            FROM (
                SELECT 'User Id' AS UID
                FROM review
                WHERE Nature > 100 AND Shopping > 100
            )'''
users = curs.execute(query2).fetchall()
print("Number of users with at least 100 'Nature' and 'Shopping' reviews: {}".format(users[0][0]))

query3 = '''SELECT AVG(Sports), AVG(Religious), AVG(Nature),
            AVG(Theatre), AVG(Shopping), AVG(Picnic)
            FROM review'''

print(curs.execute(query3).fetchall())

curs.close()
conn.commit()
