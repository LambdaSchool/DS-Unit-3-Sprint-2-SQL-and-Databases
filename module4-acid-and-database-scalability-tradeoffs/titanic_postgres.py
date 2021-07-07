"""
Titanic Postgres :: Loads titanic.csv into local Postgres instance.
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
# I will be putting all of my queries and functions in a package 'tiq'
import tiq

# %% Read titanic.csv into pd.DataFrame
# Define filename as variable to use later
tit_filename = "titanic.csv"

# Read the csv into dataframe
df1 = pd.read_csv(tit_filename)

# %% Print out head and shape of data
print(df1.shape)
df1.head()

# %% Look at the datatypes of the columns
df1.dtypes

# %% Clean up the dataset
# Fix column names
df2 = df1.clean_names()

# %% Find longest name
df2["name"].str.len().max()
# Result is 81 characters
# useful for specifying length of postgres column

# %% DataFrame -> Postgres
# I could use the pd.to_sql method, but it would require sqlalchemy
# I should be able to loop through the rows of the dataframe
# and write each one to the database manually

# %% Postgres connection
titanic_uri = os.environ["TIT_DB_URI"]

# %% Create postgres table

create_pass_table = """--- Create titanic passengers table in postgres
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(88),
    sex VARCHAR(8),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT
);"""

# Create the passenger table
with psycopg2.connect(titanic_uri) as conn:
    tiq.quarry(conn, create_pass_table, None, False)

# %% Queries

# Query string to be updated with information for each passenger
insert_passenger = """INSERT INTO passengers
    (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

# Standard select statement
select = """
    SELECT
        *
    FROM
        passengers;"""

# %% Insert the passengers data
with psycopg2.connect(titanic_uri) as conn:
    # Iterate through rows (returned as tuples from .itertuples())
    for row in df2.itertuples(index=False, name="Passenger"):
        row_data = []  # List to hold each passenger's data
        # Row data is passed into 'insert_passenger' query as parameters

        for i in range(len(row)):  # Loop thru fields that make up the row
            row_data.append(row[i])

        # Create each passenger record using the tiq.quarry function
        tiq.quarry(conn, insert_passenger, row_data, False)

    # Select the table after all passengers are added
    passengers = tiq.quarry(conn, select)

# %% Drop table to restart insert
# drop_passengers = """--- Drop passengers table to start over
# DROP TABLE passengers;"""

# with psycopg2.connect(titanic_uri) as conn:
#     tiq.quarry(conn, drop_passengers, None, False)
