import psycopg2

dbname = 'lsustohi'
user = 'lsustohi'
password = '?'
host = 'rajje.db.elephantsql.com'

#Create connection and cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()


#Create table
create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""
#pg_curs.execute(create_table_statement)
#pg_conn.commit()    Only Once


#Insert data into table
insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""
#pg_curs.execute(insert_statement)
#pg_conn.commit()   Only Once


#Query the table and data
query = "SELECT * FROM test_table;"
pg_curs.execute(query)
print(pg_curs.fetchall())

