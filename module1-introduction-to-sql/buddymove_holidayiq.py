import pandas as pd
import sqlite3


df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
#df.to_sql('reviews', conn)(ONLY ONCE)


#Count how many rows you have - it should be 249!
curs.execute("""
    SELECT COUNT('User ID')
    FROM review;
    """)
answer = curs.fetchall()[0][0]
print('There are', answer, 'rows')


#How many users who reviewed at least 100 Nature in the category 
#also reviewed at least 100 in the Shopping category?
curs.execute("""
    SELECT COUNT('User Id')
    FROM review
    WHERE Nature >= 100
    AND Shopping >= 100;
    """)
answer = curs.fetchall()[0][0]
print(answer, 'Users have reviewed at least 100 Nature and Shopping')


#(Stretch) What are the average number of reviews for each category?
curs.execute("""
    SELECT AVG(Sports), AVG(Religious), AVG(Nature),
    AVG(Theatre), AVG(Shopping), AVG(Picnic)
    FROM review;
    """)
answer = curs.fetchall()
average = pd.DataFrame(answer, columns = 
    ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic'])
print(average)


#Commit and close
curs.close()
conn.commit()
