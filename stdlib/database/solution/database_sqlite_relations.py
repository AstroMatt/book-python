import sqlite3
from datetime import datetime

DATABASE = r'/tmp/_temporary.sqlite3'

SQL_CREATE_TABLE_CONTACT = """
    CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created DATETIME,
        modified DATETIME,
        firstname TEXT,
        lastname TEXT,
        date_of_birth DATE);"""

SQL_CREATE_TABLE_ADDRESS = """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER,
        street TEXT,
        city TEXT,
        state TEXT,
        code INT,
        country TEXT);"""

SQL_CREATE_INDEX_CONTACT_LASTNAME = """
    CREATE UNIQUE INDEX IF NOT EXISTS lastname_index ON contact (lastname);"""

SQL_CREATE_INDEX_CONTACT_MODIFIED = """
    CREATE INDEX IF NOT EXISTS modified_index ON contact (modified);"""

SQL_INSERT_CONTACT = """
    INSERT INTO contact VALUES (
        NULL,
        :created,
        :modified,
        :firstname,
        :lastname,
        :date_of_birth);"""

SQL_INSERT_ADDRESS = """
    INSERT INTO address VALUES (
        NULL,
        :contact_id,
        :street,
        :city,
        :state,
        :code,
        :country);"""

SQL_UPDATE_CONTACT = """
    UPDATE contact SET
        firstname=:firstname,
        lastname=:lastname,
        modified=:modified
    WHERE id=:id;"""

SQL_SELECT_CONTACT = """
    SELECT * FROM contact;"""

SQL_SELECT = """
    SELECT *
    FROM contact
    JOIN address
    ON contact.id=address.contact_id;
"""

DATA = """
José, Jiménez
    2101 E NASA Pkwy, 77058, Houston, Texas, USA
    , Kennedy Space Center, 32899, Florida, USA

Mark, Watney
    4800 Oak Grove Dr, 91109, Pasadena, California, USA
    2825 E Ave P, 93550, Palmdale, California, USA

Иван, Иванович
    Kosmodrom Bajkonur, Bajkonur, Kazachstan

Melissa Lewis,
    <NO ADDRESS>

Alex Vogel
    Linder Hoehe, 51147, Köln, Germany
"""

addressbook = [
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

addresses = []

for i, contact in enumerate(addressbook, start=1):
    contact['created'] = datetime.now()
    contact['modified'] = datetime.now()
    contact['date_of_birth'] = None
    addr = contact.pop('addresses')

    for a in addr:
        a['contact_id'] = i
        addresses.append(a)

with sqlite3.connect(DATABASE) as db:
    db.row_factory = sqlite3.Row
    db.execute(SQL_CREATE_TABLE_CONTACT)
    db.execute(SQL_CREATE_TABLE_ADDRESS)
    db.execute(SQL_CREATE_INDEX_CONTACT_LASTNAME)
    db.execute(SQL_CREATE_INDEX_CONTACT_MODIFIED)

    try:
        db.executemany(SQL_INSERT_CONTACT, addressbook)
        db.executemany(SQL_INSERT_ADDRESS, addresses)
    except sqlite3.IntegrityError:
        pass

    cursor = db.cursor()
    for row in cursor.execute(SQL_SELECT):
        print(dict(row))
