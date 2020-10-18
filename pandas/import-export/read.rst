***********
Pandas Read
***********


Import data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    import pandas as pd


    # Important
    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sql()        # Read SQL query or database table into a DataFrame

    # Others
    pd.read_clipboard()
    pd.read_feather()
    pd.read_fwf()
    pd.read_gbq()
    pd.read_hdf()
    pd.read_msgpack()
    pd.read_parquet()
    pd.read_pickle()
    pd.read_sas()
    pd.read_spss()
    pd.read_sql_query()  # Read SQL query into a DataFrame
    pd.read_sql_table()  # Read SQL database table into a DataFrame
    pd.read_stata()
    pd.read_table()


Examples
========
.. code-block:: python

    import pandas as pd

    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-clean.csv
    header = pd.read_csv(DATA, nrows=0).columns

.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-clean.csv'
    df = pd.read_csv(DATA)

    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.4          3.9           1.3          0.4      setosa
    # 1           5.9          3.0           5.1          1.8   virginica
    # 2           6.0          3.4           4.5          1.6  versicolor

.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'
    COLUMNS =  ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'species']

    df = pd.read_csv(DATA)
    df.head(3)
    #      150    4  setosa  versicolor  virginica
    # 0    5.4  3.9     1.3         0.4          0
    # 1    5.9  3.0     5.1         1.8          2
    # 2    6.0  3.4     4.5         1.6          1

    df = pd.read_csv(url, skiprows=1, names=COLUMNS)
    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        0
    # 1           5.9          3.0           5.1          1.8        2
    # 2           6.0          3.4           4.5          1.6        1

    df['species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica',
    }, inplace=True)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        setosa
    # 1           5.9          3.0           5.1          1.8        virginica
    # 2           6.0          3.4           4.5          1.6        versicolor


Compressed
==========
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

.. code-block:: python

    df = pd.read_json('sample_file.gz', compression='infer')


Read HTML
=========
.. code-block:: python

    URL = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'

    pd.read_html(URL)
    # Traceback (most recent call last):
    #     ...
    # urllib.error.HTTPError: HTTP Error 403: Forbidden

.. code-block:: python

    import requests

    URL = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'

    resp = requests.get(URL, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})

    pd.read_html(resp.content)[0]
    #      Crew Role        Astronaut
    # 0   Prime  CDR   Neil Armstrong
    # 1   Prime  LMP      Buzz Aldrin
    # 2   Prime  CMP  Michael Collins
    # 3  Backup  CDR     James Lovell
    # 4  Backup  LMP   William Anders
    # 5  Backup  CMP       Fred Haise


StringIO
========
* Converts ``str`` to File-like object

.. code-block:: python

    from io import StringIO


    DATA = """
    "Crew", "Role", "Astronaut"
    "Prime", "CDR", "Neil Armstrong"
    "Prime", "LMP", "Buzz Aldrin"
    "Prime", "CMP", "Michael Collins"
    "Backup", "CDR", "James Lovell"
    "Backup", "LMP", "William Anders"
    "Backup", "CMP", "Fred Haise"
    """

    data = StringIO(DATA)
    pd.read_csv(data)
    #      Crew  "Role"         "Astronaut"
    # 0   Prime   "CDR"    "Neil Armstrong"
    # 1   Prime   "LMP"       "Buzz Aldrin"
    # 2   Prime   "CMP"   "Michael Collins"
    # 3  Backup   "CDR"      "James Lovell"
    # 4  Backup   "LMP"    "William Anders"
    # 5  Backup   "CMP"        "Fred Haise"

.. code-block:: python

    from io import StringIO


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-flights.csv'

    resp = requests.get(DATA)
    data = StringIO(resp.text)

    pd.read_csv(data)
    #      Order           Astronaut         Date       Mission
    # 0      1.0        Yuri Gagarin   1961-04-12        Vostok
    # 1      2.0       Gherman Titov   1961-08-06      Vostok 2
    # 2      3.0   Andrian Nikolayev   1962-08-11      Vostok 3
    # 3      4.0      Pavel Popovich   1962-08-12      Vostok 4
    # 4      5.0     Valeri Bykovsky   1963-06-14      Vostok 5
    # ..     ...                 ...          ...           ...
    # 530  531.0      Thomas Pesquet   2016-11-17   Soyuz MS-03
    # 531  532.0        Jack Fischer   2017-04-20   Soyuz MS-04
    # 532  533.0      Mark Vande Hei   2017-09-12   Soyuz MS-06
    # 533  534.0     Norishige Kanai   2017-12-17   Soyuz MS-07
    # 534    NaN        Scott Tingle   2017-12-17   Soyuz MS-07
    # [535 rows x 4 columns]


Read SQL
========
.. code-block:: python

    import sqlite3
    import requests

    DATABASE = r'/tmp/astro-timeline.sqlite3'
    URL = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/sqlite3/astro-timeline.sqlite3'
    SQL = r'SELECT * FROM logs'

    with open(DATABASE, mode='wb') as db:
        resp = requests.get(URL)
        db.write(resp.content)

    with sqlite3.connect(DATABASE) as db:
        astro_timeline = pd.read_sql(SQL, db, parse_dates=['datetime'])

    astro_timeline
    #     id  ...                                            message
    # 0    1  ...                         Terminal countdown started
    # 1    2  ...                          S-IC engine ignition (#5)
    # 2    3  ...          Maximum dynamic pressure (735.17 lb/ft^2)
    # 3    4  ...                                      S-II ignition
    # 4    5  ...                     Launch escape tower jettisoned
    # 5    6  ...                          S-II center engine cutoff
    # 6    7  ...                               Translunar injection
    # 7    8  ...                           CSM docked with LM/S-IVB
    # 8    9  ...                     Lunar orbit insertion ignition
    # 9   10  ...               Lunar orbit circularization ignition
    # 10  11  ...                                    CSM/LM undocked
    # 11  12  ...                 LM powered descent engine ignition
    # 12  13  ...                                      LM 1202 alarm
    # 13  14  ...                                      LM 1201 alarm
    # 14  15  ...                                   LM lunar landing
    # 15  16  ...                           EVA started (hatch open)
    # 16  17  ...                 1st step taken lunar surface (CDR)
    # 17  18  ...  That's one small step for [a] man... one giant...
    # 18  19  ...        Contingency sample collection started (CDR)
    # 19  20  ...                               LMP on lunar surface
    # 20  21  ...                           EVA ended (hatch closed)
    # 21  22  ...                 LM lunar liftoff ignition (LM APS)
    # 22  23  ...                                      CSM/LM docked
    # 23  24  ...                Transearth injection ignition (SPS)
    # 24  25  ...                                   CM/SM separation
    # 25  26  ...                                              Entry
    # 26  27  ...                     Splashdown (went to apex-down)
    # 27  28  ...                                        Crew egress
    # [28 rows x 4 columns]


Assignments
===========

Pandas Read CSV Dates
---------------------
* Assignment name: Pandas Read CSV Dates
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/pandas_read_csv_dates.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` to ``result: pd.DataFrame``
    #. Parse dates in "Mission Date" column
    #. Print ``result``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` do ``result: pd.DataFrame``
    #. Sparsuj daty w kolumnie "Mission Date"
    #. Wypisz ``result``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/martian-en.csv'

:Hints:
    * ``parse_dates`` argument

Pandas Read CSV Replace
-----------------------
* Assignment name: Pandas Read CSV Replace
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/pandas_read_csv_replace.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` to ``result: pd.DataFrame``
    #. Use provided column names in ``COLUMNS``
    #. Read labels from the first row
    #. Replace data in ``label`` column with values extracted above
    #. Print ``DataFrame``
    #. Print first 5 rows from ``result``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` do ``result: pd.DataFrame``
    #. Użyj podanych w ``COLUMNS`` nazw kolumn
    #. Wczytaj nazwy labeli z pierwszego wiersza
    #. Podmień dane w kolumnie ``label`` na wartości wyciągnięte powyżej
    #. Wypisz pierwsze 5 wierszy z ``result``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/breast-cancer.csv'

        COLUMNS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                   'mean smoothness', 'mean compactness', 'mean concavity',
                   'mean concave points', 'mean symmetry', 'mean fractal dimension',
                   'radius error', 'texture error', 'perimeter error', 'area error',
                   'smoothness error', 'compactness error', 'concavity error',
                   'concave points error', 'symmetry error',
                   'fractal dimension error', 'worst radius', 'worst texture',
                   'worst perimeter', 'worst area', 'worst smoothness',
                   'worst compactness', 'worst concavity', 'worst concave points',
                   'worst symmetry', 'worst fractal dimension', 'label']

:The whys and wherefores:
    * Read Pandas ``DataFrame``

:Hints:
    * ``pd.read_csv(url, nrows=0).columns``
    * ``df['label'].replace({'from': 'to'}, inplace=True)``

Pandas Read JSON
----------------
* Assignment name: Pandas Read JSON
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/pandas_read_json_iris.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``result: pd.DataFrame``
    #. Print ``result: pd.DataFrame``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    #. Wypisz ``result``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/iris.json'

Pandas Read JSON OpenAPI
------------------------
* Assignment name: Pandas Read JSON OpenAPI
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/pandas_read_json_openapi.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``result: pd.DataFrame``
    #. Use ``requests`` library
    #. Print ``result``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    #. Użyj biblioteki ``requests``
    #. Wypisz ``result``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/openapi.json'

Pandas Read HTML
----------------
* Assignment name: Pandas Read HTML
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/pandas_read_html.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``result: pd.DataFrame``
    #. Print ``result`` with active European Space Agency astronauts

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    #. Wypisz ``result`` z aktywnymi astronautami Europejskiej Agencji Kosmicznej

:Input:
    .. code-block:: python

        DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

:Hints:
    * Might require ``lxml`` and ``html5lib``: ``pip install --upgrade lxml html5lib``
    * 3rd table

Pandas Read XSLT Books
----------------------
* Assignment name: Pandas Read XSLT Books
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/pandas_read_xslt_books.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``result: pd.DataFrame``
    #. Use XSLT transformation
    #. Print ``result``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    #. Użyj transformaty XSLT
    #. Print ``result``

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xml/plants.xml'

:Hints:
    * Require ``lxml``: ``pip install lxml``

Pandas Read XSLT Plants
-----------------------
* Assignment name: Pandas Read XSLT Plants
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/pandas_read_xslt_plants.py`

:English:
    #. Use data from "Input" section (see below)
    #. Read data from ``DATA`` as ``result: pd.DataFrame``
    #. Use XSLT transformation
    #. Make sure that columns and indexes are named properly
    #. Calculate average cost of flower

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    #. Użyj transformaty XSLT
    #. Upewnij się, że nazwy kolumn i indeks są dobrze ustawione
    #. Wylicz średni koszt kwiatów

:Input:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xml/plants.xml'

:Hints:
    * Require ``lxml``: ``pip install lxml``
