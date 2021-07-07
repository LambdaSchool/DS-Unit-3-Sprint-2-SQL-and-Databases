import sqlite3

# Database
conn = sqlite3.connect('rpg_db.sqlite3')

# Search through database
curs = conn.cursor()

# 1. How many total characters are there?

# Find what you're searching for
query = 'SELECT COUNT(*) FROM charactercreator_character;'

# Save the search to result
result = curs.execute(query)

# Get the row count of the result
print(f'Total characters: {result.fetchone()[0]}')

# 2. How many of each specific subclass?

def subclass(profession):

    query = 'SELECT COUNT(*) FROM charactercreator_' + profession + ';'

    result = curs.execute(query)

    print(f'Total sub-class of {profession}: {result.fetchone()[0]}')

subclass('mage')
subclass('thief')
subclass('cleric')
subclass('fighter')

# 3. How many total items?

query = 'SELECT COUNT(*) FROM armory_item;'

result = curs.execute(query)

print(f'Total items: {result.fetchone()[0]}')

# 4. How many of the items are weapons? How many are not?

query = 'SELECT COUNT(*) FROM armory_weapon;'
result = curs.execute(query)

print(f'Total weapon count: {result.fetchone()[0]}')

query = 'SELECT COUNT(aw.item_ptr_id) FROM armory_item AS ai, armory_weapon AS aw WHERE ai.item_id != aw.item_ptr_id;'

result = curs.execute(query)

print(f'Total non-weapon count: {result.fetchone()[0]}')

# 5. How many items does each character have? Return the 1st 20

query = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'

result = curs.execute(query)

print(f'Total items of the 1st 20 chars: {result.fetchall()}')

# 6. How many Weapons does each character have? Reutrn the 1st 20
query = 'SELECT cci.character_id, COUNT(aw.item_ptr_id) FROM armory_item AS ai, armory_weapon AS aw, charactercreator_character_inventory AS cci WHERE cci.item_id = ai.item_id AND ai.item_id = aw.item_ptr_id GROUP BY cci.character_id LIMIT 20;'

result = curs.execute(query)

print(f'Total weapons per character: {result.fetchall()}')

# 7. On average, how many items does each character have?

query = 'SELECT AVG(ct) FROM (SELECT COUNT(item_id) AS ct FROM charactercreator_character_inventory GROUP BY character_id);'

result = curs.execute(query)

print(f'Avg items per character: {result.fetchone()[0]}')

# 8. On average, how many weapons does each character have?

query = 'SELECT AVG(ct) FROM (SELECT COUNT(aw.item_ptr_id) as ct FROM armory_item AS ai, armory_weapon AS aw, charactercreator_character_inventory AS cci WHERE cci.item_id = ai.item_id AND ai.item_id = aw.item_ptr_id GROUP BY cci.character_id);'

result = curs.execute(query)

print(f'Avg weapons per character: {result.fetchone()[0]}')
