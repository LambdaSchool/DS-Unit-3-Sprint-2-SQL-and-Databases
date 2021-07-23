import sqlite3
import pandas as pd

connect = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = connect.cursor()

df = pd.read_csv('buddymove_holidayiq.csv')

df.to_sql('buddy', connect)

curs.execute('SELECT COUNT(*) FROM buddy')
print(f'There are {curs.fetchall()[0][0]} rows in the database.')

curs.execute('SELECT COUNT(*) FROM buddy WHERE Nature > 99 AND Shopping > 99')
print(f'{curs.fetchall()[0][0]} users reviewed at least 100 in both Nature and Shopping.')