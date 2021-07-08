import sys
import pandas as pd
import psycopg2 as pg
import psycopg2.extras

def csv_to_list_of_tuples(filename, **kwargs):
    df = pd.read_csv(filename, **kwargs)
    list_of_tuples = df.apply(lambda x: (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]),
                              axis = 1)
    return list_of_tuples

sql_create_titanic_table = """CREATE TABLE titanic (
  passenger_id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name varchar(100),
  sex varchar(10),
  age real,
  num_siblings_spouses_aboard int,
  num_parents_children_aboard int,
  fare real
);"""

def create_titanic_table(curs):
    # These lines are here just to remove the older table if it exists
    curs.execute("""DROP TABLE titanic""")
    conn.commit()

    curs.execute(sql_create_titanic_table)
    conn.commit()
    res = csv_to_list_of_tuples('./titanic.csv', header=0, index_col=False)
    print(res[4:8].values)
    print("----------- Starting table insert -------")
    psycopg2.extras.execute_values(curs, "INSERT INTO titanic (survived,pclass,name,sex,age,num_siblings_spouses_aboard,num_parents_children_aboard,fare) VALUES %s", res.values)
    conn.commit()
    print("----------- Ended table insert ----------")

def count_survivors_and_not(curs):
    sql = """
        SELECT *
        FROM titanic
        GROUP BY survived
    """
    curs.execute(sql)
    print(curs.fetchall())

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: titanic.py dbname user pwd host")
        sys.exit()

    dbname = sys.argv[1]
    user   = sys.argv[2]
    pwd    = sys.argv[3]
    host   = sys.argv[4]

    with pg.connect(dbname=dbname, user=user, password=pwd, host=host) as conn:
        with conn.cursor() as curs:
            create_titanic_table(curs)
            count_survivors_and_not(curs)
