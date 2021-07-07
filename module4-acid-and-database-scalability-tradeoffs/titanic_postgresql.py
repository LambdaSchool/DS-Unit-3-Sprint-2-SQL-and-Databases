# ./usr/bin/env python
" Querying the RPG dataset in PostgreSQL"
from dotenv import load_dotenv
import os
import psycopg2

"""
Terminal printout (for reference)

Survived? : Number
No        : 545
Yes       : 342

Class : Survivors
    1 : 136
    2 : 87
    3 : 119

Survived? : Average Age
No        : 30.14
Yes       : 28.41

Class : Average Age
    1 : 38.79
    2 : 29.87
    3 : 25.19

Class : Average Fare
    1 : 84.15
    2 : 20.66
    3 : 13.71

Survived? : Average Fare
No        : 22.21
Yes       : 48.40

Class : Siblings/Spouses Aboard
    1 : 0.42
    2 : 0.40
    3 : 0.62

Survived? : Siblings/Spouses Aboard
No        : 0.56
Yes       : 0.47

Class : Parents/Children Aboard
    1 : 0.36
    2 : 0.38
    3 : 0.40

Survived? : Parents/Children Aboard
No        : 0.33
Yes       : 0.46

Do any passengers have the same name?
No


"""

# Get secret credentials
load_dotenv()
ElephantSQL_URL = os.getenv("ElephantSQL_URL")

# Connect to database
conn = psycopg2.connect(ElephantSQL_URL)
cur = conn.cursor()

# How many passengers survived, and how many died?
cur.execute("""
SELECT "Survived", COUNT(*)
FROM passengers
GROUP By "Survived"
""")
print()
print('Survived? : Number')
for survived, count in cur.fetchall():
    if survived:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'{ans:9} : {count}')

# How many passengers survived/died within each class?
cur.execute("""
SELECT "Pclass", COUNT(*)
FROM passengers
WHERE "Survived" = 1
GROUP By "Pclass"
""")
print()
print('Class : Survivors')
for pclass, count in cur.fetchall():
    print(f'{pclass:5} : {count}')

# What was the average age of survivors vs nonsurvivors?
cur.execute("""
SELECT "Survived", AVG("Age")
FROM passengers
GROUP By "Survived"
""")
print()
print('Survived? : Average Age')
for survived, age in cur.fetchall():
    if survived:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'{ans:9} : {age:.2f}')

# What was the average age of each passenger class?
cur.execute("""
SELECT "Pclass", AVG("Age")
FROM passengers
GROUP By "Pclass"
""")
print()
print('Class : Average Age')
for pclass, age in cur.fetchall():
    print(f'{pclass:5} : {age:.2f}')

# What was the average fare by passenger class? By survival?
cur.execute("""
SELECT "Pclass", AVG("Fare")
FROM passengers
GROUP By "Pclass"
""")
print()
print('Class : Average Fare')
for pclass, fare in cur.fetchall():
    print(f'{pclass:5} : {fare:.2f}')

cur.execute("""
SELECT "Survived", AVG("Fare")
FROM passengers
GROUP By "Survived"
""")
print()
print('Survived? : Average Fare')
for survived, fare in cur.fetchall():
    if survived:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'{ans:9} : {fare:.2f}')

# How many siblings/spouses aboard on average, by passenger class? By survival?
cur.execute("""
SELECT "Pclass", AVG("Siblings/Spouses Aboard")
FROM passengers
GROUP By "Pclass"
""")
print()
print('Class : Siblings/Spouses Aboard')
for pclass, fam in cur.fetchall():
    print(f'{pclass:5} : {fam:.2f}')

cur.execute("""
SELECT "Survived", AVG("Siblings/Spouses Aboard")
FROM passengers
GROUP By "Survived"
""")
print()
print('Survived? : Siblings/Spouses Aboard')
for survived, fam in cur.fetchall():
    if survived:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'{ans:9} : {fam:.2f}')

# How many parents/children aboard on average, by passenger class? By survival?
cur.execute("""
SELECT "Pclass", AVG("Parents/Children Aboard")
FROM passengers
GROUP By "Pclass"
""")
print()
print('Class : Parents/Children Aboard')
for pclass, fam in cur.fetchall():
    print(f'{pclass:5} : {fam:.2f}')

cur.execute("""
SELECT "Survived", AVG("Parents/Children Aboard")
FROM passengers
GROUP By "Survived"
""")
print()
print('Survived? : Parents/Children Aboard')
for survived, fam in cur.fetchall():
    if survived:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'{ans:9} : {fam:.2f}')

# Do any passengers have the same name?
cur.execute("""
SELECT "Name", COUNT(*)
FROM passengers
GROUP BY "Name"
HAVING COUNT(*) > 1
""")
print()
print('Do any passengers have the same name?')
if len(cur.fetchall()) > 0:
    print('Yes')
else:
    print('No')

conn.close()
cur.close()
