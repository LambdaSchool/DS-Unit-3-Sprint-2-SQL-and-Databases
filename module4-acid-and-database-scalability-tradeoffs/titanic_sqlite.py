"""
Titanic SQLite3 :: Imports titanic.csv into SQLite3 DB.
"""

# %% Imports
import os

from pprint import pprint
import sqlite3

# %% Move to working directory
cwd = os.environ["DIR_324"]
os.chdir(cwd)
print(os.getcwd())

# %% Local imports
# I will be putting all of my queries and functions in a package 'tiq'
import tiq

# %%
