import sqlite3


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()



def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

TOTAL_CHARACTERS = """
  SELECT COUNT(DISTINCT name) 
  FROM charactercreator_character;
"""


print('Total Characters:')
execute_query(curs, TOTAL_CHARACTERS)


SUBCLASS_TOTALS = """
  SELECT  (
        SELECT COUNT(character_ptr_id)
        FROM   charactercreator_cleric
        ) AS Cleric,
        (
        SELECT COUNT(character_ptr_id)
        FROM   charactercreator_fighter
        ) AS Fighter,
		    (
		    SELECT COUNT(character_ptr_id)
        FROM   charactercreator_mage
		    ) AS Mage,
		    (
		    SELECT COUNT(mage_ptr_id)
        FROM   charactercreator_necromancer
		    ) AS Necromancer,
		    (
		    SELECT COUNT(character_ptr_id)
        FROM   charactercreator_thief
		    ) AS Thief;
"""


print('Subclass Totals:')
execute_query(curs, SUBCLASS_TOTALS)


ITEM_TOTALS = """
  SELECT COUNT(item_id)
  FROM armory_item
"""


print('Item Totals:')
execute_query(curs, ITEM_TOTALS)


WEAPONS_TOTAL = """
  SELECT COUNT(item_ptr_id)
  FROM armory_weapon
"""


print('Weapons Totals:')
execute_query(curs, WEAPONS_TOTAL)


WEAPONS_DIFF = """
  SELECT  (
		 SELECT 
		 count(item_id) as val2
		 FROM armory_item  
		 ) - (
		 SELECT
		 COUNT(item_ptr_id) as val1
		 FROM armory_weapon
		 ) as total_count
""" 


print('Weapons Diff:')
execute_query(curs, WEAPONS_DIFF)


CHAR_ITEM_TOTALS = """
  SELECT character_id, COUNT(DISTINCT item_id)FROM
  (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
  FROM charactercreator_character as CC,
  armory_item as ai,
  charactercreator_character_inventory as cci
  WHERE cc.character_id = cci.character_id
  AND ai.item_id = cci.item_id)
  GROUP BY 1 ORDER BY 2 DESC
  LIMIT 20;
  """


print('Character Item Totals:')
execute_query(curs, CHAR_ITEM_TOTALS)

CHAR_WEAPON_TOTALS = """
  SELECT character_id, COUNT(DISTINCT item_id)FROM
  (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
  FROM charactercreator_character as cc,
  armory_item as ai,
  armory_weapon as aw,
  charactercreator_character_inventory as cci
  WHERE cc.character_id = cci.character_id
  AND ai.item_id = cci.item_id
  AND ai.item_id = aw.item_ptr_id)
  GROUP BY 1 ORDER BY 2 DESC
  LIMIT 20;
"""


print('Character Weapon Totals:')
execute_query(curs, CHAR_WEAPON_TOTALS)


AVG_ITEM = """
  SELECT avg(ic)
	  FROM
	    (
       SELECT character_id, COUNT(DISTINCT item_id) as ic
	     FROM
       (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
        FROM charactercreator_character as CC,
		    armory_item as ai,
		    charactercreator_character_inventory as cci
		    WHERE cc.character_id = cci.character_id
		    AND ai.item_id = cci.item_id)
		    GROUP BY 1 ORDER BY 2 ASC
	    )
"""


print('Character Items Average:')
execute_query(curs, AVG_ITEM)

# TO-DO , this is the average weapon of those that have weapons
# find out how to make it average weapons for all. 
AVG_WEAPON = """
SELECT avg(wa)
	FROM
	  (
       SELECT character_id, COUNT(DISTINCT item_id) as wa
	   FROM
	  (SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
	   FROM charactercreator_character as cc,
	   armory_item as ai,
	   armory_weapon as aw,
	   charactercreator_character_inventory as cci
	   WHERE cc.character_id = cci.character_id
	   AND ai.item_id = cci.item_id
	   AND ai.item_id = aw.item_ptr_id)
	   GROUP BY 1 ORDER BY 2 DESC
	   )
"""


print('Character Weapons Average:')
execute_query(curs, AVG_WEAPON)
print('this needs to be fixed')