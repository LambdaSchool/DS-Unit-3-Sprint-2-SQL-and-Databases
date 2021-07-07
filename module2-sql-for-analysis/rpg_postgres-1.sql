--- Create `test` table
CREATE TABLE test (
    test_id SERIAL PRIMARY KEY,
    file VARCHAR(30),
    count INT,
    success BOOL
);

--- Insert data into `test` table
INSERT INTO 
    test (file, count, success)
VALUES
    ('deftools.py', 5, true);

--- Insert data into `test` table
SELECT
    *
FROM
    test


--- Get all rows from sqlite3 character table
SELECT
    *
FROM
    charactercreator_character;

--- Get all rows from postgres character table
SELECT
    *
FROM
    character;


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