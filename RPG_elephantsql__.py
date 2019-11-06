# -*- coding: utf-8 -*-
"""elephantsql_lecture.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cuKM-HmwboeLzWvuYZN-gyT3U_m4QNa_
"""

pip install psycopg2-binary

import psycopg2

dbname = 'username' #same than user
user = 'username' #same than dbname
password = 'pass' 
host = 'host' #from SERVER type

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute('SELECT * FROM test_table;')

#fetchall needs to be done in a separate cell
pg_curs.fetchall()

"""# charactercreator_character"""

wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

ls -alh

mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character')
pg_curs.fetchall()

sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character')
pg_curs.fetchall()

characters = sl_curs.execute('SELECT * FROM charactercreator_character;')
pg_curs.fetchall()

characters

len(characters)

characters[-1]

characters[0]

sl_curs.execute('PRAGMA table_info(charactercreator_character);')
pg_curs.fetchall()

create_character_table = """
  CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
  """

pg_curs.execute(create_character_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

str(characters[0][1:])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence,dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ';'
print(example_insert)

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence,dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  # print(insert_character)
  pg_curs.execute(insert_character)

insert_character


pg_curs.execute ('SELECT * FROM charactercreator_character;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

characters[0]

pg_characters[0]

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

pg_curs.close()
pg_conn.commit()

"""# armory_item"""

sl_curs.execute('SELECT COUNT(*) FROM armory_item')
pg_curs.fetchall()

items = sl_curs.execute('SELECT * FROM armory_item;')
pg_curs.fetchall()

items

sl_curs.execute('PRAGMA table_info(armory_item);')
pg_curs.fetchall()

create_item_table = """
  CREATE TABLE armory_item (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    value INT,
    weight INT
  );
  """

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_item_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)

pg_curs.fetchall()

item_insert = """
INSERT INTO armory_item
(name, value, weight)
VALUES """ + str(items[0][1:]) + ';'

print(item_insert)

for item in items:
  insert_item = """
    INSERT INTO armory_item
    (name, value, weight)
    VALUES """ + str(item[1:]) + ';'
  pg_curs4.execute(insert_item)

items

insert_item

pg_curs.execute ('SELECT * FROM armory_item;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM armory_item;')
pg_items = pg_curs.fetchall()

items[0]

pg_items[0]

for item, pg_item in zip(items, pg_items):
    assert item == pg_item

pg_curs.close()
pg_conn.commit()

"""# armory_weapon"""

sl_curs.execute('SELECT COUNT(*) FROM armory_weapon')
pg_curs.fetchall()

weapons = sl_curs.execute('SELECT * FROM armory_weapon;')
pg_curs.fetchall()

weapons

sl_curs.execute('PRAGMA table_info(armory_weapon);')
pg_curs.fetchall()

create_weapons_table = """
  CREATE TABLE armory_weapon(
    item_ptr_id INT NOT NULL,
    power INT NOT NULL,
    FOREIGN KEY(item_ptr_id) REFERENCES armory_item(item_id),
	  PRIMARY KEY(item_ptr_id)
  );
  """

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_weapons_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

weapon_insert = """
INSERT INTO armory_weapon
(item_ptr_id, power)
VALUES """ + str(weapons[0]) + ';'

print(weapon_insert)

weapons[0][0:]

for weapon in weapons:
  insert_weapon = """
    INSERT INTO armory_weapon
    (item_ptr_id, power)
    VALUES """ + str(weapon[0:]) + ';'
  pg_curs.execute(insert_weapon)

insert_weapon

pg_curs.execute ('SELECT * FROM armory_weapon;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM armory_weapon;')
pg_weapons = pg_curs.fetchall()

weapons[0]

pg_weapons[0]

for weapon, pg_weapon in zip(weapons, pg_weapons):
    assert weapon == pg_weapon

pg_curs.close()
pg_conn.commit()

"""# charactercreator_character_inventory"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character_inventory')
pg_curs.fetchall()

ids = sl_curs.execute('SELECT * FROM charactercreator_character_inventory;')
pg_curs.fetchall()

ids

sl_curs.execute('PRAGMA table_info(charactercreator_character_inventory);')
pg_curs.fetchall()

create_ids_table = """
  CREATE TABLE charactercreator_character_inventory (
	id	SERIAL PRIMARY KEY,
	character_id	INT NOT NULL,
	item_id	INT NOT NULL,
	FOREIGN KEY(character_id) REFERENCES charactercreator_character(character_id),
	FOREIGN KEY(item_id) REFERENCES armory_item(item_id)
);
  """

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_ids_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

id_insert = """
INSERT INTO charactercreator_character_inventory
(character_id, item_id)
VALUES """ + str(ids[0][1:]) + ';'

print(id_insert)

ids[10][1:]

for identification in ids:
  insert_id = """
    INSERT INTO charactercreator_character_inventory
    (character_id, item_id)
    VALUES """ + str(identification[1:]) + ';'
  pg_curs.execute(insert_id)
  #print(insert_id)

insert_id

pg_curs.execute ('SELECT * FROM charactercreator_character_inventory;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character_inventory;')
pg_ids = pg_curs.fetchall()

ids[0]

pg_ids[0]

for identification, pg_identification in zip(ids, pg_ids):
    assert identification == pg_identification

pg_curs.close()
pg_conn.commit()

"""# charactercreator_mage"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_mage')
pg_curs.fetchall()

mages = sl_curs.execute('SELECT * FROM charactercreator_mage;')
pg_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_mage);')
pg_curs.fetchall()

create_mages_table = """
  CREATE TABLE charactercreator_mage (
	character_ptr_id	INT NOT NULL,
	has_pet	INT NOT NULL,
	mana	INT NOT NULL,
	FOREIGN KEY(character_ptr_id) REFERENCES charactercreator_character(character_id),
	PRIMARY KEY(character_ptr_id)
);
  """

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_mages_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

mage_insert = """
INSERT INTO charactercreator_mage
(character_ptr_id, has_pet, mana)
VALUES """ + str(mages[0]) + ';'

print(mage_insert)

for mage in mages:
  insert_mage = """
    INSERT INTO  charactercreator_mage
    (character_ptr_id, has_pet, mana)
    VALUES """ + str(mage[0:]) + ';'
  pg_curs.execute(insert_mage)

insert_mage

pg_curs.execute ('SELECT * FROM charactercreator_mage;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_mage;')
pg_mages = pg_curs.fetchall()

mages[0]

pg_mages[0]

for mage, pg_mage in zip(mages, pg_mages):
    assert mage == pg_mage

pg_curs.close()
pg_conn.commit()

"""# charactercreator_thief"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_thief')
pg_curs.fetchall()

thieves = sl_curs.execute('SELECT * FROM charactercreator_thief')
pg_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_thief);')
pg_curs.fetchall()

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

create_thieves_table = """
  CREATE TABLE charactercreator_thief (
	character_ptr_id	INT NOT NULL,
	is_sneaking	INT NOT NULL,
	energy	INT NOT NULL,
	FOREIGN KEY(character_ptr_id) REFERENCES charactercreator_character(character_id),
	PRIMARY KEY(character_ptr_id)
);
"""

pg_curs.execute(create_thieves_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

thieves[0]

thief_insert = """
INSERT INTO charactercreator_thief
(character_ptr_id, is_sneaking, energy)
VALUES """ + str(thieves[0]) + ';'

print(thief_insert)

for thief in thieves:
  insert_thief = """
    INSERT INTO  charactercreator_thief
    (character_ptr_id, is_sneaking, energy)
    VALUES """ + str(thief[0:]) + ';'
  pg_curs.execute(insert_thief)

insert_thief

pg_curs.execute ('SELECT * FROM charactercreator_thief;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_thief;')
pg_thieves = pg_curs.fetchall()

thieves[0]

pg_thieves[0]

for thief, pg_thief in zip(thieves, pg_thieves):
    assert thief == pg_thief

pg_curs.close()
pg_conn.commit()

"""# charactercreator_cleric"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_cleric')
pg_curs.fetchall()

clerics = sl_curs.execute('SELECT * FROM charactercreator_cleric')
pg_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_cleric);')
pg_curs.fetchall()

create_clerics_table = """
  CREATE TABLE charactercreator_cleric (
	character_ptr_id	INT NOT NULL,
	using_shield	INT NOT NULL,
	mana	INT NOT NULL,
	FOREIGN KEY(character_ptr_id) REFERENCES charactercreator_character(character_id),
	PRIMARY KEY(character_ptr_id)
);
"""

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_clerics_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

cleric_insert = """
INSERT INTO charactercreator_cleric
(character_ptr_id, using_shield, mana)
VALUES """ + str(clerics[0]) + ';'

print(cleric_insert)

for cleric in clerics:
  insert_cleric = """
    INSERT INTO  charactercreator_cleric
    (character_ptr_id, using_shield, mana)
    VALUES """ + str(cleric[0:]) + ';'
  pg_curs.execute(insert_cleric)

insert_cleric

pg_curs.execute ('SELECT * FROM charactercreator_cleric;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_cleric;')
pg_clerics = pg_curs.fetchall()

clerics[0]

pg_clerics[0]

for cleric, pg_cleric in zip(clerics, pg_clerics):
    assert cleric == pg_cleric

pg_curs.close()
pg_conn.commit()

"""# charactercreator_fighter"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_fighter')
pg_curs.fetchall()

fighters = sl_curs.execute('SELECT * FROM charactercreator_fighter')
pg_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_fighter);')
pg_curs.fetchall()

create_fighters_table = """
  CREATE TABLE charactercreator_fighter (
	character_ptr_id	INT NOT NULL,
	using_shield	INT NOT NULL,
	rage	INT NOT NULL,
	FOREIGN KEY(character_ptr_id) REFERENCES charactercreator_character(character_id),
	PRIMARY KEY(character_ptr_id)
);
"""

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_fighters_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

fighter_insert = """
INSERT INTO charactercreator_fighter
(character_ptr_id, using_shield, rage)
VALUES """ + str(fighters[0]) + ';'

print(fighter_insert)

for fighter in fighters:
  insert_fighter = """
    INSERT INTO  charactercreator_fighter
    (character_ptr_id, using_shield, rage)
    VALUES """ + str(fighter[0:]) + ';'
  pg_curs.execute(insert_fighter)

insert_fighter

pg_curs.execute ('SELECT * FROM charactercreator_fighter;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_fighter;')
pg_fighters = pg_curs.fetchall()

fighters[0]

pg_fighters[0]

for fighter, pg_fighter in zip(fighters, pg_fighters):
    assert fighter == pg_fighter

pg_curs.close()
pg_conn.commit()

"""# charactercreator_necromancer"""

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_necromancer')
pg_curs.fetchall()

nmcs = sl_curs.execute('SELECT * FROM charactercreator_necromancer')
pg_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_necromancer);')
pg_curs.fetchall()

create_nmcs_table = """
  CREATE TABLE charactercreator_necromancer (
	mage_ptr_id	INT NOT NULL,
	talisman_charged	INT NOT NULL,
	FOREIGN KEY(mage_ptr_id) REFERENCES charactercreator_mage(character_ptr_id),
	PRIMARY KEY(mage_ptr_id)
);
"""

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()

pg_curs.execute(create_nmcs_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

nmc_insert = """
INSERT INTO charactercreator_necromancer
(mage_ptr_id, talisman_charged)
VALUES """ + str(nmcs[0]) + ';'

print(nmc_insert)

for nmc in nmcs:
  insert_nmc = """
    INSERT INTO  charactercreator_necromancer
    (mage_ptr_id, talisman_charged)
    VALUES """ + str(nmc[0:]) + ';'
  pg_curs.execute(insert_nmc)

insert_nmc

pg_curs.execute ('SELECT * FROM charactercreator_necromancer;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_necromancer;')
pg_nmcs = pg_curs.fetchall()

nmcs[0]

pg_nmcs[0]

for nmc, pg_nmc in zip(nmcs, pg_nmcs):
    assert nmc == pg_nmc

pg_curs.close()
pg_conn.commit()