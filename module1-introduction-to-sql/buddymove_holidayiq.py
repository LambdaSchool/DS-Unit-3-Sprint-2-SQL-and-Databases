import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
review = pd.read_csv('buddymove_holidayiq.csv')
review.to_sql('review', con=conn, if_exists = 'replace')


def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


ROW_COUNT= """ 
SELECT COUNT(*) FROM review;
"""


print('Row Count:')
execute_query(curs, ROW_COUNT)


USER_COUNT = """
SELECT COUNT(*)
FROM review
WHERE Nature >= 100
AND Shopping >= 100;
"""


print('Users who love nature and shopping count:')
execute_query(curs, USER_COUNT)