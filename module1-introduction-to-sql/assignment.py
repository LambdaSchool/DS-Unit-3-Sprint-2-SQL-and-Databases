import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

"""Total number of characters"""
query1 = 'SELECT COUNT(*) FROM charactercreator_character'
print('The total number of characters are:', curs.execute(query1).fetchone())

"""How many of each specific sublcass"""
query2 = 'SELECT COUNT(*) FROM charactercreator_fighter'
print('The total number of fighters are:', curs.execute(query2).fetchone())

query3 = 'SELECT COUNT(*) FROM charactercreator_cleric'
print('The Total number of clerics are:', curs.execute(query3).fetchone())

query4 = 'SELECT COUNT(*) FROM charactercreator_mage'
print('The total number of mages are:', curs.execute(query4).fetchone())

query5 = 'SELECT COUNT(*) FROM charactercreator_thief'
print('The total number of thieves are:', curs.execute(query5).fetchone())

"""Total # of items:"""
query6 = 'SELECT COUNT(*) FROM armory_item'
print('The total number of items are:', curs.execute(query6).fetchone())

"""Total # of weapons"""
query7 = 'SELECT COUNT(*) FROM armory_weapon'
print('The Total number of weapons are:', curs.execute(query7).fetchone())

"""Total # of items that are not weapons:"""
print('The total number of Items that are not weapons are:', 174-37)

"""How many Items does each character have (first 20 rows)"""
query9 = """
SELECT COUNT(cci.item_id)
FROM charactercreator_character as cc,
charactercreator_character_inventory as cci
WHERE cci.character_id = cc.character_id
GROUP BY cc.character_id;
"""
print('The number of items per character are:', curs.execute(query9).fetchmany(20))

"""How many weapons does each character have (first 20 rows)?"""
query10 = """
SELECT COUNT(AW.item_ptr_id)
FROM charactercreator_character_inventory as cci,
charactercreator_character as cc,
armory_item as ai,
armory_weapon as aw
WHERE cci.character_id = cc.character_id
AND cci.item_id = ai.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id;
"""
print('The number of weapons per character are:', curs.execute(query10).fetchmany(20))

"""On average, how many Items does each character have?"""
query11 = """
SELECT AVG(avg_items)
FROM(SELECT COUNT(CCI.item_id) as avg_items
FROM charactercreator_character as cc,
charactercreator_character_inventory as cci
WHERE cci.character_id = CC.character_id
GROUP BY cc.character_id) AS T;
"""
print('The avg. num of items per character are:', curs.execute(query11).fetchone())

"""On average, how many Weapons does each character have?"""
query12 = """
SELECT AVG(avg_weaps)
FROM (SELECT COUNT(AW.item_ptr_id) as avg_weaps
FROM charactercreator_character_inventory as cci,
charactercreator_character as cc,
armory_item as ai,
armory_weapon as aw
WHERE cci.character_id = CC.character_id
AND cci.item_id = ai.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id) AS Z;
"""
print('The avg. num of weapons per character are:', curs.execute(query12).fetchone())

curs.close()
conn.commit()