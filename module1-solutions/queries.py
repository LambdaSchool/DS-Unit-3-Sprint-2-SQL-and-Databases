

TOTAL_CHARACTERS = "select count(*) from charactercreator_character"

TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item"

WEAPONS = "SELECT COUNT(*) FROM armory_weapon"

NON_WEAPONS = "select COUNT(*) from armory_item ai LEFT JOIN armory_weapon aw ON ai.item_id = aw.item_ptr_id WHERE item_ptr_id IS NULL"

CHARACTER_ITEMS = "SELECT COUNT(item_id) from charactercreator_character_inventory GROUP BY character_id limit 20"

CHARACTER_WEAPONS = "SELECT COUNT(item_id) FROM charactercreator_character_inventory cci JOIN armory_weapon aw on cci.item_id = aw.item_ptr_id GROUP BY character_id"

AVG_CHARACTER_ITEMS = "SELECT AVG(item_count) FROM ( \
SELECT count(item_id) item_count from charactercreator_character_inventory GROUP BY character_id)"

AVG_CHARACTER_WEAPONS = "SELECT AVG(item_count) FROM (SELECT COUNT(item_id) item_count \
						 FROM charactercreator_character_inventory cci JOIN armory_weapon aw on cci.item_id = aw.item_ptr_id GROUP BY character_id)"


NUMBER_ROWS = 'SELECT COUNT(*) FROM review'

NUMBER_OF_USERS = 'SELECT COUNT(*) FROM review where nature >= 100 and shopping >= 100'

