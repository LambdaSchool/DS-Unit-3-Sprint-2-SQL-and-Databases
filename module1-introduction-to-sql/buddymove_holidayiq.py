import sqlite3
import pandas as pd

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df = pd.read_csv("buddymove_holidayiq.csv")

print(df.shape)
#print(df.head())

# Creating new sql database from df
df.to_sql(name='review', con=conn, if_exists='replace')

curs = conn.cursor()

# Count how many rows you have - it should be 249!
query1 = ''' SELECT COUNT(*)
FROM review;
'''

curs.execute(query1)
print('SQL Database has', curs.fetchall()[0][0], 'rows.')

'''How many users who reviewed at least 100 Nature in the category also
reviewed at least 100 in the Shopping category?'''
query2 = '''SELECT COUNT(uid) 
            FROM (SELECT 'User Id' as uid
            FROM review
            WHERE Nature > 100 AND Shopping > 100);'''

curs.execute(query2)
print(curs.fetchall()[0][0],
      "Users reviewed at least 100 Nature and 100 Shopping Category")

curs.close()
conn.commit()
