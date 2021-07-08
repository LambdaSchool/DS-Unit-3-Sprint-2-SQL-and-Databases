import sys, logging
import pandas as pd
import pymongo
import sqlite3
from tqdm import tqdm


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger = setup_custom_logger('rpg_import_mongo')

# setting path to MongoDB connection URL
url_mongo = ""

logger.info("Connecting to MongoDB...")
client = pymongo.MongoClient(url_mongo)
db = client.test

try:
   client.admin.command('ismaster')
except ConnectionFailure:
   logger.info("Server not available...")
   
logger.info("Connected to MongoDB...")

logger.info("Connecting to sqlite3...")
conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()
logger.info("Connected to sqlite3...")

# check all the tables in the DB
curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
#logger.info(curs.fetchall())

df = pd.read_sql_query("SELECT * FROM charactercreator_character", conn)
cols = df.columns.to_list()

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    entry = dict({'charactercreator_character': dict(zip(cols, row))})
    print(entry)
    print(type(entry))
    #db.test.insert_one(entry)
    

# getting the header of the sql table
#col_query = '''PRAGMA table_info(charactercreator_character);'''
#curs.execute(col_query)
#col_list = curs.fetchall()
#cols = [col[1] for col in col_list]
#logger.info(cols)

# doing one single query to get everything, knowing there's
# less than 1k entries in the table.
#query = '''SELECT * FROM charactercreator_character;'''
#charz = curs.execute(query).fetchall()
#logger.info(type(charz))

#print(conn)