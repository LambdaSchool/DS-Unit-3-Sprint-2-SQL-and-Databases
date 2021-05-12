#!/usr/bin/env/ python

import psycopg2 as pg

dbname = 'hplkjeta'
user ='hplkjeta'
password='oZIHUw7MLlfv7STG_kigAzstwcYwUE2z'
host = 'stampy.db.elephantsql.com'

 
pg_conn = pg.connect(dbname=dbname, user=user,
                     password=password, host=host)

pg_curs = pg_conn.cursor()

surv_died_query = """ SELECT (
SELECT COUNT(*)
FROM titanic2 as t
WHERE t.survived = 1
) AS Survived,
(
SELECT COUNT(*)
FROM titanic2 as t
WHERE t.survived = 0
) AS Died; """

pclass_count_query = """SELECT (
SELECT COUNT(*)
FROM titanic2 as t
WHERE t.Pclass = 1
) AS pclass_is_1,
(
SELECT COUNT(*)
FROM titanic2 as t
WHERE t.Pclass = 2
) AS pclass_is_2,
(
SELECT COUNT(*)
FROM titanic2 as t
WHERE t.Pclass = 3
) AS pclass_is_3; """
