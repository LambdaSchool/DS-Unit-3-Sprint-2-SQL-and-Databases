# imports
import psycopg2 as ps, pandas as pd, passwords


# DB connection setup
dbname = passwords.dbname
user = passwords.user
password = passwords.password
host = passwords.host

# connect to database
conn = ps.connect(dbname=dbname, user=user, password=password, host=host)

print(conn)

# questions to answer
ques_list = [
    "How many passengers survived, and how many died?",
    "How many passengers were in each class?",
    "How many passengers survived/died within each class?",
    "What was the average age of survivors vs nonsurvivors?",
    "What was the average age of each passenger class?",
    "What was the average fare by passenger class? By survival?",
    "How many siblings/spouses aboard on average, by passenger class? By survival?",
    "How many parents/children aboard on average, by passenger class? By survival?",
]

# turn list into dict for ease of use
q_dict = {}
for q in ques_list:
    entry = {ques_list.index(q) + 1: q}
    q_dict.update(entry)

# create querries to answer questions
a_dict = {
    1: """
    SELECT survived, COUNT(*) 
    FROM simple_passenger_table
    GROUP BY survived;
""",
    2: """
    SELECT pclass, COUNT(*) 
    FROM simple_passenger_table
    GROUP BY pclass 
    ORDER BY pclass;
    
""",
    3: """
    SELECT pclass, survived, COUNT(survived) 
    FROM simple_passenger_table
    GROUP BY pclass, survived
    ORDER BY pclass;
""",
    4: """
    SELECT survived, AVG(age) 
    FROM simple_passenger_table
    GROUP BY survived;
""",
    5: """
    SELECT pclass, AVG(age) 
    FROM simple_passenger_table
    GROUP BY pclass;
""",
    6: """
    SELECT pclass, survived, AVG(fare)
    FROM simple_passenger_table
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    7: """
    SELECT pclass, survived, COUNT(sibs_abd)
    FROM simple_passenger_table
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    8: """
    SELECT pclass, survived, COUNT(p_c_abd)
    FROM simple_passenger_table
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    9: """
    SELECT name, COUNT(passenger_id) 
    FROM simple_passenger_table 
    GROUP BY name HAVING COUNT(passenger_id) > 1;
""",
}

q_all_names = """
    SELECT name
    FROM simple_passenger_table;
"""

# Answer questions using SQL querries

# iterate through questions
for q_key, q_val in q_dict.items():

    # print questions
    print("Question ", q_key)
    print(q_val)

    # print query
    print("SQL query :")
    print(a_dict[q_key])

    # create a connection object and execute query
    curs = conn.cursor()
    curs.execute(a_dict[q_key])
    output = curs.fetchall()

    print("Output: ")
    print(output, "\n")

    # close cursor
    curs.close()


# bonus_questions = """
# (Bonus! Hard, may require pulling and processing with Python)
# How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.)
# with the same last name and with at least 1 sibling/spouse aboard are a married couple.

# Do any passengers have the same name?
# """
# # get all passenger names

# name_query = """
#     SELECT name
#     FROM simple_passenger_table;
# """

# # create a connection object and execute query
# curs = conn.cursor()
# curs.execute(name_query)
# names_tups = curs.fetchall()
# names_str = []

# for name in names_tups:
#     names_str.append(name[0])

# print(names_str)

# # close cursor
# curs.close()


# # close any open cursors and connection
curs.close()
conn.close()
