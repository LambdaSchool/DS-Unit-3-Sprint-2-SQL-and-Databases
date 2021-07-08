import sys
import os
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
        SELECT survived, COUNT(passenger_id)
        FROM titanic
        GROUP BY survived;
    """
    curs.execute(sql)
    items = curs.fetchall()
    num_survived = items[0][1]
    num_deaths   = items[1][1]
    print("Number of survivors:", num_survived)
    print("Number of deaths:", num_deaths)

def count_pass_per_class(curs):

    sql = """
        SELECT pclass, COUNT(passenger_id)
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass;
    """
    curs.execute(sql)
    items = curs.fetchall()

    print("Number of passengers in each class:")
    for item in items:
        print("  class:", item[0], "num:", item[1])

def count_pass_per_class_survived_died(curs):

    sql = """
        SELECT pclass, survived, COUNT(passenger_id)
        FROM titanic
        GROUP BY pclass, survived
        ORDER BY pclass, survived
    """
    curs.execute(sql)
    items = curs.fetchall()
    print("Number of passengers in each class that survived/died:")
    for item in items:
        print("  class:", item[0], "survived:", item[1], "num:", item[2])

def avg_age_survivors_nonsurvivors(curs):

    sql = """
        SELECT survived, AVG(age)
        FROM titanic
        GROUP BY survived
        ORDER BY survived
    """
    curs.execute(sql)
    items = curs.fetchall()
    print("Average age of survivors:", items[1][1])
    print("Average age of non-survivors:", items[0][1])

def avg_age_per_class(curs):

    sql = """
        SELECT pclass, AVG(age)
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass
    """
    curs.execute(sql)
    items = curs.fetchall()
    for item in items:
        print("  class:", item[0], "age:", item[1])

def avg_fare_per_class(curs):

   sql = """
       SELECT pclass, AVG(fare)
       FROM titanic
       GROUP BY pclass
       ORDER BY pclass
   """
   curs.execute(sql)
   items = curs.fetchall()
   print("Average fare per class:")
   for item in items:
       print("  class:", item[0], "average fare:", item[1])

def avg_fare_survivors_vs_nonsurvivors(curs):

   sql = """
       SELECT survived, AVG(fare)
       FROM titanic
       GROUP BY survived
       ORDER BY survived
   """
   curs.execute(sql)
   items = curs.fetchall()
   print("Average fare survivors vs non-survivors:")
   for item in items:
       print("  survived:", item[0], "average fare:", item[1])

def avg_num_siblings_spouses_per_class(curs):

    sql = """
        SELECT pclass, AVG(num_siblings_spouses_aboard)
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass
    """
    curs.execute(sql)
    items = curs.fetchall()
    print("Average number of siblings and spouses aboard per class:")
    for item in items:
        print("  class:", item[0], "num:", item[1])

def avg_num_siblings_spouses_per_class_and_survival(curs):

    sql = """
        SELECT pclass, survived, AVG(num_siblings_spouses_aboard)
        FROM titanic
        GROUP BY pclass, survived
        ORDER BY pclass, survived
    """
    curs.execute(sql)
    items = curs.fetchall()
    print("Average number of siblings and spouses aboard per class and survival:")
    for item in items:
        print("  class:", item[0], "survived:", item[1], "num:", num)

def passengers_with_same_names(curs):

    sql = """
        SELECT COUNT(DISTINCT LOWER(name))
        FROM titanic
    """
    curs.execute(sql)
    num_distinct_names = curs.fetchone()[0]
    print("Number of passengers with distinct names:",
          num_distinct_names)

    sql = """
        SELECT COUNT(*)
        FROM titanic
    """
    curs.execute(sql)
    num_rows_in_table = curs.fetchone()[0]
    print("Number of rows in table:",
          num_rows_in_table)
    print("Number of names shared with other passengers:",
          num_rows_in_table - num_distinct_names)

if __name__ == "__main__":

    dbname = os.environ["POSTGRESQL_ELEPHANTDB_DBNAME"]
    user   = os.environ["POSTGRESQL_ELEPHANTDB_USERNAME"]
    pwd    = os.environ["POSTGRESQL_ELEPHANTDB_PASSWORD"]
    host   = os.environ["POSTGRESQL_ELEPHANTDB_HOSTNAME"]

    with pg.connect(dbname=dbname, user=user, password=pwd, host=host) as conn:
        with conn.cursor() as curs:
            # create_titanic_table(curs)
            count_survivors_and_not(curs)
            count_pass_per_class(curs)
            count_pass_per_class_survived_died(curs)
            avg_age_survivors_nonsurvivors(curs)
            avg_age_per_class(curs)
            avg_fare_per_class(curs)
            avg_fare_survivors_vs_nonsurvivors(curs)
            passengers_with_same_names(curs)
