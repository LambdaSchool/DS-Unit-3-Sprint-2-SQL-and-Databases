import pandas as pd 
import sqlite3
import queries as q


DBASE = 'rpg_db.sqlite3'
DBASE2 = 'buddymove_holidayiq.sqlite3'

def connect_db(db_name):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	return cursor

def retrieve_data(cursor, sql_statement):
	cursor.execute(sql_statement)
	return cursor.fetchall()[0][0]


cursor = connect_db(DBASE)

cursor.execute(q.TOTAL_CHARACTERS)
TOTAL_CHARACTERS = retrieve_data(cursor, q.TOTAL_CHARACTERS)

#############################################
# SUBCLASSES FOR EACH OF THE VARIOUS GROUPS #
#############################################

cursor.execute('select count(*) count_cleric from charactercreator_character cc where cc.character_id IN (select character_ptr_id from charactercreator_cleric)')
subclass_cleric = cursor.fetchall()[0][0]
cursor.execute('select count(*) count_thief from charactercreator_character cc where cc.character_id IN (select character_ptr_id from charactercreator_thief)')
subclass_thief = cursor.fetchall()[0][0]
cursor.execute('select count(*) count_thief from charactercreator_character cc where cc.character_id IN (select character_ptr_id from charactercreator_mage)')
subclass_mage = cursor.fetchall()[0][0]
cursor.execute('select count(*) count_thief from charactercreator_character cc where cc.character_id IN (select character_ptr_id from charactercreator_fighter)')
subclass_fighter = cursor.fetchall()[0][0]

TOTAL_ITEMS = retrieve_data(cursor, q.TOTAL_ITEMS)

TOTAL_SUBCLASS = subclass_cleric + subclass_thief + subclass_mage + subclass_fighter

WEAPONS = retrieve_data(cursor, q.WEAPONS)

NON_WEAPONS = retrieve_data(cursor, q.NON_WEAPONS)

CHARACTER_ITEMS = retrieve_data(cursor, q.CHARACTER_ITEMS)

CHARACTER_WEAPONS = retrieve_data(cursor, q.CHARACTER_WEAPONS)

AVG_CHARACTER_ITEMS = retrieve_data(cursor, q.AVG_CHARACTER_ITEMS)

AVG_CHARACTER_WEAPONS = retrieve_data(cursor, q.AVG_CHARACTER_WEAPONS)

print(AVG_CHARACTER_WEAPONS)


data = pd.read_csv('buddymove_holidayiq.csv')
print(data.head())

conn2 = sqlite3.connect(DBASE2)

try:
	cursor2 = conn2.cursor()

except:
	print('Database might already exist')

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

print('Number of users: ',USERS)

cursor2.execute('SELECT * FROM review limit 10')
collected = cursor2.fetchall()
print(collected)



conn2.commit()
cursor.close()
cursor2.close()



#TOTAL_SUBCLASS = cursor.execute(q.TOTAL_SUBCLASS).fetchall()

###########################
# CONNECT TO NEW DATABASE #
###########################

# conn2 = sqlite3.connect(DBASE2)

# pd.to_sql('review', conn2, dtype={'User Id': int,'Sports' : int,'Religious': int,'Nature': int,'Theatre': int,'Shopping': int, 'Picnic': int})








# try:
# 	cursor.execute(q.statement_2)

# except:
# 	print("Couldn't create table")

# for data in cursor.execute(q.select_all):
# 	print(data)


# for table in cursor.execute(q.show_tables):
# 	print(table)

# cursor.execute(q.insert_into)

# for i in cursor.execute('SELECT * FROM test_table'):
# 	print(i)

# conn.commit()
# conn.close()