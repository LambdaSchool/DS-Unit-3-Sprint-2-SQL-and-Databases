import os 
import sqlite3

#DB_FILEPATH = "fpg_db.sqlite3"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), ".", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("Connection: ", connection)

cursor = connection.cursor()
print("Cursor: ", cursor)

query = """
SELECT
	character_id
	,count(DISTINCT character_id) as CharacterCount
FROM charactercreator_character
"""

result = cursor.execute(query).fetchall()
print("Result: ", result)

for row in result:
	print("")
	print(type(row))
	print(row)
	print(row[0])
	print("-------")
	print(row[1])
	print("-------")