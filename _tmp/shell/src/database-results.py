import sqlite3

DATABASE = ':memory:'
DATA = [{'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'}]

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""

SQL_INSERT = """
    INSERT INTO astronauts
    VALUES (NULL, :pesel, :firstname, :lastname)"""

SQL_SELECT = 'SELECT * FROM astronauts'


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, DATA)

    for row in db.execute(SQL_SELECT):
        print(row)

# (1, 61041212345, 'José', 'Jiménez')
# (2, 61041212346, 'Jan', 'Twardowski')
# (3, 61041212347, 'Melissa', 'Lewis')
# (4, 61041212348, 'Alex', 'Vogel')
# (5, 61041212349, 'Ryan', 'Stone')
