import pandas as pd
import sqlite3

df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect("buddy_holidayiq.sqlite3")
df.to_sql("ratings", con=conn)
pd.read_sql_query("SELECT count(*) FROM ratings", conn