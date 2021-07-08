import pandas as pd
import psycopg2
from tqdm import tqdm

dbname = ''
user = ''
password = ''
host = 'raja.db.elephantsql.com'
csv = 'titanic.csv'

df = pd.read_csv(csv)

columns = df.columns.tolist()
col_type_dict = dict(zip(df.dtypes.index.tolist(),
                         df.dtypes.values.tolist()))

conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

curs = conn.cursor()

create_titanic_table = '''
    CREATE TABLE titanic (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex VARCHAR(10),
        Age FLOAT,
        Siblings_Spouces_Aboard INT,
        Parents_Children_Aboard INT,
        Fare FLOAT        
    )
'''

curs.execute(create_titanic_table)

# This shows all the tables in the postgres.
show_tables = """
    SELECT
       *
    FROM
       pg_catalog.pg_tables
    WHERE
       schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""

# insert each row of pandas into the dB
for index, row in  tqdm(df.iterrows(), total=df.shape[0]):
    insert_record = f'''
        INSERT INTO titanic (
            Survived, Pclass, Name, Sex, Age,
            Siblings_Spouces_Aboard, Parents_Children_Aboard,
            Fare
        )
        VALUES (
        {row[0]}, {row[1]}, '{row[2].replace("'", "''")}', 
        '{row[3]}', {row[4]}, {row[5]}, {row[6]}, {row[7]}
        );
    '''
    curs.execute(insert_record)

curs.close()
conn.commit()
conn.close()