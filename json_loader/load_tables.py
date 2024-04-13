import psycopg
from tables import *
from known_tables import load_known_tables

root_database_name = "project_database"
dbname = "query_database"
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
conn = psycopg.connect(dbname=root_database_name, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

def drop_database():
    # Drop database if it exists.
    try:
        conn.autocommit = True
        cursor.execute(f"DROP DATABASE IF EXISTS {dbname};")
        conn.commit()
    except Exception as error:
        print(error)
        pass
    finally:
        conn.autocommit = False


if __name__ == "__main__":
    conn.autocommit = True
    drop_database()

    # Create the Database if it DNE
    try:
        conn.autocommit = True
        cursor.execute(f"CREATE DATABASE {dbname};")
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        conn.autocommit = False
    conn.close()

    # Connect to this query database.
    conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    conn.autocommit = True
    create_tables(cursor)
    load_known_tables(cursor)
    conn.commit()