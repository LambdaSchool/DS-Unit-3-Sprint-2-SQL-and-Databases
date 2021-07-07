"""
Titanic Postgres :: Runs queries against titanic data in 
local Postgres instance.
"""

# %% Imports
import os
from pprint import pprint
import psycopg2
import pandas as pd

import janitor

# %% Move to working directory
cwd = os.environ["DIR_324"]
os.chdir(cwd)
print(os.getcwd())

# %% Local imports
# queries and functions are inside 'tiq'
import tiq

# %% Postgres URI
titanic_uri = os.environ["TIT_DB_URI"]

# %% The Easier Queries
# Executes list of easy queries
with psycopg2.connect(titanic_uri) as conn:
    for q in tiq.qez:
        pprint(q.split("\n")[0])
        tiq.quarry(conn, q)
        print()

# %% tiq.same_name
"""Do any passengers have the same name?"""
