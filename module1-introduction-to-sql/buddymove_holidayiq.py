
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
c.execute('''SELECT COUNT(*) FROM buddymove_holidayiq''')
print(c.fetchone())

c.execute('''SELECT * FROM buddymove_holidayiq WHERE Nature = 100 AND Shopping =100''')
print(c.fetchone())

#c.execute('''SELECT * FROM buddymove_holidayiq AVG(*)''')
#print(c.fetchone())

# Load the data (use pandas) from the provided file buddymove_holidayiq.csv (the BuddyMove Data Set) - you should have 249 rows, 7 columns, and no missing values. The data reflects the number of place reviews by given users across a variety of categories (sports, parks, malls, etc.).

# Using the standard sqlite3 module:

#     Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
#     Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database

# Then write the following queries (also with sqlite3) to test:

#     Count how many rows you have - it should be 249!
#     How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
#     (Stretch) What are the average number of reviews for each category?

# Your code (to reproduce all above steps) should be saved in buddymove_holidayiq.py, and added to the repository along with the generated SQLite database.