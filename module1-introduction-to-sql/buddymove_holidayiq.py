import pandas as pd
import sqlite3

# load df
df = pd.read_csv('buddymove_holidayiq.csv')

#connect to blank database
with sqlite3.connect('buddymove_holidayiq.sqlite3') as conn:
    df.to_sql('buddymove_holidayiq', con=conn, index=False, 
    if_exists='replace')


#create our connection object
curs = conn.cursor()

#query db for # of rows
query = """select count('User ID')
from buddymove_holidayiq;
"""
result = curs.execute(query)
output = result.fetchall().pop()[0]

print('SQL row length is', output)

#query db for descriminating user reviews
query = """select count('User Id')
from buddymove_holidayiq
where Nature >=100 and Shopping >= 100;
"""
result = curs.execute(query)
output = result.fetchall().pop()[0]

print('%d users reviewed at least 100 in Nature and also reviewed at least 100 in Shopping' % output)

