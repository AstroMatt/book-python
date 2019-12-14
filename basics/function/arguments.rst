******************
Function Arguments
******************


Simple Usage
============
.. code-block:: python

    def add(a, b):
        print(a + b)

    add(1, 2)
    # 3

    add(1.5, 2.5)
    # 4.0

.. code-block:: python

    def echo(text):
        print(text)

    echo('hello')
    # hello


Required arguments
==================
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract()
    # TypeError: subtract() missing 2 required positional arguments: 'a' and 'b'

    subtract(10)
    # TypeError: subtract() missing 1 required positional argument: 'b'

    subtract(10, 20)
    # -10


Arguments with default value
============================
.. highlights::
    * Arguments without default values are required
    * Function will take default value if not overwritten by user
    * Arguments with default values must be at the right side
    * Arguments with default values can be omitted while executing

.. code-block:: python

    def subtract(a=1, b=2):
        return a - b


    subtract()
    # -1

    subtract(10)
    # 8

    subtract(10, 20)
    # -10

.. code-block:: python

    def subtract(a, b=2):
        return a - b

.. code-block:: python

    def subtract(a=1, b):
        return a - b

    # SyntaxError: non-default argument follows default argument


Positional arguments
====================
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(2, 1)      # 1
    subtract(1, 2)      # -1


Keyword arguments
=================
.. highlights::
    * Arguments without default values are required
    * Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(a=2, b=1)  # 1
    subtract(b=1, a=2)  # 1
    subtract(2, b=1)    # 1
    subtract(2, a=1)    # TypeError: subtract() got multiple values for argument 'a'
    subtract(a=2, 1)    # SyntaxError: positional argument follows keyword argument

.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez


Example
=======
.. code-block:: python

    def connect(username, password, host='127.0.0.1',
                port=80, ssl=True, keep_alive=1, persistent=False):
        print('Connecting...')


    connect('admin', 'admin', 'localhost', 80, False, 1, True)

    connect(host='localhost', username='admin', password='admin', ssl=True, persistent=True, keep_alive=1)

    connect(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python

    def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
                 names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
                 mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
                 true_values=None, false_values=None, skipinitialspace=False,
                 skiprows=None, nrows=None, na_values=None, keep_default_na=True,
                 na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
                 infer_datetime_format=False, keep_date_col=False, date_parser=None,
                 dayfirst=False, iterator=False, chunksize=None, compression='infer',
                 thousands=None, decimal=b'.', lineterminator=None, quotechar='"',
                 quoting=0, escapechar=None, comment=None, encoding=None, dialect=None,
                 tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
                 skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True,
                 memory_map=False, float_precision=None):
        """
        Definition of pandas.read_csv() function
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        """

    my_file1 = read_csv('iris.csv')
    my_file2 = read_csv('iris.csv', encoding='utf-8')
    my_file3 = read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])
    my_file4 = read_csv('iris.csv', skiprows=3, delimiter=';')
    my_file5 = read_csv('iris.csv',
        encoding='utf-8',
        skiprows=3,
        delimiter=';',
        usecols=['Sepal Length', 'Species'],
        parse_dates=['date_of_birth']
    )


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/functions_example.py`

:English:
    #. For given input data (see below)
    #. Define ``wanted: Set[str]`` with 'setosa' and 'versicolor'
    #. Iterate over data and split row into ``features`` and ``label`` (last)
    #. Define function which sums ``features``, only when ``label`` is in ``wanted``
    #. When ``label`` is not in ``wanted`` return ``0`` (zero)
    #. Print sum

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj ``wanted: Set[str]`` z 'setosa' oraz 'versicolor'
    #. Iterując po danych rozdziel wiersz na ``features`` i ``label`` (ostatni)
    #. Zdefiniuj funkcję sumującą ``features``, tylko gdy ``label`` jest w ``wanted``
    #. Gdy ``label`` nie występuje w ``wanted`` zwróć ``0`` (zero)
    #. Wypisz sumę

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        OUTPUT: float
        # 74.9

:Solution:
    .. literalinclude:: solution/functions_example.py
        :language: python

Divide
------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/function_divide.py`

:English:
    #. Define function ``divide``
    #. Function takes two arguments
    #. Function returns result of a division for its arguments
    #. Call function with ``divide(10, 3)``
    #. Call function with ``divide(10, 0)``
    #. Print returned values
    #. What to do in case of error?

:Polish:
    #. Zdefiniuj funkcję ``divide``
    #. Funkcja przyjmuje dwa argumenty
    #. Funkcja zwraca wynik dzielenia jej argumentów
    #. Wywołaj funkcję z ``divide(10, 3)``
    #. Wywołaj funkcję z ``divide(10, 0)``
    #. Wypisz zwracane wartości
    #. Co zrobić w przypadku błędu?

Cleaning text input
-------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_str_clean.py`

:English:
    #. For given input data (see below)
    #. Write function cleaning up data
    #. Function takes one argument of type ``str``
    #. Function returns cleaned text

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst

:Input:
    .. code-block:: python

        INPUT = [
            'ul.Mieszka II',
            'UL. Zygmunta III WaZY',
            '  bolesława chrobrego ',
            'ul Jana III SobIESkiego',
            '\tul. Jana trzeciego Sobieskiego',
            'ulicaJana III Sobieskiego',
            'UL. JA    NA 3 SOBIES  KIEGO',
            'ULICA JANA III SOBIESKIEGO  ',
            'ULICA. JANA III SOBIeskieGO',
            ' Jana 3 Sobieskiego  ',
            'Jana III Sobi  eskiego ',
        ]

:Output:
    .. code-block:: python

        'Mieszka II'
        'Zygmunta III Wazy'
        'Bolesława Chrobrego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input

.. todo:: Translate input data to English

Aviation numbers
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_aviation_numbers.py`

:English:
    #. For input data (see below)
    #. Define function converting ``int`` or ``float`` to text form in Pilot's Speak

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów

:Input:
    .. code-block:: text

        0, "zero"
        1, "one"
        2, "two"
        3, "tree"
        4, "fower"
        5, "fife"
        6, "six"
        7, "seven"
        8, "ait"
        9, "niner"

    .. code-block:: python

        1969
        31337
        13.37
        31.337
        -1969
        -31.337
        -49.35

:Output:
    .. code-block:: python

        'one niner six niner'
        'tree one tree tree seven'
        'one tree and tree seven'
        'tree one and tree tree seven'
        'minus one niner six niner'
        'minus tree one and tree tree seven'
        'minus fower niner and tree fife'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups

Number to human readable
------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_numstr_human.py`

:English:
    #. For input data (see below)
    #. Define function converting ``int`` or ``float`` to text form
    #. Text form must be in proper grammar form
    #. Max 6 digits before decimal separator (point ``.``)
    #. Max 5 digits after decimal separator (point ``.``)

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową
    #. Forma tekstowa musi być poprawna gramatycznie
    #. Max 6 cyfr przed separatorem dziesiętnym (point ``.``)
    #. Max 5 cyfr po separatorze dziesiętnym (point ``.``)

:Input:
    .. code-block:: python

        1969
        31337
        13.37
        31.337
        -1969
        -31.337
        -49.35

:Output:
    .. code-block:: python

        'one thousand nine hundred sixty nine'
        'thirty one thousand three hundred thirty seven'
        'thirteen and thirty seven hundredths'
        'thirty one three hundreds thirty seven thousands'
        'minus one thousand nine hundred sixty nine'
        'minus thirty one and three hundreds thirty seven thousands'
        'minus forty nine and thirty five hundreds'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups

Roman numbers
-------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_roman.py`

:English:
    #. Define function converting roman numerals to integer
    #. Define function converting integer to roman numerals

:Polish:
    #. Zdefiniuj funkcję przeliczającą liczbę rzymską na całkowitą
    #. Zdefiniuj funkcję przeliczającą liczbę całkowitą na rzymską

:The whys and wherefores:
    * Defining and calling functions
    * Checking for corner cases
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups
