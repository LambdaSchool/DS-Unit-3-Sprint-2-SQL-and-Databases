import psycopg2 as pig
import pandas as pd
dbname = ''
user = ''
password = ''
host = ''
conn = pig.connect(dbname=dbname, user=user, password=password, host=host)
curse = conn.cursor()

make_titanic_table = curse.execute('''
    CREATE TABLE titanic_table(
        pass_id SERIAL PRIMARY KEY,
        survived int,
        pclass int,
        name varchar(100),
        sex varchar(6),
        age int,
        spouse_sibling int,
        parents_children int,
        fare float
    );
''')

# curse.execute(make_titanic_table)
titanic = pd.read_csv('''C:/Users/dakot/Documents/GitHub/DS-Unit-3-Sprint-2
-SQL-and-Databases/module2-sql-for-analysis/titanic.csv''')
titanic.Name = titanic.Name.replace("'", '', regex=True)
titanic_l = titanic.values.tolist()

for item in titanic_l:
    insert = '''INSERT INTO titanic_table(
        survived, pclass, name, sex, age, spouse_sibling, 
        parents_children, fare) VALUES''' + str(tuple(item))
    curse.execute(insert)


# with open('titanic.csv', 'r') as f:
#     next(f)
#     curse.copy_from(f, 'titanic_table', sep=',')
# conn.commit()
