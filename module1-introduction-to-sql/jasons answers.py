import sqlite3 as lite

conn = lite.Connection("""rpg_db.sqlite3""")

curs = conn.cursor()

query = [
         """SELECT COUNT(*) FROM charactercreator_character""",
         """SELECT COUNT(*) FROM charactercreator_cleric""",
         """SELECT COUNT(*) FROM charactercreator_thief""",
         """SELECT COUNT(*) FROM charactercreator_fighter""",
         """SELECT COUNT(*) FROM charactercreator_mage""",
         """SELECT COUNT(*) FROM charactercreator_necromancer""",
         """SELECT COUNT(*) FROM charactercreator_character_inventory    """,
         """SELECT COUNT(*) FROM charactercreator_character_inventory
          WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)""",
         """SELECT COUNT(*) FROM charactercreator_character_inventory
          WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)""",
         """SELECT charactercreator_character.name,
          charactercreator_character.character_id, armory_item.name,
          armory_item.item_id FROM (armory_item
          LEFT JOIN charactercreator_character_inventory)
          LEFT JOIN charactercreator_character
          WHERE (charactercreator_character.character_id
          == charactercreator_character_inventory.character_id)
          AND (charactercreator_character_inventory.item_id
          == armory_item.item_id)""",
          """SELECT charactercreator_character.name,
           charactercreator_character.character_id,
           armory_weapon.item_ptr_id
           FROM (armory_weapon
           LEFT JOIN charactercreator_character_inventory)
           LEFT JOIN charactercreator_character
           WHERE (charactercreator_character.character_id
           == charactercreator_character_inventory.character_id)
           AND (charactercreator_character_inventory.item_id
           == armory_weapon.item_ptr_id)"""
           ]