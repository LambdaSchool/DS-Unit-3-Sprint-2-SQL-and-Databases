
import sqlalchemy
import pandas as pd
import sqlite3

engine = sqlalchemy.create_engine('sqlite:///buddymove_holidayiq.db', echo=False)

df = pd.read_csv(
    'https://raw.githubusercontent.com/chefdarek/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
)
df.to_sql("buddymove_holidayiq",con=engine, if_exists='replace')

conn = sqlite3.connect('buddymove_holidayiq.db')
c = conn.cursor()
''''''
#c.execute('''SELECT COUNT(*) FROM buddymove_holidayiq''')
#print(c.fetchone())

#c.execute('''SELECT * FROM buddymove_holidayiq WHERE Nature = 100 AND Shopping =100''')
#print(c.fetchone())

#c.execute('''SELECT * FROM buddymove_holidayiq AVG(*)''')
#print(c.fetchone())

