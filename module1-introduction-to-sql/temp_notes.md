Use `sqlite3` to load and write queries to explore the data, and answer the
following questions:

- How many total Characters are there?
-- > How many total Characters are there?
# I cam up with 302
SELECT
	character_id
	,count(DISTINCT character_id) as CharacterCount
FROM charactercreator_character

- How many of each specific subclass?
Jonathan Dukes answer 
SELECT "cleric" as class_name, COUNT(DISTINCT character_ptr_id) as class_count
FROM charactercreator_cleric
UNION
SELECT "fighter" as class_name, COUNT(DISTINCT character_ptr_id) as class_count
FROM charactercreator_fighter
UNION
SELECT "mage" as class_name, COUNT(DISTINCT character_ptr_id) as class_count
FROM charactercreator_mage
UNION
SELECT "thief" as class_name, COUNT(DISTINCT character_ptr_id) as class_count
FROM charactercreator_thief
UNION
SELECT "necromancer" as class_name, COUNT(DISTINCT mage_ptr_id) as class_count
FROM charactercreator_necromancer


look at my screenshots see how ryan explained it. 

- How many total Items?
SELECT
	item_id	
	,count(item_id) as item_count
FROM armory_item

- How many of the Items are weapons?
# this kinda works but its kinda hacky. 
SELECT
  armory_item.item_id
  ,armory_weapon.item_ptr_id
  ,count(armory_item.item_id)
FROM armory_item
JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
-- WHERE armory_item.item_id <> armory_weapon.item_ptr_id

How many items are not weapons ?

SELECT 
	count(DISTINCT armory_item.item_id) - count(DISTINCT armory_weapon.item_ptr_id) as "Non Weapon"
	,count(DISTINCT armory_weapon.item_ptr_id) as "Weapon"
FROM 
	armory_weapon
	,armory_item



- How many Items does each character have? (Return first 20 rows)


- How many Weapons does each character have? (Return first 20 rows)


- On average, how many Items does each Character have?


- On average, how many Weapons does each character have?



# _________________
SELECT character.name as character_name, item.name as item_name
FROM charactercreator_character AS character,
charactercreator_character_inventory AS inventory,
armory_item AS item
WHERE character.character_id = inventory.character_id
AND inventory.item_id = item.item_id
LIMIT 20;

found this bad boy here. 


# Average number of weapons 
SELECT AVG(NoW)
FROM
(SELECT 
    character_id, COUNT(DISTINCT item_id) as NoW
FROM 
    charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20)

# wepon non weapon 
SELECT 
 sum(w.item_ptr_id is null) as non_weapon_count
 ,sum(w.item_ptr_id is not null) as weapon_count
FROM armory_item i
LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id


-- How many Weapons does each character have? (Return first 20 rows)
-- assume: also count 0 for char that don't have weapons
-- 302 rows (characters)
SELECT
  c.character_id
  ,c.name as char_name
  ,count(inv.item_id) as item_count
  ,count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
GROUP BY c.character_id -- row per what?
-- ORDER BY weapon_count DESC
-- LIMIT 20


# ! Here is another to try. 
Also have this one here . 
SELECT 
  character_id, count(distinct item_id)/ as ANI
FROM
  charactercreator_character_inventory
GROUP BY character_id