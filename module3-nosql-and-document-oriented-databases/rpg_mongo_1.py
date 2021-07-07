"""
RPG MongoDB :: Loads RPG test data into a mongo db cluster.
Author :: Tobias Reaper | github.com/tobias-fyi
"""

# %% Imports
import pymongo
import os
import json

from pprint import pprint

# %% Construct path working directory
# Get the full filepath from envirovars
dir_path = os.environ["DIR_323"]

os.chdir(dir_path)  # Change working directory

# Just to be sure that we're in the correct directory
assert os.getcwd() == dir_path

# %% Load json into python object

# Define name of json file
json_file_name = "rpg_data.json"

# Open file and read it into a python object
with open(json_file_name) as f:
    rpg_data = json.load(f)

pprint(rpg_data)

# %% Split up Python object
# The goal here is to reorganize the data such that
# each row is contained within its corresponding model.
# This way, I can use the name of the model as the name
# of the MongoDB document.

# Set to hold distinct data models
rpg_modelset = set()

for row in rpg_data:  # Loop to build set of existing models
    rpg_modelset.add(row["model"].split(".")[1])

# TODO: Use list comprehension to clean up loops

# %% Create dictionaries for each model
# They will be dictionaries inside of rpg_models
rpg_models = {}

# Loop to nest a dict for each model inside rpg_models
for model in rpg_modelset:
    rpg_models[f"{model}"] = {}

# %% Now add all the data into the new data structure
# Loop through rows, this time adding them to their respective nested dict
for row in rpg_data:
    rpg_models[f'{row["model"].split(".")[1]}'][row["pk"]] = row["fields"]

# %% Connect to the cluster
# Password is a URL-encoded string saved as an environment variable
client = pymongo.MongoClient(os.environ["MONGO_URI"])

# %% Create the database
db = client.rpg_db

# %% Loop through models and rows
# Write each row to its corresponding model
# In MongoDB terms: insert each document into its collection

for d in rpg_models:
    print(f"Model: {d}")  # Visual confirmation of model names

    # Create a collection (table) for each rpg_data model
    coll = db[f"{d}"]

    insert_list = []  # List to hold records of each model

    # Loop through the records in each model, appending to the list
    for k, v in rpg_models[d].items():
        # Insert the key into value dict as "pk"
        # This way, "pk" will be included in each record
        v["pk"] = k
        insert_list.append(v)

    # Insert the contents of 'insert_list' into collection
    coll.insert_many(insert_list)

    # Print the insert list just as visual confirmation
    pprint(insert_list)

# %% Look at one document from each collection
for d in rpg_models:
    print(f"Collection: {d}")  # Collection title
    # Count the number of docs by passing empty query
    print(f"  Doc count: {db[f'{d}'].count_documents({})}")
    # pprint(db[f"{d}"].find_one())  # Pretty print the first doc

# %%
