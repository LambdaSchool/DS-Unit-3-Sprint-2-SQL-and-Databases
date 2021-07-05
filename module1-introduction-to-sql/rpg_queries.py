import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

# How many total Characters are there?
result_1 = cur.execute("SELECT COUNT(*) FROM charactercreator_character;").fetchall()[0][0]
print(f" How many total Characters are there? Answer: {result_1}")

# How many of each specific subclass?
result_2 = cur.execute("SELECT COUNT(*) FROM charactercreator_fighter;").fetchall()[0][0]
result_3 = cur.execute("SELECT COUNT(*) FROM charactercreator_mage;").fetchall()[0][0]
result_4 = cur.execute("SELECT COUNT(*) FROM charactercreator_cleric;").fetchall()[0][0]
result_5 = cur.execute("SELECT COUNT(*) FROM charactercreator_thief;").fetchall()[0][0]
result_6 = cur.execute("SELECT COUNT(*) FROM charactercreator_necromancer;").fetchall()[0][0]
print(f" How many of each specific subclass? fighter:{result_2}; mage:{result_3}; cleric:{result_4}; thief:{result_5}; necromancer:{result_6} ")

# How many total Items?
result_7 = cur.execute(" SELECT COUNT(*) FROM armory_item;").fetchall()[0][0]
print(f" How many total Items? Answer: {result_7}")

# How many of the Items are weapons? How many are not?
result_8 = cur.execute(" SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id == item_ptr_id; ").fetchall()[0][0]
print(f" How many of the Items are weapons? Answer: {result_8}")

###
