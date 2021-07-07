# ./usr/bin/env python
" Importing from .csv to PostgreSQL, the hard way"

from dotenv import load_dotenv
import os
import psycopg2
import csv
load_dotenv()
ElephantSQL_URL = os.getenv("ElephantSQL_URL")

conn = psycopg2.connect(ElephantSQL_URL)
cur = conn.cursor()

schema = """CREATE TABLE "passengers" (
    "Survived" INT,
    "Pclass" INT,
    "Name" TEXT,
    "Sex" TEXT,
    "Age" NUMERIC(4, 2),
    "Siblings_Spouses_Aboard" INT,
    "Parents_Children_Aboard" INT,
    "Fare" NUMERIC(7, 4)
);"""

cur.execute(schema)

with open('titanic.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    parsed = ((int(row[0]),
              int(row[1]),
              row[2].replace("'", '"'),  # Swap out the quote types
              row[3],
              float(row[4]),
              int(row[5]),
              int(row[6]),
              float(row[7]))
              for row in reader
              )
    for row in parsed:
        insert_result = """INSERT INTO "passengers" VALUES""" + str(row) + ';'
        cur.execute(insert_result)

conn.commit()
cur.close()
conn.close()
