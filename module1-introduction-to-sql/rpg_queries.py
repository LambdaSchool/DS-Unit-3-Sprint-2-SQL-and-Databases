import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


CHARACTER_COUNT = """
SELECT COUNT(character_id)
FROM charactercreator_character;
"""

CLERIC_COUNT = """
SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric;
"""

FIGHTER_COUNT = """
SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;
"""

MAGE_COUNT = """
SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;
"""

NECRO_COUNT = """
SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer;
"""

THIEF_COUNT = """
SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;
"""

ITEM_COUNT = """
SELECT COUNT(item_id)
FROM armory_item;
"""

WEAPON_COUNT = """
SELECT COUNT(DISTINCT item_id)
FROM armory_item, armory_weapon
WHERE item_id = item_ptr_id;
"""

CHAR_INV_COUNT = """
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

CHAR_WEAP_COUNT = """
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id
LIMIT 20;
"""

CHAR_INV_AVG = """
SELECT AVG(items.avg_count) FROM
(SELECT COUNT(item_id) AS avg_count
FROM charactercreator_character_inventory
GROUP BY character_id) AS items;
"""

CHAR_WEAP_AVG = """
SELECT AVG(weapons.avg_count) FROM
(SELECT COUNT(item_id) AS avg_count
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id) AS weapons;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()

    results1 = execute_query(curs, CHARACTER_COUNT)[0][0]
    print('How many total characters are there?')
    print(f'There are {results1} characters.')
    print('***************')

    total_cleric = execute_query(curs, CLERIC_COUNT)[0][0]
    total_fight = execute_query(curs, FIGHTER_COUNT)[0][0]
    total_mage = execute_query(curs, MAGE_COUNT)[0][0]
    total_necro = execute_query(curs, NECRO_COUNT)[0][0]
    total_thief = execute_query(curs, THIEF_COUNT)[0][0]
    print('How many of each specific subclass?')
    print(f'Breakdown of classes: {total_cleric} clerics, {total_fight} fighters, {total_thief} thieves, and {total_mage} mages, {total_necro} of which are necromancers.')
    print('***************')

    total_items = execute_query(curs, ITEM_COUNT)[0][0]
    print('How many total items?')
    print(f'There are {total_items} items in the game.')
    print('***************')

    total_weap = execute_query(curs, WEAPON_COUNT)[0][0]
    print ('How many of the items are weapons? How many are not?')
    print(f'Of these, {total_weap} are weapons and {total_items - total_weap} are not.')
    print('***************')

    char_items = execute_query(curs, CHAR_INV_COUNT)[0:20]
    print('How many Items does each character have? (Return first 20 rows)')
    print('Number of items in the top 20 inventories:')
    print(char_items)
    print('***************')

    char_weapons = execute_query(curs, CHAR_WEAP_COUNT)[0:20]
    print('How many Weapons does each character have? (Return first 20 rows)')
    print('And these are the number of weapons within them:')
    print(char_weapons)
    print('***************')

    char_avg_items = execute_query(curs, CHAR_INV_AVG)[0][0]
    print('On average, how many Items does each Character have?')
    print(f'The average number of items carried by players is {char_avg_items}')
    print('***************')

    char_avg_weaps = execute_query(curs, CHAR_WEAP_AVG)[0][0]
    print('On average, how many Weapons does each Character have?')
    print(f'The average number of weapons carried by players is {char_avg_weaps}')
    print('***************')
