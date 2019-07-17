#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install psycopg2-binary
#!pip install pandas


# In[2]:


import psycopg2 
print('Imported')


# In[3]:


dbname = 'nrqyjmbk'
user = 'nrqyjmbk'
password = '1d8mzh6uo7-PqRNsjYIf8ZnomO7hvu1T'
host = 'raja.db.elephantsql.com'


# In[4]:


help(psycopg2)


# In[5]:


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


# In[6]:


pg_curs = pg_conn.cursor()


# In[7]:


pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()


# In[8]:


import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')


# In[9]:


sl_curs = sl_conn.cursor()


# In[10]:


sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()


# In[11]:


#Our goal is an ETL/data_pipeline
#Get the character data from SQLite data to PostgreSQL
characters = sl_curs.execute("SELECT * FROM charactercreator_character").fetchall()


# In[12]:


characters[0]


# In[13]:


characters[-1]


# In[14]:


#Now we need to put it in the PostgreSQL with schema
create_character_table = '''
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT)
'''


# In[16]:


pg_curs.execute(create_character_table)


# In[ ]:


# loop over and insert results
for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(character[1:])
    pg_curs.execute(insert_character)


# In[ ]:


#SELECT are read only opeerations, most of the time you should only be doing that.
#INSERTS and DELETES ect are usually for devops to make the call
#IT IS ALL OR NOTHING HOWEVER and if one part is broke it will terminate the command
#leaving no partial changes


# In[ ]:


pg_conn.commit()


# In[ ]:


#REMAKE THE CURSOR 
#SQLlite returnsa a cursor when you execute instead of changing the cursor and cannot
#change fetchall at the end
pg_curs = pg_conn.cursor()
pg_curs.execute("SELECT * FROM charactercreator_character;")
pg_characters = pg_curs.fetchall()


# In[ ]:


pg_characters[0]


# In[ ]:


characters[0]


# In[17]:


for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character


# In[ ]:




