#!/usr/bin/env python
import os
import pymongo

def num_total_characters(coll):
    count = coll.count_documents({'model': 'charactercreator.character'})
    print('Number of total characters:', count)

def num_characters_in_each_subclass(coll):

    clerics = coll.count_documents({'model': 'charactercreator.cleric'})
    fighters = coll.count_documents({'model': 'charactercreator.fighter'})
    mages = coll.count_documents({'model': 'charactercreator.mage'})
    thieves = coll.count_documents({'model': 'charactercreator.thief'})

    print("Num characters in each subclass:")
    print("  Number of total clerics:", clerics)
    print("  Number of total fighters:", fighters)
    print("  Number of total mages:", mages)
    print("  Number of total thieves:", thieves)

def num_total_items(coll, print_result = True):
    num_items = coll.count_documents({'model': 'armory.item'})

    if print_result:
        print("Number of total items:", num_items)
    return num_items

def num_total_weapons(coll, print_result = True):
    num_weapons = coll.count_documents({'model': 'armory.weapon'})

    if print_result:
        print("Number of total weapons:", num_weapons)
    return num_weapons

def num_weapons_and_other(coll):
    num_weapons = num_total_weapons(coll, print_result = False)
    num_items = num_total_items(coll, print_result = False)
    print("Number of items that are weapons:", num_weapons)
    print("Number of items that are not weapons:", num_items - num_weapons)

MAX_LIMIT = 10000
# TODO: Fix the limit in the parameters here !!!
def character_inventory(coll, limit = MAX_LIMIT, print_result = True):

    characters = list(coll.find({'model': 'charactercreator.character'}))
    if print_result:
        print('Characters (limit 20) and the number of items they posess:')

    until = min(limit, len(characters))
    res = []
    for i in range(until):
        c = characters[i]
        res.append({c["fields"]["name"]: c["fields"]["inventory"]})
        if print_result:
            print('  ', c["fields"]["name"], ":", len(c["fields"]["inventory"]))
    return res

def character_weapons(coll, limit = MAX_LIMIT, print_result = True):
    c_inventory = character_inventory(coll, limit = limit, print_result = False)
    weapons = list(map(lambda x: x['pk'], list(coll.find({'model': 'armory.weapon'}))))

    if print_result:
        print('Number of weapons per character (limit 20):')
    res = []
    for character in c_inventory:
        for k, inventory in character.items():
            name_to_weapons = {k: 0}
            for v in inventory:
                if v in weapons:
                    name_to_weapons[k] += 1
            res.append(name_to_weapons)

            if print_result:
                print('  ', k, ':', name_to_weapons[k])
    return res

def avg_num_items_per_character(coll):
    c_inventory = character_inventory(coll, limit = MAX_LIMIT, print_result = False)

    sum = 0
    for c in c_inventory:
        for k, inventory in c.items():
            sum += len(inventory)
    print('Average number of items per character:',
          sum / len(c_inventory))

def avg_num_weapons_per_character(coll):
    c_weapons = character_weapons(coll, limit = MAX_LIMIT, print_result = False)

    sum = 0
    for c in c_weapons:
        for k, weapons in c.items():
            sum += weapons
    print('Average number of weapons per character:',
          sum / len(c_weapons))

if __name__ == "__main__":
    mongo_atlas_username = os.environ['MONGO_ATLAS_USERNAME']
    mongo_atlas_password = os.environ['MONGO_ATLAS_PASSWORD']

    connection_string = "mongodb://<USERNAME>:<PASSWORD>@cluster0-shard-00-00-q42xu.mongodb.net:27017,cluster0-shard-00-01-q42xu.mongodb.net:27017,cluster0-shard-00-02-q42xu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
    connection_string = connection_string.replace("<USERNAME>",
                                                  mongo_atlas_username)
    connection_string = connection_string.replace("<PASSWORD>",
                                                  mongo_atlas_password)
    print(connection_string)

    client = pymongo.MongoClient(connection_string)

    db = client.rpg_database
    coll = db.rpg_collection

    num_total_characters(coll)
    num_characters_in_each_subclass(coll)
    num_total_items(coll)
    num_weapons_and_other(coll)
    character_inventory(coll, 20)
    character_weapons(coll, 20)
    avg_num_items_per_character(coll)
    avg_num_weapons_per_character(coll)
