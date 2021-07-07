# ./usr/bin/env python
import sqlite3
sl_con = sqlite3.connect('rpg_db.sqlite3')

characters = sl_con.execute(
    'SELECT * FROM charactercreator_character;').fetchall()
clerics = sl_con.execute(
    'SELECT * FROM charactercreator_cleric;').fetchall()
fighters = sl_con.execute(
    'SELECT * FROM charactercreator_fighter;').fetchall()
mages = sl_con.execute(
    'SELECT * FROM charactercreator_mage;').fetchall()
necromancers = sl_con.execute(
    'SELECT * FROM charactercreator_necromancer;').fetchall()
thiefs = sl_con.execute(
    'SELECT * FROM charactercreator_thief;').fetchall()
items = sl_con.execute(
    'SELECT * FROM armory_item;').fetchall()
weapons = sl_con.execute(
    'SELECT * FROM armory_weapon;').fetchall()
non_weapons = sl_con.execute("""
    SELECT armory_item.item_id
       FROM armory_item LEFT JOIN armory_weapon
       ON armory_item.item_id = armory_weapon.item_ptr_id
       WHERE armory_weapon.item_ptr_id IS NULL;
    """).fetchall()

print(f'Total Characters: {len(characters)}')
print(f'Clerics:          {len(clerics)}')
print(f'Fighters:         {len(fighters)}')
print(f'Mages:            {len(mages)}')
print(f'Necromancers:     {len(necromancers)}')
print(f'Thiefs:           {len(thiefs)}')
print()
print(f'Total Items:      {len(items)}')
print(f'Weapons:          {len(weapons)}')
print(f'Non-Weapons:      {len(non_weapons)}')


# Items per character
char_items = sl_con.execute("""
    SELECT character_id, count(id)
    FROM charactercreator_character_inventory
    GROUP BY character_id
    ;
    """).fetchall()
print('\nHow many items does each character have?')
print('Character : Items')
for i in range(20):
    print(f'{char_items[i][0]:9} : {char_items[i][1]}')


# Weapons per character
char_weapons = sl_con.execute("""
    SELECT character_id, COUNT(item_ptr_id)
    FROM charactercreator_character_inventory LEFT JOIN armory_weapon
    ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
    GROUP BY character_id;
    """).fetchall()
print('\nHow many weapons does each character have?')
print('Character : Weapons')
for i in range(20):
    print(f'{char_weapons[i][0]:9} : {char_weapons[i][1]}')


# Average items
mean_items = sl_con.execute("""
    SELECT
        AVG(count_id)
    FROM
        (
        SELECT COUNT(id) count_id
        FROM charactercreator_character_inventory
        GROUP BY character_id
        )
    """).fetchall()
print(f'\nAverage number of items per character: {mean_items[0][0]:.3f}')


# Average weapons
mean_items = sl_con.execute("""
    SELECT
        AVG(count_id)
    FROM
        (
        SELECT character_id, COUNT(item_ptr_id) count_id
        FROM charactercreator_character_inventory AS inventory
        LEFT JOIN armory_weapon AS weapons
        ON inventory.item_id = weapons.item_ptr_id
        GROUP BY character_id
        )
    """).fetchall()
print(f'\nAverage number of weapons per character: {mean_items[0][0]:.3f}')
print()

sl_con.close()
