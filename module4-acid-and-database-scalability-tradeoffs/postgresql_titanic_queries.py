import warnings
import psycopg2 as pg
import os
from dotenv import load_dotenv
warnings.simplefilter(action='ignore', category=UserWarning)

load_dotenv()

DB_NAME = os.getenv("PG_NAME")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_HOST = os.getenv("PG_HOST")

conn = pg.connect(dbname=DB_NAME, user=DB_USER,
                  password=DB_PASSWORD, host=DB_HOST)
curs = conn.cursor()

# passengers survived and died
query = """
SELECT COUNT(*) FROM titanic
GROUP BY survived
ORDER BY survived
"""
curs.execute(query)
survived = curs.fetchall()
print(f'Passengers who survived: {survived[1][0]}\n'
      f'Passengers who died: {survived[0][0]}\n')

# passengers in each class
query = """
SELECT COUNT(*) FROM titanic
GROUP BY passenger_class
ORDER BY passenger_class
"""
curs.execute(query)
print(f'First Class Passengers: {curs.fetchone()[0]}\n'
      f'Second Class Passengers: {curs.fetchone()[0]}\n'
      f'Third Class Passengers: {curs.fetchone()[0]}\n')

# survived/died by class
query = """
SELECT COUNT(passenger_class)
FROM titanic
GROUP BY survived, passenger_class
ORDER BY survived, passenger_class
"""
curs.execute(query)
survived = curs.fetchall()
print(f'First Class Passengers Survived/Died: '
      f'{survived[3][0]}/{survived[0][0]}\n'
      f'Second Class Passengers Survived/Died: '
      f'{survived[4][0]}/{survived[1][0]}\n'
      f'Third Class Passengers Survived/Died: '
      f'{survived[5][0]}/{survived[2][0]}\n')

# average age of survivors vs died
query = """
SELECT AVG(age), survived 
FROM 
(SELECT age, survived 
FROM titanic) as avg 
GROUP BY survived
"""
curs.execute(query)
age = curs.fetchall()
print(f'Average Age Survivors: {round(age[1][0])}\n'
      f'Average Age Died: {round(age[0][0])}\n')

# average age of each class
query = """
SELECT AVG(age), passenger_class
FROM
(SELECT age, passenger_class
FROM titanic) as avg
GROUP BY passenger_class
ORDER BY passenger_class
"""
curs.execute(query)
age_by_pclass = curs.fetchall()
print(f'Average Age By Class:\n'
      f'Class: {age_by_pclass[0][1]} == Age: {round(age_by_pclass[0][0])}\n'
      f'Class: {age_by_pclass[1][1]} == Age: {round(age_by_pclass[1][0])}\n'
      f'Class: {age_by_pclass[2][1]} == Age: {round(age_by_pclass[2][0])}\n')

# average fare by class
query = """
SELECT AVG(fare), passenger_class
FROM
(SELECT fare, passenger_class
FROM titanic) as avg
GROUP BY passenger_class
ORDER BY passenger_class
"""
curs.execute(query)
fare_by_class = curs.fetchall()
print(f'Average Fare By Class:\n'
      f'Class: {fare_by_class[0][1]} == '
      f'Fare: {round(fare_by_class[0][0], 2)}\n'
      f'Class: {fare_by_class[1][1]} == '
      f'are: {round(fare_by_class[1][0], 2)}\n'
      f'Class: {fare_by_class[2][1]} == '
      f'Fare: {round(fare_by_class[2][0], 2)}\n')

# average fare by survival
query = """
SELECT AVG(fare), survived
FROM
(SELECT fare, survived
FROM titanic) as avg
GROUP BY survived
ORDER BY survived
"""
curs.execute(query)
fare_by_survival = curs.fetchall()
print(f'Average Fare By Survival:\n'
      f'Avg. Fare Of Fatalities: {round(fare_by_survival[0][0], 2)}\n'
      f'Avg. Fare Of Survivors: {round(fare_by_survival[1][0], 2)}\n')

# average siblings/spouses, by class
query = """
SELECT AVG(siblings_and_spouses), passenger_class
FROM
(SELECT siblings_and_spouses, passenger_class
FROM titanic) as avg
GROUP BY passenger_class
ORDER BY passenger_class
"""
curs.execute(query)
sibs_spouses_by_class = curs.fetchall()
print(f'Average # Of Siblings/Spouses By Class:\n'
      f'Class: {sibs_spouses_by_class[0][1]} == '
      f'Family: {round(sibs_spouses_by_class[0][0], 2)}\n'
      f'Class: {sibs_spouses_by_class[1][1]} == '
      f'Family: {round(sibs_spouses_by_class[1][0], 2)}\n'
      f'Class: {sibs_spouses_by_class[2][1]} == '
      f'Family: {round(sibs_spouses_by_class[2][0], 2)}\n')

# average # Of Siblings/Spouses By Survival
query = """
SELECT AVG(siblings_and_spouses), survived
FROM
(SELECT siblings_and_spouses, survived
FROM titanic) as avg
GROUP BY survived
ORDER BY survived
"""
curs.execute(query)
sibs_spouses_by_survival = curs.fetchall()
print(f'Average # Of Siblings/Spouses By Survival:\n'
      f'Avg. Family Of Fatalities: '
      f'{round(sibs_spouses_by_survival[0][0], 2)}\n'
      f'Avg. Family Of Survivors: '
      f'{round(sibs_spouses_by_survival[1][0], 2)}\n')

# average parents/children, by class
query = """
SELECT AVG(parents_and_children), passenger_class
FROM
(SELECT parents_and_children, passenger_class
FROM titanic) as avg
GROUP BY passenger_class
ORDER BY passenger_class
"""
curs.execute(query)
parents_kids_by_class = curs.fetchall()
print(f'Average # Of Parents/Children By Class:\n'
      f'Class: {parents_kids_by_class[0][1]} == '
      f'Family: {round(parents_kids_by_class[0][0], 2)}\n'
      f'Class: {parents_kids_by_class[1][1]} == '
      f'Family: {round(parents_kids_by_class[1][0], 2)}\n'
      f'Class: {parents_kids_by_class[2][1]} == '
      f'Family: {round(parents_kids_by_class[2][0], 2)}\n')

# average # Of parents/children By Survival
query = """
SELECT AVG(parents_and_children), survived
FROM
(SELECT parents_and_children, survived
FROM titanic) as avg
GROUP BY survived
ORDER BY survived
"""
curs.execute(query)
parents_kids_by_survival = curs.fetchall()
print(f'Average # Of Parents/Children By Survival:\n'
      f'Avg. Family Of Fatalities: '
      f'{round(parents_kids_by_survival[0][0], 2)}\n'
      f'Avg. Family Of Survivors: '
      f'{round(parents_kids_by_survival[1][0], 2)}\n')

# duplicate names
query = """
SELECT name, COUNT(*)
FROM titanic
GROUP BY name
HAVING COUNT(*) > 1
"""
curs.execute(query)
duplicates = curs.fetchall()
print(f'Duplicate Names: {duplicates}')
