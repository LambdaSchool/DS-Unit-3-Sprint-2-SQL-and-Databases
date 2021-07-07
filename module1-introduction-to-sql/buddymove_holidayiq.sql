-- SQLite

-- --- Count how many rows you have - it should be 249!
-- SELECT COUNT(*)
-- FROM review;


-- --- Users who reviewed at least 100 in `Nature` and `Shopping` categories?
-- SELECT COUNT(*)
-- FROM review
-- WHERE
--     nature > 100
-- AND shopping > 100;


--- Average number of reviews for each category
SELECT
    AVG(sports) avg_sports,
    AVG(religious) avg_religious,
    AVG(nature) avg_nature,
    AVG(theatre) avg_theatre,
    AVG(shopping) avg_shopping,
    AVG(picnic) avg_picnic
FROM review;