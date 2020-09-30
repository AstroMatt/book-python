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

DataFrame Export CSV
--------------------
* Assignment name: DataFrame Export CSV
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/df_export_csv.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``astro_eva1: pd.DataFrame``
    #. Export to file ``FILE`` data in ``CSV`` format

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``astro_eva1: pd.DataFrame``
    #. Wyeksportuj do pliku ``FILE`` dane w formacie ``CSV``

:Input:
    .. code-block:: python

        DATA = 'https://www.worldspaceflight.com/bios/eva/eva.php'
        FILE = 'astro-eva1.csv'

DataFrame Export JSON
---------------------
* Assignment name: DataFrame Export JSON
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/df_export_json.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``astro_eva2: pd.DataFrame``
    #. Export to file ``FILE`` data in ``JSON`` format

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``astro_eva2: pd.DataFrame``
    #. Wyeksportuj do pliku ``FILE`` dane w formacie ``JSON``

:Input:
    .. code-block:: python

        DATA = 'https://www.worldspaceflight.com/bios/eva/eva2.php'
        FILE = 'astro-eva2.json'

DataFrame Export Pickle
-----------------------
* Assignment name: DataFrame Export Pickle
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/df_export_pickle.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``astro_eva3: pd.DataFrame``
    #. Export to file ``FILE`` data in ``JSON`` format

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``astro_eva3: pd.DataFrame``
    #. Wyeksportuj do pliku ``FILE`` dane w formacie ``JSON``

:Input:
    .. code-block:: python

        DATA = 'https://www.worldspaceflight.com/bios/eva/eva3.php'
        FILE = 'astro-eva3.pkl'

DataFrame Export Pickle
-----------------------
* Assignment name: DataFrame Export Pickle
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/df_export_sql.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``astro_eva4: pd.DataFrame``
    #. Export to file ``FILE`` data in ``SQL`` format
    #. Use table ``astro_eva``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``astro_eva4: pd.DataFrame``
    #. Wyeksportuj do pliku ``FILE`` dane w formacie ``SQL``
    #. Użyj tabeli ``astro_eva``

:Input:
    .. code-block:: python

        DATA = 'https://www.worldspaceflight.com/bios/eva/eva4.php'
        FILE = 'astro-eva4.sqlite3'

