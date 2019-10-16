import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total characters are there?
def total_chars():
    curs.execute("""SELECT COUNT(distinct character_id)
    FROM charactercreator_character;""")
    return curs.fetchall()

# How many of each specific subclass?
def subclass_count():
    curs.execute("""SELECT 'mages', COUNT(*)
    FROM charactercreator_mage

    UNION

    SELECT 'clerics', COUNT(*)
    FROM charactercreator_cleric

    UNION

    SELECT 'fighter', COUNT(*)
    FROM charactercreator_fighter

    UNION

    SELECT 'thieves', COUNT(*)
    FROM charactercreator_thief;""")
    return curse.fetchall()

# How many total Items?
def total_items():
    curs.execute("""SELECT COUNT(distinct item_id)
    FROM armory_item;""")
    return curs.fetchall()

# How many of the Items are weapons? How many are not?
def weapon_items():
    curse.execute("""SELECT COUNT(*)
    FROM armory_weapon
    WHERE item_id IN
    (SELECT distinct item_ptr_id
    FROM armory_weapon);""")
    return curs.fetchall()

def nonweapon_items():
    curs.execute("""SELECT COUNT(*)
    FROM armory_item
    WHERE item_id NOT IN
    (SELECT distinct item_ptr_id
    FROM armory_item);""")
    return curs.fetchall()

# How many Items does each character have? (Return first 20 rows)
def chars_items():
    curs.execute("""SELECT character_id, count(item_id)
    FROM chractercreator_character_inventory
    GROUP BY character_id
    LIMIT 20;""")
    return curs.fetchall()

# How many Weapons does each character have? (Return first 20 rows)
def chars_weapons():
    curs.execute("""SELECT character_id, count(item_id)
    FROM charactercreator_character_inventory
    WHERE item_id IN
    (SELECT distinct item_ptr_id
    FROM armory_weapon)
    GROUP BY character_id
    LIMIT 20;""")
    return curs.fetchall()

# On average, how many Items does each Character have?
def avg_items():
    curs.execute("""SELECT AVG(items)
    FROM(
        SELECT character_id, count(item_id) as items
        FROM charactercreator_character_inventory
        GROUP BY character_id);""")
    return curs.fetchall()

# On average, how many Weapons does each character have?
def avg_weapons():
    curs.execute("""SELECT AVG(items)
    FROM(
        SELECT character_id, count(item_id) as items
        FROM charactercreator_character_inventory
        WHERE item_id IN (
            SELECT distinct item_ptr_id
            FROM armory_weapon)
        GROUP BY character_id);""")
    return curs.fetchall()