****************
DataFrame Export
****************


Export data
===========
* File paths works also with DATAs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    import pandas as pd


    df = pd.DataFrame()

    # Important
    df.to_csv()
    df.to_dict()
    df.to_excel()
    df.to_json()
    df.to_sql()

    # Other
    df.to_clipboard()
    df.to_dense()
    df.to_feather()
    df.to_gbq()
    df.to_hdf()
    df.to_html()
    df.to_latex()
    df.to_msgpack()
    df.to_numpy()
    df.to_parquet()
    df.to_period()
    df.to_pickle()
    df.to_records()
    df.to_sparse()
    df.to_stata()
    df.to_string()
    df.to_timestamp()
    df.to_xarray()


Assignments
===========

.. todo:: Convert assignments to literalinclude

DataFrame Export CSV
--------------------
* Assignment: DataFrame Export CSV
* Filename: :download:`assignments/pandas_to_csv.py`
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``astro_eva1: pd.DataFrame``
    3. Export to file ``FILE`` data in ``CSV`` format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``astro_eva1: pd.DataFrame``
    3. Wyeksportuj do pliku ``FILE`` dane w formacie ``CSV``

Given:
    .. code-block:: python

        DATA = 'https://www.worldspaceflight.com/bios/eva/eva.php'
        FILE = r'_temporary.csv'

DataFrame Export JSON
---------------------
* Assignment: DataFrame Export JSON
* Filename: :download:`assignments/pandas_to_json.py`
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``astro_eva2: pd.DataFrame``
    3. Export to file ``FILE`` data in ``JSON`` format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``astro_eva2: pd.DataFrame``
    3. Wyeksportuj do pliku ``FILE`` dane w formacie ``JSON``

Given:
    .. code-block:: python

        DATA = r'https://www.worldspaceflight.com/bios/eva/eva2.php'
        FILE = r'_temporary.json'

DataFrame Export Pickle
-----------------------
* Assignment: DataFrame Export Pickle
* Filename: :download:`assignments/pandas_to_pickle.py`
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``astro_eva3: pd.DataFrame``
    3. Export to file ``FILE`` data in ``JSON`` format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``astro_eva3: pd.DataFrame``
    3. Wyeksportuj do pliku ``FILE`` dane w formacie ``JSON``

Given:
    .. code-block:: python

        DATA = r'https://www.worldspaceflight.com/bios/eva/eva3.php'
        FILE = r'_temporary.pkl'

DataFrame Export Pickle
-----------------------
* Assignment: DataFrame Export Pickle
* Filename: :download:`assignments/pandas_to_sql.py`
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``astro_eva4: pd.DataFrame``
    3. Export to file ``FILE`` data in ``SQL`` format
    4. Use table ``astro_eva``

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``astro_eva4: pd.DataFrame``
    3. Wyeksportuj do pliku ``FILE`` dane w formacie ``SQL``
    4. Użyj tabeli ``astro_eva``

Given:
    .. code-block:: python

        DATA = r'https://www.worldspaceflight.com/bios/eva/eva4.php'
        FILE = r'_temporary.sqlite3'

