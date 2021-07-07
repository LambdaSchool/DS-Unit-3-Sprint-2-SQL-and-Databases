# %% BuddyMove to SQL
# A Python script by Tobias Reaper
# ---
# Loads the BuddyMove dataset via CSV
# Saves the resulting DataFrame into an SQLite3 database
# And queries the resulting database

# %% Imports
import sqlite3
import os
import pandas as pd

# %% Create the path object
# Where the data is (and will be) located

# The working directory (could un-hardcode it with `os.getcwd()`)
# However, vscode works from the project root
path1 = "/Users/Tobias/workshop/dasci/sprints/10-SQL_and_Databases"
path2 = "DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/"
dir_path = os.path.join(path1, path2)

csv_filename = "buddymove_holidayiq.csv"
csv_fullpath = os.path.join(dir_path, csv_filename)

print(csv_fullpath)

# %% Load the csv into a DataFrame
df1 = pd.read_csv(csv_fullpath)

# %% Confirm it is the expected size / shape
assert df1.shape == (249, 7)
print(df1.shape)
print(df1.head())

# %% Clean up the dataframe column names using pyjanitor
import janitor

# Replace the whitespace in the "User ID" column
# Also makes the column names lowercase
df2 = df1.clean_names()

df2.head()

# %% Clean up the "user_id" column
# Strip the "User" and convert to integer
df2["user_id"] = df2["user_id"].str.strip("User ").astype(int)

df2.head()

# %% Create the database connection
# In this case, it will create a new database file

# Create filepath / filename for the new database
db_filename = "buddymove_holidayiq.sqlite3"
db_filepath = os.path.join(dir_path, db_filename)

conn = sqlite3.connect(db_filepath)

# %% Write the DataFrame into the new database
# Create a new table called "review"
df2.to_sql("review", con=conn)

# %% Create the cursor object
cur = conn.cursor()

# %% Create test query 1
# Count how many rows you have - it should be 249!
query1 = """--- Row count - it should be 249
SELECT COUNT(*)
FROM review;"""

# %% Run query 1 and print the result
query1_result = cur.execute(query1).fetchone()[0]
assert query1_result == 249

print(query1_result)

# %% Create test query 2
# How many users who reviewed at least 100 `Nature` in the category also
# reviewed at least 100 in the `Shopping` category?
query2 = """--- Number of users who reviewed > 100 in `Nature` and `Shopping`
SELECT COUNT(*)
FROM review
WHERE
    nature > 100
AND shopping > 100;"""

# %% Run query 2 and print the result
query2_result = cur.execute(query2).fetchone()[0]

print(query2_result)

# %% Create test query 3
# (*Stretch*) What are the average number of reviews for each category?
query3 = """--- Average number of reviews for each category
SELECT
    AVG(sports) avg_sports,
    AVG(religious) avg_religious,
    AVG(nature) avg_nature,
    AVG(theatre) avg_theatre,
    AVG(shopping) avg_shopping,
    AVG(picnic) avg_picnic
FROM review;"""

# %% Run query 3 and print the result
query3_result = cur.execute(query3).fetchall()
query3_colnames = cur.description

for i in range(len(query3_result[0])):
    print(f"{query3_colnames[i][0]}: {query3_result[0][i]}")
    print()

# %%
cur.close()

# %%
conn.close()
