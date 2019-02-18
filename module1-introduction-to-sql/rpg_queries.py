#!/usr/bin/env python 3

import pandas as pd
import sqlite3

connection = sqlite3.connect('rpg_db.sqlite3')
character_inventory = pd.read_sql_query("SELECT * from charactercreator_character_inventory;", connection)
print(character_inventory.head())
print('There are', character_inventory.shape[0], 'total Characters.')

# from README.md on github, known character base classes are Fighter, Mage,
# Cleric, and Thief. Necromancer class appears to be subclass of Mage class.

necromancers = pd.read_sql_query("SELECT * from charactercreator_necromancer;",
                                 connection)
print('There are', necromancers.shape[0], 'Necromancers.')

char_items = pd.read_sql_query("SELECT * from armory_item;", connection)
print('\nThere are', char_items.shape[0], 'total Items.')

weapons = pd.read_sql_query("SELECT * from armory_weapon;", connection)
print(weapons.shape[0], 'are weapons.')
print(char_items.shape[0] - weapons.shape[0], 'are not weapons.\n')

