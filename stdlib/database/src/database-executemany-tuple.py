import sqlite3


DATABASE = ':memory:'
DATA = [(61041212345, 'José', 'Jiménez'),
        (61041212346, 'Jan', 'Twardowski'),
        (61041212347, 'Melissa', 'Lewis'),
        (61041212348, 'Alex', 'Vogel'),
        (61041212349, 'Ryan', 'Stone')]

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""

SQL_INSERT = """
    INSERT INTO astronauts
    VALUES (NULL, ?, ?, ?)"""


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT, DATA)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
