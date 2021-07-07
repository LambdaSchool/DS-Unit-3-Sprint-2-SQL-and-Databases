import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Engine use for sql query
engine = create_engine('sqlite://', echo=False)

# DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

# Create a new Database
conn = sqlite3.connect('buddymove_holiday.sqlite3')

# Use df as sql
df.to_sql('buddymove_holiday', con=engine)

# Use the engine to execute query
print('The count is:', engine.execute('SELECT COUNT(*) FROM buddymove_holiday').fetchone()[0])

print('The number of users who reviewed at least 100 Nature and Shopping category:', engine.execute('SELECT COUNT(*) FROM buddymove_holiday WHERE Nature>=100 AND Shopping >= 100').fetchone()[0])