"""
LSDS 323 Lesson :: NoSQL + MongoDB
"""
# %%
import pymongo

# %%
client = pymongo.MongoClient(
    "mongodb://fyi_admin:oM6u1*Id%25Kzt%25jWHY@cluster0-shard-00-00-p0nim.mongodb.net:27017,cluster0-shard-00-01-p0nim.mongodb.net:27017,cluster0-shard-00-02-p0nim.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
)
db = client.test

# %% Count documents
db.test.count_documents({"x": 1})

# %% Insert document
db.test.insert_one({"x": 1})

# Count again
db.test.count_documents({"x": 1})

# %%
