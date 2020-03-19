import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

client = pymongo.MongoClient(
    f'mongodb+srv://{DB_USER}:{DB_PASS}'
    f'@lambda-qip5e.mongodb.net/test?retryWrites=true&w=majority')

rpg = client.rpg

# total characters
print(rpg.charactercreator.character.count_documents({}))

# subclass counts
subclass = ['mage', 'thief', 'cleric', 'fighter', 'necromancer']
for x in subclass:
    if x == 'mage':
        count = rpg.charactercreator[x].count_documents({})
        count2 = rpg.charactercreator.necromancer.count_documents({})
        print(f'Mage Count: {count-count2}')
    else:
        count = rpg.charactercreator[x].count_documents({})
        print(f'{x.capitalize()} Count: {count}')

# total items
count = rpg.armory.item.count_documents({})
print(f'Total Items: {count}')

# weapons vs not
count = rpg.armory.weapon.count_documents({})
count2 = rpg.armory.item.count_documents({})
print(f'Weapon Count: {count}')
print(f'Non-Weapon Item Count: {count2-count}\n')

# Items per character
count = rpg.charactercreator.character.find(
    {}, {'_id': 0, 'name': 1, 'inventory': 1}
)
for doc in count:
    print(f'Character Name: {doc["name"]} == '
          f'Item Count: {len(doc["inventory"])}')

# # Weapons per character
# count = rpg.charactercreator.character.find(
#     {}, {'_id': 0, 'name': 1, 'inventory': 1}
# )
# for doc in count:
#     print(f'Character Name: {doc["name"]} == '
#           f'Item Count: {len(doc["inventory"])}')

# Average items per character
count = rpg.charactercreator.character.find(
    {}, {'_id': 0, 'inventory': 1})
inventories = []
for doc in count:
    inventories.append(len(doc['inventory']))
count2 = rpg.charactercreator.character.count_documents({})
print(f'Average Items Per Character: {sum(inventories)/count2}')

# # Average Weapons Per Character
# count = rpg.charactercreator.character.find(
#     {}, {'_id': 0, 'inventory': 1})
# inventories = []
# for doc in count:
#     inventories.append(len(doc['inventory']))
# count2 = rpg.charactercreator.character.count_documents({})
# print(f'Average Items Per Character: {sum(inventories)/count2}')
