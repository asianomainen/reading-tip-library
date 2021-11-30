from database_connection import get_database_connection


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Tips (id INTEGER PRIMARY KEY, name TEXT, url TEXT)")

def initialize_database():
    connection = get_database_connection()

    create_tables(connection)

if __name__ == '__main__':
    initialize_database()