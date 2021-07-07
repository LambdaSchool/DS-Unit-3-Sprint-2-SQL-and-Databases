--- SQLite

--- Use COUNT to get the count of characters
--- 302
SELECT COUNT(*) name
FROM charactercreator_character;

--- How many of each specific subclass?
--- For the Python, I can iterate through a list

--- cleric: 75
SELECT COUNT(*)
FROM charactercreator_cleric;

--- fighter: 68
SELECT COUNT(*)
FROM charactercreator_fighter;

--- mage: 108
SELECT COUNT(*)
FROM charactercreator_mage;

--- necromancer: 11
SELECT COUNT(*)
FROM charactercreator_necromancer;

--- thief: 51
SELECT COUNT(*)
FROM charactercreator_thief;

--- How many total Items?
--- 174
SELECT COUNT(*)
FROM armory_item;

--- How many of the Items are weapons? How many are not?
--- 37 are weapons
SELECT
    COUNT(*)
FROM 
    armory_item as ai, 
    armory_weapon as aw
WHERE 
    ai.item_id = aw.item_ptr_id; 

--- 137 are not weapons
SELECT
    COUNT(*) name
FROM 
    armory_item as ai
LEFT JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
WHERE item_ptr_id IS NULL; 


--- How many Items does each character have? (Return first 20 rows)
SELECT 
    COUNT(*) item_id
FROM
    charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;


--- How many Weapons does each character have? (Return first 20 rows)
SELECT
    COUNT(*) item_ptr_id
FROM
    charactercreator_character_inventory as inv
INNER JOIN armory_weapon as aw 
    ON inv.item_id = aw.item_ptr_id
GROUP BY inv.character_id
LIMIT 20;


--- On average, how many Items does each Character have?
--- 2.97
SELECT
    ROUND(AVG(item_count), 2)
FROM
    (SELECT 
        character_id, COUNT(item_id) item_count
    FROM
        charactercreator_character_inventory
    GROUP BY character_id);


--- On average, how many Weapons does each character have?
--- 0.67 average weapons per character
SELECT
    ROUND(AVG(weapon_count), 2)
FROM
    (SELECT 
        character_id, COUNT(item_ptr_id) weapon_count
    FROM
        charactercreator_character_inventory inv
    LEFT JOIN armory_weapon as aw
        ON inv.item_id = aw.item_ptr_id
    GROUP BY character_id);

