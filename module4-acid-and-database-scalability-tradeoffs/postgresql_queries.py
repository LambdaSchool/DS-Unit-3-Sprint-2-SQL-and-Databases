import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)
cursor = conn.cursor()

# How many passengers survived, and how many died?
survivors = ("""
    SELECT COUNT(*)
    FROM titanic
    WHERE survived = 1
""")
deaths = ("""
    SELECT COUNT(*)
    FROM titanic
    WHERE survived = 0
""")
print(cursor.execute(survivors).fetchall() + " survived.")
print(cursor.execute(deaths).fetchall() + " died.")

# How many passengers were in each class?
class_query = ("""
    SELECT pclass, count(DISTINCT id)
    FROM titanic
    GROUP BY pclass
""")
class_result = cursor.execute(class_query).fetchall()

for each in result:
    if each[0] == 1:
        print(f'{each[1]} passengers were in first class.')
    elif each[0] == 2:
        print(f'{each[1]} passengers were in second class.')
    else:
        print(f'{each[1]} passengers were in third class.')

# How many passengers survived/died in each class?
class_surv_query = ("""
    SELECT pclass, COUNT(DISTINCT id)
    FROM titanic
    WHERE survived = 1
    GROUP BY pclass
""")
class_surv_result = cursor.execute(class_surv_query).fetchall()

class_died_query = ("""
    SELECT pclass, COUNT(DISTINCT id)
    FROM titanic
    WHERE survived = 0
    GROUP BY pclass
""")
class_died_result = cursor.execute(class_died_query).fetchall()

for each in class_died_result:
    if each[0] == 1:
        dead_first = each[1]
    elif each[0] == 2:
        dead_second = each[1]
    else:
        dead_third = each[1]

for each in class_surv_result:
    if each[0] == 1:
        print(f'In first class {each[1]} passengers survived and
              {dead_first} died.')
    elif each[0] == 2:
        print(f'In first class {each[1]} passengers survived and
              {dead_second} died.')
    else:
        print(f'In first class {each[1]} passengers survived and
              {dead_third} died.')

# What was the average age of survivors vs. nonsurvivors?
age_query = ("""
    SELECT survived, AVG(age)
    FROM titanic
    GROUP BY survived
""")
age_result = cursor.execute(age_query).fetchall()

for each in age_result:
    if each[0] == 1:
        print(f'The average age of survivors is {each[1]}')
    else:
        print(f'The average age of the deceased is {each[1]}')

# What was the average age of each passenger class?
class_age_query = ("""
    SELECT pclass, AVG(age)
    FROM titanic
    GROUP BY pclass
""")
class_age_result = cursor.execute(class_age_query).fetchall()

for each in class_age_result:
    if each[0] == 1:
        print(f'The average age of first class passengers is {each[1]}')
    elif each[0] == 2:
        print(f'The average age of second class passengers is {each[1]}')
    else:
        print(f'The average age of third class passengers is {each[1]}')

# What was the average fare by passenger class? By survival?
class_fare_query = ("""
    SELECT pclass, AVG(fare)
    FROM titanic
    GROUP BY pclass
""")
class_fare_result = cursor.execute(class_fare_query).fetchall()

surv_fare_query = ("""
    SELECT survived, AVG(fare)
    FROM titanic
    GROUP BY survived
""")
surv_fare_result = cursor.execute(surv_fare_query).fetchall()

for each in class_fare_result:
    if each[0] == 1:
        print(f'The average fare for first class passengers is {each[1]}')
    elif each[0] == 2:
        print(f'The average fare for second class passengers is {each[1]}')
    else:
        print(f'The average fare for third class passengers is {each[1]}')

for each in surv_fare_result:
    if each[0] == 1:
        print(f'The average fare for survivors is {each[1]}')
    else:
        print(f'The average fare for the deceased is {each[1]}')

# How many siblings/spouses aboard on average, by passenger class? By survival?
class_sib_query = ("""
    SELECT pclass, AVG(siblings_spouses)
    FROM titanic
    GROUP BY pclass
""")
class_sib_result = cursor.execute(class_sib_query).fetchall()

surv_sib_query = ("""
    SELECT survived, AVG(siblings_spouses)
    FROM titanic
    GROUP BY survived
""")
surv_sib_result = cursor.execute(surv_sib_query).fetchall()

for each in class_sib_result:
    if each[0] == 1:
        print(f'The average number of siblings and spouses for survivors
              is {each[1]}')
    else:
        print(f'The average number of siblings and spouses for the deceased
              is {each[1]}')

for each in surv_sib_result:
    if each[0] == 1:
        print(f'The average number of siblings and spouses for first class
              passengers is {each[1]}')
    elif each[0] == 2:
        print(f'The average number of siblings and spouses for second class
              passengers is {each[1]}')
    else:
        print(f'The average number of siblings and spouses for third class
              passengers is {each[1]}')

# How many parents/children aboard on average, by passenger class? By survival?
class_parent_query = ("""
    SELECT pclass, AVG(parents_children)
    FROM titanic
    GROUP BY pclass
""")
class_parent_result = cursor.execute(class_parent_query).fetchall()

surv_parent_query = ("""
    SELECT survived, AVG(parents_children)
    FROM titanic
    GROUP BY survived
""")
surv_parent_result = cursor.execute(surv_parent_query).fetchall()

for each in class_parent_result:
    if each[0] == 1:
        print(f'The average number of parents and children for survivors
              is {each[1]}')
    else:
        print(f'The average number of parents and children for the deceased
              is {each[1]}')

for each in surv_parent_result:
    if each[0] == 1:
        print(f'The average number of parents and children for first class
              passengers is {each[1]}')
    elif each[0] == 2:
        print(f'The average number of parents and children for second class
              passengers is {each[1]}')
    else:
        print(f'The average number of parents and children for third class
              passengers is {each[1]}')

# Do any passengers have the same name?
unique_query = ("""
    SELECT name, COUNT(*)
    FROM titanic
    GROUP BY name
""")
unique_result = cursor.execute(unique_query).fetchall()

print("The following passengers have the same name:")
for each in unique_result:
    if each[1] > 1:
        print(f'     {each[0]}')
    else:
        pass
