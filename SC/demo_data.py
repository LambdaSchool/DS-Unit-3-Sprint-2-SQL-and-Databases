import sqlite3


def create_db(db_name):
    # connect to the db
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()

    #query_table_exist = '''SELECT name FROM sqlite_master WHERE type='table' AND name='{demo}';'''

    # first drop the table if exists to make life easier
    drop_table = '''DROP TABLE IF EXISTS demo'''

    # creating demo table
    create_demo_table = '''
        CREATE TABLE demo (
            s VARCHAR(1),
            x INT,
            y INT
        )
        '''
    conn.commit()
    curs.close()
    conn.close()
    
def insert_records(db_name, records):
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()

    for r in records:
        curs.execute(r)

    conn.commit()
    curs.close()
    conn.close()

if __name__ == "__main__":
    db_name = "demo_data.sqlite3"
    create_db(db_name)
    
    # inserting records
    insert_record1 = """INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)"""
    insert_record2 = """INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)"""
    insert_record3 = """INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)"""
    records = [insert_record1, insert_record2, insert_record3]
    insert_records(db_name, records)
    
    # querying demo table
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()
    q1 = '''SELECT COUNT(*) FROM demo'''
    a1 = curs.execute(q1).fetchall()
    print(f'Total number of rows is {a1[0][0]}')

    q2 = '''SELECT COUNT(*) FROM demo
            WHERE x >= 5 AND y >= 5'''
    a2 = curs.execute(q2).fetchall()
    print(f"There are {a2[0][0]} rows where both 'x' and 'y' are at least 5.")

    q3 = '''SELECT COUNT(DISTINCT y) FROM demo'''
    a3 = curs.execute(q3).fetchall()
    print(f"There are {a3[0][0]} unique values of 'y'.")
    curs.close()
    conn.close()