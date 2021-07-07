import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query1 = 'SELECT count(*) FROM charactercreator_character;'
query2 = """SELECT cc.name AS character_name, ai.name AS item_name FROM
charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE
cc.character_id = cci.character_id AND
ai.item_id = cci.item_id
GROUP BY cc.name;"""
result = curs.execute(query2)
result.fetchall()
query2
