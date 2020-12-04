import sqlite3
from datetime import datetime, timezone

DATABASE = r'_temporary.sqlite3'
FILE = r'_temporary.csv'

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'}

DATA = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0
5.1,3.3,1.7,0.5,2
4.8,3.4,1.9,0.2,0
5.0,3.0,1.6,0.2,1
5.0,3.4,1.6,0.4,2
5.2,3.5,1.5,0.2,1
5.2,3.4,1.4,0.2,2
4.7,3.2,1.6,0.2,0"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        species TEXT,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL);"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        iris_created_index ON iris (created);"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        CURRENT_TIMESTAMP,
        :species,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width);"""

SQL_SELECT = """
    SELECT *
    FROM iris
    ORDER BY created DESC"""

data = []

with open(FILE, mode='w') as file:
    file.write(DATA)

with open(FILE) as file:
    for line in file:
        line = line.strip().split(',')

        data.append({
            'sepal_length': float(line[0]),
            'sepal_width': float(line[1]),
            'petal_length': float(line[2]),
            'petal_width': float(line[3]),
            'species': SPECIES[int(line[4])],
        })


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, data)
    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))

# ...
# {'id': 15, 'datetime': '1961-04-12 06:07:00.952411+00:00', 'species': 'versicolor', 'sepal_length': 5.2, 'sepal_width': 3.5, 'petal_length': 1.5, 'petal_width': 0.2}
# {'id': 16, 'datetime': '1961-04-12 06:07:00.952414+00:00', 'species': 'virginica', 'sepal_length': 5.2, 'sepal_width': 3.4, 'petal_length': 1.4, 'petal_width': 0.2}
# {'id': 17, 'datetime': '1961-04-12 06:07:00.952431+00:00', 'species': 'setosa', 'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.6, 'petal_width': 0.2}
