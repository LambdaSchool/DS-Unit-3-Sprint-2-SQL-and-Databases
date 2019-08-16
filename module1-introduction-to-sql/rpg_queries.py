import sqlite3

# -----------------Q1 How many total Characters are there?---------------------
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = '''SELECT COUNT(character_id)
FROM charactercreator_character;'''

curs.execute(query)
print("How many total Characters are there?")
print("Answer: Total Characters =", curs.fetchall()[0][0])
curs.close()

# ---------------- Q2 How many of each specific subclass? ---------------------
# mage class
curs = conn.cursor()

query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;'''

curs.execute(query)
print("\nHow many of each specific subclass?")
print("Answer: \nMage = ", curs.fetchall()[0][0])
curs.close()

# thief class
curs = conn.cursor()
query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;'''

curs.execute(query)
print("Thief = ", curs.fetchall()[0][0])
curs.close()

# Cleric class
curs = conn.cursor()
query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric;'''

curs.execute(query)
print("Cleric = ", curs.fetchall()[0][0])
curs.close()

# fighter class
curs = conn.cursor()
query = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;'''

curs.execute(query)
print("Fighter = ", curs.fetchall()[0][0])
curs.close()

# ---------------- Q3 How many total Items? ----------------------
curs = conn.cursor()

query = '''SELECT COUNT(item_id)
FROM armory_item;'''

curs.execute(query)
print("\nHow many total Items?")
print("Answer: ", curs.fetchall()[0][0])
curs.close()

# ------- Q4 How many of the Items are weapons? How many are not? -------
curs = conn.cursor()

query = '''SELECT COUNT(item_ptr_id)
FROM armory_weapon;'''

curs.execute(query)
print("\nHow many of the Items are weapons? How many are not?")
print("Answer: ", curs.fetchall()[0][0], 'weapons and 137 are not')
curs.close()

# ---- Q5 How many Items does each character have? (Return first 20 rows) -----
curs = conn.cursor()

query = '''SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id;'''

curs.execute(query)
print("\nHow many Items does each character have? (Return first 20 rows)")
print("Answer: ", curs.fetchmany(20))
curs.close()

# --- Q6 How many Weapons does each character have? (Return first 20 rows) ----
curs = conn.cursor()

query = '''SELECT COUNT(item_id)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon AS aw
ON item_id = aw.item_ptr_id
GROUP BY character_id;'''

curs.execute(query)
print("\nHow many Weapons does each character have? (Return first 20 rows)")
print("Answer: ", curs.fetchmany(20))
curs.close()

# --- Q7 On average, how many Items does each Character have? ----
curs = conn.cursor()

query = '''SELECT AVG(item_count)
FROM (SELECT COUNT(item_id) as item_count
FROM charactercreator_character_inventory 
GROUP BY character_id);'''

curs.execute(query)
print("\nOn average, how many Items does each Character have?")
print("Answer: ", curs.fetchall()[0][0])
curs.close()

# --- Q8 On average, how many Weapons does each character have? ----
curs = conn.cursor()

query = '''SELECT AVG(item_count)
FROM (SELECT COUNT(item_id) AS item_count 
FROM charactercreator_character_inventory 
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id);'''

curs.execute(query)
print("\nOn average, how many Weapons does each character have?")
print("Answer: ", curs.fetchall()[0][0])
curs.close()
conn.commit()
