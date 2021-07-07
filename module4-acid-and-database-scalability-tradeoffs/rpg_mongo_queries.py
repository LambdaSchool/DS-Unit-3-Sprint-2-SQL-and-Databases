# ./usr/bin/env python
" Importing from JSON to MongoDB"

from dotenv import load_dotenv
import os
import pymongo
import requests
from statistics import mean

"""
Terminal printouts (for reference):

Total Characters: 302

Clerics:          75
Fighters:         68
Mages:            108
Necromancers:     11
Thiefs:           51

Total Items:      174

Total weapons:     37
Total non-weapons: 137

Aliquid iste optio reiciendi    : 3 items
Optio dolorem ex a              : 3 items
Minus c                         : 2 items
Sit ut repr                     : 4 items
At id recusandae expl           : 4 items
Non nobis et of                 : 1 items
Perferendis                     : 5 items
Accusantium amet quidem eve     : 3 items
Sed nostrum inventore error m   : 4 items
Harum repellendus omnis od      : 4 items
Itaque ut commodi,              : 3 items
Molestiae quis                  : 3 items
Ali                             : 4 items
Tempora quod optio possimus il  : 4 items
Sed itaque beatae pari          : 4 items
Quam dolor                      : 1 items
Molestias expedita              : 5 items
Lauda                           : 5 items
Incidunt sint perferen          : 3 items
Laboriosa                       : 1 items

Aliquid iste optio reiciendi    : 0 weapons
Optio dolorem ex a              : 0 weapons
Minus c                         : 0 weapons
Sit ut repr                     : 0 weapons
At id recusandae expl           : 2 weapons
Non nobis et of                 : 0 weapons
Perferendis                     : 1 weapons
Accusantium amet quidem eve     : 0 weapons
Sed nostrum inventore error m   : 0 weapons
Harum repellendus omnis od      : 0 weapons
Itaque ut commodi,              : 1 weapons
Molestiae quis                  : 0 weapons
Ali                             : 0 weapons
Tempora quod optio possimus il  : 0 weapons
Sed itaque beatae pari          : 0 weapons
Quam dolor                      : 0 weapons
Molestias expedita              : 0 weapons
Lauda                           : 0 weapons
Incidunt sint perferen          : 0 weapons
Laboriosa                       : 1 weapons

Average items carried: 2.9735099337748343

Average weapons carried: 0.6721854304635762

"""

load_dotenv()
MongoDB_URL = os.getenv("MongoDB_URL")
rpg_URL = 'https://raw.githubusercontent.com/\
    LambdaSchool/Django-RPG/master/testdata.json'

client = pymongo.MongoClient(MongoDB_URL)
database = client.rpg_database
collection = database.rpg_collection

# How many total Characters are there?
characters = collection.count_documents(
    {'model': "charactercreator.character"})
print()
print(f'Total Characters: {characters}')


# How many of each specific subclass?
clerics = collection.count_documents(
    {'model': "charactercreator.cleric"})
fighters = collection.count_documents(
    {'model': "charactercreator.fighter"})
mages = collection.count_documents(
    {'model': "charactercreator.mage"})
necromancers = collection.count_documents(
    {'model': "charactercreator.necromancer"})
thiefs = collection.count_documents(
    {'model': "charactercreator.thief"})
print()
print(f'Clerics:          {clerics}')
print(f'Fighters:         {fighters}')
print(f'Mages:            {mages}')
print(f'Necromancers:     {necromancers}')
print(f'Thiefs:           {thiefs}')


# How many total Items?
items = collection.count_documents({'model': "armory.item"})
print()
print(f'Total Items:      {items}')


# How many of the Items are weapons? How many are not?
weapons = collection.count_documents({'model': "armory.weapon"})
print()
print(f'Total weapons:     {weapons}')
print(f'Total non-weapons: {items-weapons}')


# How many Items does each character have? (Return first 20 rows)
characters = collection.find({'model': "charactercreator.character"})
print()
for x in characters[:20]:
    name = x['fields']['name']
    items = len(x['fields']['inventory'])
    print(f'{name:32}: {items} items')


# How many Weapons does each character have? (Return first 20 rows)
characters = collection.find({'model': "charactercreator.character"})
weapons = collection.find({'model': "armory.weapon"})
weapon_codes = set(x['pk'] for x in weapons)
print()
for x in characters[:20]:
    name = x['fields']['name']
    items_carried = set(x['fields']['inventory'])
    num_weapons = len(items_carried.intersection(weapon_codes))
    print(f'{name:32}: {num_weapons} weapons')


# On average, how many Items does each Character have?
characters = collection.find({'model': "charactercreator.character"})
items = [len(x['fields']['inventory']) for x in characters]
avg_items = mean(items)
print()
print(f'Average items carried: {avg_items}')


# On average, how many Weapons does each character have?
characters = collection.find({'model': "charactercreator.character"})
weapons_carried = []
for x in characters:
    items = x['fields']['inventory']
    num_weapons = len([x for x in items if x in weapon_codes])
    weapons_carried.append(num_weapons)

avg_weapons = mean(weapons_carried)
print()
print(f'Average weapons carried: {avg_weapons}')
