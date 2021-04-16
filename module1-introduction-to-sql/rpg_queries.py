import sqlite3

conn = sqlite3.connect('rgb_data.db')

# return the number of characters
query1 = "SELECT COUNT (character_id) FROM  charactercreator_character;"

query2 = """SELECT  (
                SELECT COUNT(character_ptr_id)
                FROM   charactercreator_cleric
                ) AS cleric_players,
                (
                SELECT COUNT(character_ptr_id)
                FROM   charactercreator_fighter
                ) AS fighter_players,
                (
                SELECT COUNT(character_ptr_id)
                FROM   charactercreator_mage
                ) AS mage_players,
                (
                SELECT COUNT(character_ptr_id)
                FROM charactercreator_thief
                ) AS thief_players """


curs = conn.cursor()
curs.execute(query)
curs.close()
conn.commit()
