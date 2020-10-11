***************
Database SQLite
***************


Installation
============
#. To check if Sqlite3 is already installed run in Console/Terminal/CMD:

    .. code-block:: console

        $ sqlite3 --version

#. If it's not installed, then:

    * Download from https://sqlite.org/download.html
    * Extract archive
    * Add ``sqlite`` executable to ``$PATH``:

        * \*nix systems (Linux, macOS, etc...): move ``sqlite`` executable to ``/usr/local/bin/``
        * Windows (better): Add folder with extracted ``sqlite`` executable to ``$PATH`` directory by following instruction (https://python.astrotech.io/install.html)
        * Windows (simple): If you have GIT installed, move ``sqlite`` executable to ``C:\Program Files\Git\cmd``

    * Check if Sqlite3 is installed (Point 1.)


SQL Syntax
==========
.. note:: For SQL Syntax refer to :ref:`Database SQL`

Data Types
----------
.. list-table:: SQLite basic data types
    :widths: 10, 10, 80
    :header-rows: 1

    * - SQLite Type
      - Python Type
      - Description

    * - ``NULL``
      - ``None``
      - The value is a undefined value

    * - ``INTEGER``
      - ``int``
      - The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value

    * - ``REAL``
      - ``float``
      - The value is a floating point value, stored as an 8-byte IEEE floating point number

    * - ``TEXT``
      - ``str``
      - The value is a text string, stored using the database encoding (ie. UTF-8)

    * - ``BLOB``
      - ``bytes``
      - The value is a blob of data, stored exactly as it was input

.. csv-table:: SQLite extra data types
    :widths: 50, 50
    :header: "SQLite Type", "SQLite Alias"

    "``INTEGER``", "``INT``"
    "``INTEGER``", "``INTEGER``"
    "``INTEGER``", "``TINYINT``"
    "``INTEGER``", "``SMALLINT``"
    "``INTEGER``", "``MEDIUMINT``"
    "``INTEGER``", "``BIGINT``"
    "``INTEGER``", "``UNSIGNED BIG INT``"
    "``INTEGER``", "``INT2``"
    "``INTEGER``", "``INT8``"

    "``TEXT``", "``CHARACTER(20)``"
    "``TEXT``", "``VARCHAR(255)``"
    "``TEXT``", "``VARYING CHARACTER(255)``"
    "``TEXT``", "``NCHAR(55)``"
    "``TEXT``", "``NATIVE CHARACTER(70)``"
    "``TEXT``", "``NVARCHAR(100)``"
    "``TEXT``", "``TEXT``"
    "``TEXT``", "``CLOB``"

    "``REAL``", "``REAL``"
    "``REAL``", "``DOUBLE``"
    "``REAL``", "``DOUBLE PRECISION``"
    "``REAL``", "``FLOAT``"

    "``NUMERIC``", "``NUMERIC``"
    "``NUMERIC``", "``DECIMAL(10,5)``"
    "``NUMERIC``", "``BOOLEAN``"
    "``NUMERIC``", "``DATE``"
    "``NUMERIC``", "``DATETIME``"

Numeric
-------
A column with ``NUMERIC`` affinity may contain values using all five storage classes. When text data is inserted into a ``NUMERIC`` column, the storage class of the text is converted to INTEGER or REAL (in order of preference) if the text is a well-formed integer or real literal, respectively. If the TEXT value is a well-formed integer literal that is too large to fit in a 64-bit signed integer, it is converted to REAL.

Datetime
--------
SQLite does not have a storage class set aside for storing dates and/or times. Instead, the built-in Date And Time Functions of SQLite are capable of storing dates and times as TEXT, REAL, or INTEGER values:

* ``TEXT`` as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
* ``REAL`` as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
* ``INTEGER`` as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

Applications can chose to store dates and times in any of these formats and freely convert between formats using the built-in date and time functions.

Constrains
----------
.. csv-table:: SQL Constraints
    :header:  "Constraint", "Description"
    :widths: 15, 85

    "``NOT NULL``", "Ensures that a column cannot have a ``NULL`` value"
    "``UNIQUE``", "Ensures that all values in a column are different"
    "``PRIMARY KEY``", "A combination of a ``NOT NULL`` and ``UNIQUE``. Uniquely identifies each row in a table"
    "``FOREIGN KEY``", "Uniquely identifies a row/record in another table"
    "``CHECK``", "Ensures that all values in a column satisfies a specific condition"
    "``DEFAULT``", "Sets a default value for a column when no value is specified"
    "``INDEX``", "Used to create and retrieve data from the database very quickly"

DB API v2
=========
.. code-block:: python

    sqlite3.connect(...) -> connection

    connection.execute(...) -> result
    connection.executemany(...) -> list[result]
    connection.fetchmany(...) -> list[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
    connection.commit(...)
    connection.close()


Connection
==========
.. code-block:: python
    :caption: Connection to in-memory database

    import sqlite3

    DATABASE = ':memory:'

    with sqlite3.connect(DATABASE) as db:
        ...

.. code-block:: python
    :caption: Connection to database file

    import sqlite3

    DATABASE = r'/tmp/database.sqlite3'

    with sqlite3.connect(DATABASE) as db:
        ...


Execute
=======
.. code-block:: python
    :caption: Execute

    import sqlite3


    DATABASE = ':memory:'

    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT)"""

    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'

    DATA = {'pesel': '61041212345',
            'firstname': 'Mark',
            'lastname': 'Watney'}


    with sqlite3.connect(DATABASE) as db:
        db.execute(SQL_CREATE_TABLE)


Executemany
===========

``list[tuple]``
---------------
.. literalinclude:: src/database-executemany-tuple.py
    :language: python
    :caption: Execute many

``list[dict]``
--------------
.. literalinclude:: src/database-executemany-dict.py
    :language: python
    :caption: Execute many


Results
=======

Fetch as ``list[tuple]``
------------------------
.. literalinclude:: src/database-results.py
    :language: python
    :caption: Results

Fetch as ``list[dict]``
-----------------------
.. literalinclude:: src/database-results-dict.py
    :language: python
    :caption: Results with ``dict``


Cursor
======
.. literalinclude:: src/database-cursor.py
    :language: python
    :caption: Results with cursor


Use cases
=========
.. literalinclude:: src/database-case-study.py
    :name: listing-database-case-study
    :language: python
    :caption: Zapisywanie do bazy danych wyników pobranych z sensorów podłączonych po USB


Assignments
===========

Database SQLite Iris
--------------------
* Assignment name: Database SQLite Iris
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/database_sqlite_iris.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``FILE`` (don't use ``csv`` or ``pandas`` library)
    #. Reading data replace species ``int`` to ``str`` according to ``SPECIES`` conversion table
    #. Connect to the ``sqlite3`` using context manager (``with``)
    #. Create table ``iris`` with column specified in "Input" section
    #. Save data to database table
    #. Print results using ``SELECT * FROM iris ORDER BY datetime DESC``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``FILE`` (nie używaj biblioteki ``csv`` lub ``pandas``)
    #. Czytając dane podmień ``int`` z gatunkiem na ``str`` zgodnie z tabelą podstawień ``SPECIES``
    #. Połącz się do bazy danych ``sqlite3`` używając context managera (``with``)
    #. Stwórz tabelę ``iris`` o kolumnach podanych w sekcji "Input"
    #. Zapisz dane do tabeli w bazie danych
    #. Wypisz wyniki z bazy danych ``SELECT * FROM iris ORDER BY datetime DESC``

:Non functional requirements:
    * Add data in ``dict`` format using ``.executemany()``
    * Return data as ``sqlite3.Row``
    * Create index on ``datetime`` column
    * Save date and time to database in UTC

:The whys and wherefores:
    * Parsing ``csv`` files
    * Using ``sqlite3`` database
    * Creating database
    * Inserting data to database
    * Selecting data from database
    * Type casting
    * Using ``datetime`` and UTC timezone
    * Creating indexes (extra task)

:Input:
    .. code-block:: python

        DATABASE = r'database-sqlite-iris.sqlite3'
        FILE = r'database-sqlite-iris.csv'

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
                datetime DATETIME,
                species TEXT,
                sepal_length REAL,
                sepal_width REAL,
                petal_length REAL,
                petal_width REAL);"""

        SQL_CREATE_INDEX = """
            CREATE INDEX IF NOT EXISTS
                iris_datetime_index ON iris (datetime);"""

        SQL_INSERT = """
            INSERT INTO iris VALUES (
                NULL,
                :datetime,
                :species,
                :sepal_length,
                :sepal_width,
                :petal_length,
                :petal_width);"""

        SQL_SELECT = 'SELECT * FROM iris ORDER BY datetime DESC'

        with open(FILE, mode='w') as file:
            file.write(DATA)

Database SQLite Logs
--------------------
* Assignment name: Database SQLite Logs
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/database_sqlite_logs.py`

:English:
    #. Use data from "Input" section (see below)
    #. Save input data to file ``apollo11-timeline.log``
    #. Extract ``datetime`` object, level name and message from each line
    #. Collect data to ``DATA: list[dict]`` (see below)
    #. Create database schema for logs
    #. Add all logs to database
    #. Select only ``WARNING`` logs between 1969-07-20 and 1969-07-21
    #. Order logs by datetime descending
    #. Print ``result: list[dict]``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz dane wejściowe do pliku ``apollo11-timeline.log``
    #. Wyciągnij obiekt ``datetime``, poziom logowania oraz wiadomość z każdej linii
    #. Zbierz dane do ``DATA: list[dict]`` (patrz sekcja input)
    #. Stwórz schemat bazy danych dla logów
    #. Dodaj wszystkie linie do bazy danych
    #. Wybierz tylko logi ``WARNING`` z przedziału 1969-07-20 i 1969-07-21
    #. Posortuj logi w kolejności datetime malejąco
    #. Wyświetl ``result: list[dict]``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python
        :caption: Apollo 11 timeline https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

        DATA = """1969-07-14, 21:00:00, INFO, Terminal countdown started
        1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
        1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
        1969-07-16, 13:34:44, WARNING, S-II ignition
        1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
        1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
        1969-07-16, 16:22:13, INFO, Translunar injection
        1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
        1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
        1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
        1969-07-20, 17:44:00, INFO, CSM/LM undocked
        1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
        1969-07-20, 20:10:22, ERROR, LM 1202 alarm
        1969-07-20, 20:14:18, ERROR, LM 1201 alarm
        1969-07-20, 20:17:39, WARNING, LM lunar landing
        1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
        1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
        1969-07-21, 02:56:15, WARNING, That's one small step for [a] man... one giant leap for mankind
        1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
        1969-07-21, 03:15:16, INFO, LMP on lunar surface
        1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
        1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
        1969-07-21, 21:35:00, INFO, CSM/LM docked
        1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
        1969-07-24, 16:21:12, INFO, CM/SM separation
        1969-07-24, 16:35:05, WARNING, Entry
        1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
        1969-07-24, 17:29, INFO, Crew egress"""

:Output:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'date': datetime.datetime(1969, 7, 21, 17, 54, 00, tzinfo=datetime.timezone.utc),
          'level': 'WARNING',
          'message': 'LM lunar liftoff ignition (LM APS)'},

         {'date': datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
          'level': 'WARNING',
          'message': '1st step taken lunar surface (CDR) "That\'s one small step for [a] man... one giant leap for mankind"'},

         {'date': datetime.datetime(1969, 7, 20, 20, 17, 39, tzinfo=datetime.timezone.utc),
          'level': 'WARNING',
          'message': 'LM lunar landing'},

        ...]

Database SQLite Relations
-------------------------
* Assignment name: Database SQLite Relations
* Last update: 2020-10-11
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/database_sqlite_relations.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create database for input data
    #. Add support for many addresses
    #. Insert data to database
    #. Select data from database using JOIN relations

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz bazę danych na podstawie danych wejściowych
    #. Dodaj obsługę dla wielu adresów
    #. Zapisz dane do bazy
    #. Wypisz dane z bazy wykorzystując relację JOIN

:Input:
    .. code-block:: python

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

:Hint:
    .. code-block:: python

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
