import warnings
import pandas as pd
import sqlite3
warnings.simplefilter(action='ignore', category=UserWarning)


df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

try:
    df.to_sql('buddymove_holidayiq.sqlite3', con=conn)
except ValueError:
    pass


def execute(sql_query):
    curs = conn.cursor()
    return curs.execute(sql_query).fetchall()


# count rows
query = 'SELECT COUNT(*) FROM "buddymove_holidayiq.sqlite3"'
print(f'Total Rows: {execute(query)[0][0]}\n')

# Users with at least 100 nature and shopping reviews
query = 'SELECT COUNT(*) FROM "buddymove_holidayiq.sqlite3" ' \
        'WHERE "Nature" >= 100 AND "Shopping" >= 100'
print(f'Users With Minimum 100 Reviews in Nature and Shopping: '
      f'{execute(query)[0][0]}\n')

# Average reviews for each category
categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
for x in categories:
    query = f'SELECT AVG({x}) FROM "buddymove_holidayiq.sqlite3"'
    print(f'Average Reviews For {x}: {execute(query)[0][0]}')
