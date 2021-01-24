.. _Function Basics:

***************
Function Basics
***************


Function definition
===================
* Wielokrotne używanie tego samego kodu
* Poprawiają czytelność kodu
* Porządkują kod
* Pozwalają na łatwiejszy refactoring

.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez


Returning values
================
* ``return`` wskazuje funkcji jaką wartość ma zwrócić
* Kod po słowie kluczowym ``return`` się nie wykona

.. code-block:: python

    def hello():
        return 'ehlo world'

    output = hello()

    print(output)
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    output = hello()

    print(output)
    # 'ehlo world'

Returning simple types
----------------------
.. code-block:: python

    def function():
        return 42

.. code-block:: python

    def function():
        return 13.37

.. code-block:: python

    def function():
        return 'José Jiménez'

.. code-block:: python

    def function():
        return (42, 13.37, 'José Jiménez')

.. code-block:: python

    def function():
        return 42, 13.37, 'José Jiménez'

.. code-block:: python

    def function():
        return [42, 13.37, 'foobar']

.. code-block:: python

    def function():
        return {42, 13.37, 'José Jiménez'}

.. code-block:: python

    def function():
        return {'first_name': 'José', 'last_name': 'Jiménez'}

.. code-block:: python

    def function():
        return True

.. code-block:: python

    def function():
        return None

.. code-block:: python

    def function():
        print('ehlo world')
        # Python will ``return None`` if not specified

.. code-block:: python

    def function():
        pass
        # Python will ``return None`` if not specified

Returning nested types
----------------------
.. code-block:: python

    def function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Apollo')},
        ]

Function arguments
==================

Required arguments
------------------
.. code-block:: python

    def subtract(a, b):
        return a - b

Arguments with default value
----------------------------
* Funkcja przyjmie wartość domyślną dla argumentu jeżeli użytkownik nie nadpisze
* Argumenty z wartością domyślną muszą być skrajnie po prawej stronie
* Argumenty z wartościami domyślnymi nie muszą być podane

.. code-block:: python

    def subtract(a, b=2):
        return a - b

.. code-block:: python

    def subtract(a=1, b=2):
        return a - b

Positional arguments
--------------------
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(2, 1)      # 1
    subtract(1, 2)      # -1

Named arguments
---------------
* Argumenty bez wartości domyślnych są wymagane
* Kolejność podawania argumentów nazwanych nie ma znaczenia

.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(a=2, b=1)  # 1
    subtract(b=1, a=2)  # 1
    subtract(2, b=1)    # 1
    subtract(a=2, 1)    # SyntaxError: positional argument follows keyword argument

.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Иван Иванович')        # My name... Иван Иванович
    hello(name='Иван Иванович')   # My name... Иван Иванович
    hello()                       # My name... José Jiménez

.. code-block:: python

    def server(username, password, host='127.0.0.1',
               port=80, ssl=False, keep_alive=1,
               persistent=False):
        print('Connecting...')


    server('admin', 'admin', 'localhost', 80, False, 1, True)

    server(host='localhost', username='admin', password='admin', ssl=True, keep_alive=1, persistent=True)

    server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python
    :emphasize-lines: 6,10

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


    data = read_csv(
        filepath_or_buffer='iris-clean.csv',
        encoding='utf-8',
        verbose=True,
        usecols=['Sepal Length', 'Species']
    )


Naming convention
=================

Function name convention
------------------------
* It's not Java, do not use ``camelCase``

    .. code-block:: python

        def addNumbers(a, b):
            return a + b

* It's Python, use ``snake_case`` # Python - snake ;)

    .. code-block:: python

        def add_numbers(a, b):
            return a + b

Use better names, rather than comments
--------------------------------------
.. code-block:: python

    def cal_var(results):
        """Calculate variance"""
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

    def calculate_variance(results):
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

Name collisions
---------------
* ``_`` at the end of name when name collision

    .. code-block:: python

        def print_(text):
            print(f'<strong>{text}</strong>')

System functions names
----------------------
* ``__`` at the beginning and end of name

    .. code-block:: python

        def __import__(module_name):
            ...


Variable scope
==============

Global scope
------------
* All variables in main program
* Variables are available inside all functions

.. code-block:: python

    print(globals())
    # {...}

Local scope
-----------
* Variables defined inside function
* Variables are not available from outside

.. code-block:: python

    print(locals())
    # {...}

.. code-block:: python

    def add_numbers(a, b=2):
        c = 3
        print(locals())

    add_numbers(1)
    # {'a': 1, 'b': 2, 'c': 3}


Assignments
===========

Cleaning text input
-------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_str_clean.py`

#. Napisz funkcję oczyszczającą ciągi znaków
#. Funkcja musi przechodzić wszystkie ``doctest``

.. code-block:: python

    def clean(text: str) -> str:
        """
        >>> clean('  bolesława chrobrego ')
        'Bolesława Chrobrego'

        >>> clean('ul Jana III SobIESkiego')
        'Jana III Sobieskiego'

        >>> clean('\tul. Jana trzeciego Sobieskiego')
        'Jana III Sobieskiego'

        >>> clean('ulicaJana III Sobieskiego')
        'Jana III Sobieskiego'

        >>> clean('UL. JA\tNA 3 SOBIES  KIEGO')
        'Jana III Sobieskiego'

        >>> clean('UL. Zygmunta III WaZY')
        'Zygmunta III Wazy'

        >>> clean('ULICA JANA III SOBIESKIEGO  ')
        'Jana III Sobieskiego'

        >>> clean('ULICA. JANA III SOBIeskieGO')
        'Jana III Sobieskiego'

        >>> clean(' Jana 3 Sobieskiego  ')
        'Jana III Sobieskiego'

        >>> clean('Jana III Sobi\teskiego ')
        'Jana III Sobieskiego'

        >>> clean('ul.Mieszka II')
        'Mieszka II'
        """
        return text

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Czyszczenie danych od użytkownika

Aviation numbers
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_aviation_numbers.py`

#. Napisz funkcję ``aviation_numbers``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową w mowie pilotów
#. Funkcja musi przechodzić wszystkie ``doctest``

.. csv-table:: Aviation Phonetic Numbers
    :header-rows: 1
    :file: data/aviation-numbers.csv

.. code-block:: python

    def aviation_numbers(number: Union[int, float]) -> str:
        """
        >>> aviation_numbers(1969)
        'one niner six niner'

        >>> aviation_numbers(31337)
        'tree one tree tree seven'

        >>> aviation_numbers(13.37)
        'one tree and tree seven'

        >>> aviation_numbers(31.337)
        'tree one and tree tree seven'

        >>> aviation_numbers(-1969)
        'minus one niner six niner'

        >>> aviation_numbers(-31.337)
        'minus tree one and tree tree seven'

        >>> aviation_numbers(-49.35)
        'minus fower niner and tree fife'
        """
        return number

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Number to human readable
------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_numstr_human.py`

#. Napisz funkcję ``number_to_str``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową
#. Funkcja musi zmieniać wartości na poprawną gramatycznie formę
#. Max 6 cyfr przed przecinkiem
#. Max 5 cyfr po przecinku

    .. code-block:: python

        number_to_str(1969)      #
        number_to_str(13.37)     #
        number_to_str(31337)     #
        number_to_str(31.337)    #
        number_to_str(-1969)     #
        number_to_str(-31.337)   #

.. code-block:: python

    def number_to_text(number: Union[int, float]) -> str:
        """
        >>> number_to_text(1969)
        'one thousand nine hundred sixty nine'

        >>> number_to_text(31337)
        'thirty one thousand three hundred thirty seven'

        >>> number_to_text(13.37)
        'thirteen and thirty seven hundredths'

        >>> number_to_text(31.337)
        'thirty one three hundreds thirty seven thousands'

        >>> number_to_text(-1969)
        'minus one thousand nine hundred sixty nine'

        >>> number_to_text(-31.337)
        'minus thirty one three hundreds thirty seven thousands'

        >>> number_to_text(-49.35)
        'minus forty nine and thirty five hundreds'
        """
        return number

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Roman numbers
-------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_roman.py`

#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów
