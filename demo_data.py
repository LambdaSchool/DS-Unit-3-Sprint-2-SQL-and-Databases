### Part 1 - Making and populating a Database

'''Describe file'''

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

def make_cursor():
    ''' Detailed instructions '''
    curs = conn.cursor()
    
    curs.close()
    conn.commit()

###Example###
'''
| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |
'''

#How many rows do I have?

#How many rows where x, y at least 5?

#How many unique values of y are there?

#after this, save code to a py and upload to TL, same with sqlite DB