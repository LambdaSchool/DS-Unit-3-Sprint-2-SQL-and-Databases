import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results =  execute_query(curs, GET_CHARACTERS)
    print(results) 




