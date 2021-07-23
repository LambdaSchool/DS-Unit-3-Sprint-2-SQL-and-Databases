import sqlite3

def create_table(conn):
    curs = conn.cursor()
    create_statement = """
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(20),
            favorite_number INTEGER,
            least_favorite_number INTEGER
        );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()

def insert_data(conn)
    my_data = [
        ('Malven', 7, 10,)
        ('Steven', -3, 12,)
        ('Dondre', 80, -1)
    ]
    for row in my_data:
        pass
        # TODO write an insert statement!
    curs.close()
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('example_db.sqlite3')
    create_table(conn)
    insert_data(conn)