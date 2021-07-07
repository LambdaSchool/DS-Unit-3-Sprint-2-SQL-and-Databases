"""
CREATE TABLE "charactercreator_character" 
("character_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(30) NOT NULL, 
"level" integer NOT NULL, 
"exp" integer NOT NULL, 
"hp" integer NOT NULL, 
"strength" integer NOT NULL, 
"intelligence" integer NOT NULL, 
"dexterity" integer NOT NULL, 
"wisdom" integer NOT NULL)
"""

"""
CREATE TABLE "charactercreator_character_inventory" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"character_id" integer NOT NULL REFERENCES "charactercreator_character" ("character_id") DEFERRABLE INITIALLY DEFERRED, 
"item_id" integer NOT NULL REFERENCES "armory_item" ("item_id") DEFERRABLE INITIALLY DEFERRED)
"""
"""
CREATE TABLE "armory_item" 
("item_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(30) NOT NULL, 
"value" integer NOT NULL, 
"weight" integer NOT NULL)
"""

"""
CREATE TABLE "armory_weapon" 
("item_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "armory_item" ("item_id") DEFERRABLE INITIALLY DEFERRED, 
"power" integer NOT NULL)
"""


"""
CREATE TABLE "charactercreator_mage" 
("character_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "charactercreator_character" ("character_id") DEFERRABLE INITIALLY DEFERRED,
 "has_pet" bool NOT NULL, 
 "mana" integer NOT NULL)
 """
