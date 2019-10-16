# /usr/bin/env python
" Import from .csv to PostgreSQL "

import pandas as import pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

titanic = pd.read_csv('titanic.csv')

# Retreive secret credentials
load_dotenv()
ElephantSQL_URL = os.getenv("ElephantSQL_URL")

# Upload data to SQL
engine = create_engine(ElephantSQL_URL)
titanic.to_sql(name='passengers', con=engine)