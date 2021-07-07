--- Create postgres table from sqlite3 table_info()
CREATE TABLE character (
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


--- Show the postgres tables
SELECT
    *
FROM pg_catalog.pg_tables
WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';


--- Example insert of one record
INSERT INTO character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES 