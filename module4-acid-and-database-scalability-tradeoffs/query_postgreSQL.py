import psycopg2 as pig
import pandas as pd
dbname = ''
user = ''
password = ''
host = ''
conn = pig.connect(dbname=dbname, user=user, password=password, host=host)
curse = conn.cursor()


survive_count = '''SELECT COUNT(*)
    FROM "public"."titanic_table"
    WHERE survived =1;'''
# Returns: 342

persons_in_class = '''SELECT COUNT(*)
    FROM "public"."titanic_table"
    GROUP BY pclass;'''
# Returns:  class 1: 216, class 2: 184, class 3: 487

survived_by_class = '''SELECT COUNT(*)
    FROM "public"."titanic_table"
    WHERE survived = 1
    GROUP BY pclass;'''
# Returns: class 1: 136, class 2: 87, class 3: 119

average_survive_age = '''SELECT AVG(age)
    FROM "public"."titanic_table"
    WHERE survived = 1;'''
# Returns: 0.28412280701754386e2 which equates to 28 was the
# average age to survive

average_died_age = '''SELECT AVG(age)
    FROM "public"."titanic_table"
    WHERE survived = 0;'''
# Returns: 0.301541284403669725e2 which equates to 30 as the
# average age to die

average_age_class = '''SELECT AVG(age)
    FROM "public"."titanic_table"
    GROUP BY pclass;'''
# Returns: class 1: 0.387916666666666667e2 or 38.7 years
# class 2: 0.298804347826086957e2 or 29.8 years
# class 3: 0.252032854209445585e2 or 25.2 years

average_fare_pclass = '''SELECT AVG(fare)
    FROM "public"."titanic_table"
    GROUP BY pclass;'''
# Returns: class1: 84.1546874999999
# class 2: 20.6621831521739
# class 3: 13.7077073921971

average_fare_survival = '''SELECT AVG(fare)
    FROM "public"."titanic_table"
    GROUP BY survived;'''
# Returns: died: 22.2085840366972
# survived: 48.3954076023392

average_sibling_spouse_pclass = '''SELECT AVG(spouse_sibling)
    FROM "public"."titanic_table"
    GROUP BY pclass;'''
# Returns: class 1: 0.41666666666666666667e0 spouses or siblings
# class 2: 0.62012320328542094456e0 spouses or siblings
# class 3: 0.40217391304347826087e0 spouses or siblings 

average_sibling_spouse_survival = '''SELECT AVG(spouse_sibling)
    FROM "public"."titanic_table"
    GROUP BY survived;'''
# Returns: died: 0.47368421052631578947e0
# survived: 0.5577981651376146789e0

average_parents_children_pclass = '''SELECT AVG(parents_children)
    FROM "public"."titanic_table"
    GROUP BY pclass;'''
# Returns: class 1: 0.35648148148148148148e0
# class 2: 0.39630390143737166324e0
# class 3: 0.38043478260869565217e0

average_parents_children_survival = '''SELECT AVG(parents_children)
    FROM "public"."titanic_table"
    GROUP BY survived;'''
# Returns: died: 0.46491228070175438596e0
# survived: 0.33211009174311926606e0

count_name = '''SELECT COUNT(DISTINCT name)
    FROM "public"."titanic_table";'''
# Returns 887 representing individual names 

all_entries = '''SELECT COUNT(*)
    FROM "public"."titanic_table"'''
# Returns 887 representing all entries in the data base.
# SO it is counting all names as unique