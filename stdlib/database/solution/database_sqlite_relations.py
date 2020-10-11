import sqlite3

DATABASE = r':memory:'

SQL_CREATE_TABLE_ASTRONAUT = """
    CREATE TABLE IF NOT EXISTS astronaut (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        firstname TEXT,
        lastname TEXT);"""

SQL_CREATE_TABLE_ADDRESS = """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP,
        astronaut_id INTEGER,
        street TEXT,
        city TEXT,
        state TEXT,
        code INT,
        country TEXT);"""

SQL_CREATE_INDEX_ASTRONAUT_LASTNAME = """
    CREATE UNIQUE INDEX IF NOT EXISTS lastname_index ON astronaut (lastname);"""

SQL_INSERT_ASTRONAUT = """
    INSERT INTO astronaut VALUES (
        NULL,
        CURRENT_TIMESTAMP,
        :firstname,
        :lastname);"""

SQL_INSERT_ADDRESS = """
    INSERT INTO address VALUES (
        NULL,
        CURRENT_TIMESTAMP,
        :astronaut_id,
        :street,
        :city,
        :state,
        :code,
        :country);"""

SQL_SELECT = """
    SELECT *
    FROM astronaut
    JOIN address
    ON astronaut.id=address.astronaut_id;
"""

DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "code": 77058, "city": "Houston", "state": "Texas", "country": "USA"},
        {"street": None, "code": 32899, "city": "Kennedy Space Center", "state": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "code": 91109, "city": "Pasadena", "state": "California", "country": "USA"},
        {"street": "2825 E Ave P", "code": 93550, "city": "Palmdale", "state": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "code": None, "city": "Космодро́м Байкону́р", "state": "Кызылординская область", "country": "Қазақстан"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "code": 51147, "state": None, "country": "Germany"}]}
]


with sqlite3.connect(DATABASE) as connection:
    db = connection.cursor()
    db.row_factory = sqlite3.Row

    db.execute(SQL_CREATE_TABLE_ASTRONAUT)
    db.execute(SQL_CREATE_TABLE_ADDRESS)
    db.execute(SQL_CREATE_INDEX_ASTRONAUT_LASTNAME)

    for astronaut in DATA:
        addresses = astronaut.pop('addresses')
        db.execute(SQL_INSERT_ASTRONAUT, astronaut)
        astronaut_id = db.lastrowid

        for addr in addresses:
            addr['astronaut_id'] = astronaut_id
            db.execute(SQL_INSERT_ADDRESS, addr)

    for row in db.execute(SQL_SELECT):
        print(dict(row))
