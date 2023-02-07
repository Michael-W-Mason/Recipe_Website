import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
    except Error as err:
        print(err)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection()