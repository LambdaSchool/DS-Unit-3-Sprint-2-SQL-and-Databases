import pandas as pd 
import sqlite3
import queries as q

data = pd.read_csv('buddymove_holidayiq.csv')
print(data.head())

DBASE2 = 'buddymove_holidayiq.sqlite3'

conn2 = sqlite3.connect(DBASE2)


def avg_category(category, cursor):
	query = 'SELECT AVG(' + category +') from review'
	cursor.execute(query)
	return cursor.fetchall()[0][0]


try:
	cursor2 = conn2.cursor()

except:
	print('Cursor connection faile')

try:
	cursor2.execute('DROP TABLE IF EXISTS review')

except:
	print('ERROR encountered when dropping table')


try:
	data.to_sql('review', conn2, if_exists='fail')

except ValueError:
	print('Table already Exists: ',ValueError)

cursor2.execute(q.NUMBER_ROWS)
NUMBER_OF_ROWS = cursor2.fetchall()

cursor2.execute(q.NUMBER_OF_USERS)
USERS = cursor2.fetchall()[0][0]

AVG_SPORTS = avg_category('Sports', cursor=cursor2)
AVG_RELIGIOUS = avg_category('Religious', cursor=cursor2)
AVG_NATURE = avg_category('Nature', cursor=cursor2)
AVG_THEATRE = avg_category('Theatre', cursor=cursor2)
AVG_SHOPPING = avg_category('Shopping', cursor=cursor2)
AVG_PICNIC = avg_category('Picnic', cursor=cursor2)

print('Average Picnic Votes: ',AVG_PICNIC)

cursor2.execute('SELECT * FROM review limit 10')
collected = cursor2.fetchall()
print(collected)