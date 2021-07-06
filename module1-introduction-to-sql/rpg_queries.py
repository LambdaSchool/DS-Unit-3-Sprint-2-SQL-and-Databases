import sqlite3 as sql
import pandas as pd

connect = sql.connect('rpg_db.sqlite3')
curse = connect.cursor()


def total_char_count():
    '''Total all characters'''
    print(pd.read_sql_query('''SELECT COUNT(distinct character_id)
        FROM charactercreator_character;''', connect))


def sub_class():
    '''Grab population count of each subclass of characters'''
    print(pd.read_sql_query('''SELECT "mages", COUNT(*)
        From charactercreator_mage

        UNION

        SELECT "clerics", COUNT(*)
        FROM charactercreator_cleric

        UNION

        SELECT "fighter", COUNT(*)
        FROM charactercreator_fighter

        UNION

        SELECT "thieves", COUNT(*)
        FROM charactercreator_thief;''', connect))


def item_count():
    '''Total count of all items'''
    print(pd.read_sql_query('''SELECT COUNT(distinct item_id)
        FROM armory_item;''', connect))


def weapons():
    '''Amount of items that are weapons'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM armory_item
        WHERE item_id IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon);''', connect))


def not_weapon():
    '''Any item that is not  weapon'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM armory_item
        WHERE item_id NOT IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon);''', connect))


def char_items():
    '''Amount of items a character has, first 20 characters'''
    print(pd.read_sql_query(''' SELECT character_id, COUNT( item_id)
        FROM charactercreator_character_inventory
        GROUP BY character_id
        LIMIT 20;''', connect))


def char_weapons():
    '''Weapons held by characters, first 20 characters'''
    print(pd.read_sql_query('''SELECT character_id,COUNT(item_id)
        From charactercreator_character_inventory
        WHERE item_id IN
            (SELECT distinct item_ptr_id
                FROM armory_weapon)
        GROUP BY character_id
        LIMIT 20;''', connect))


def item_avg():
    '''How many items the average person carries'''
    print(pd.read_sql_query('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) AS items
            FROM charactercreator_character_inventory
            GROUP BY character_id);''', connect))


def weapon_avg():
    '''Average weapon count per character'''
    print(pd.read_sql_query('''SELECT AVG(items)
        FROM(
            SELECT character_id, COUNT(item_id) as items
            FROM charactercreator_character_inventory
            Where item_id IN(
                    SELECT distinct item_ptr_id
                    FROM armory_weapon)
            GROUP BY character_id);''', connect))
