.. _Function Parameters:

*******************
Function Parameters
*******************


Rationale
=========
.. glossary::

    parameter
        Receiving variable used within the function/block

    default parameter
        Parameter which is optional and has default value (if not specified at call time)

    required parameter
        Parameter which is necessary to call function

Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    def my_function(<parameters>):
        <do something>

.. code-block:: python

    def add(a, b):
        print(a + b)


Required Parameters
===================
.. highlights::
    * Parameters without default values are required

.. code-block:: python

    def add(a, b):
        print(a + b)


    add()
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() missing 2 required positional arguments: 'a' and 'b'

    add(1)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() missing 1 required positional argument: 'b'

    add(1, 2)
    # 3

    add(1, 2, 3)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() takes 2 positional arguments but 3 were given


Default Parameters
==================
.. highlights::
    * Default parameters has default value
    * Function will use default value if not overwritten by user
    * Parameters with default values can be omitted while executing

.. code-block:: python

    def add(a=10, b=20):
        print(a + b)


    add()
    # 30

    add(1)
    # 21

    add(1, 2)
    # 3

    add(1, 2, 3)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() takes from 0 to 2 positional arguments but 3 were given


Required and Default Parameters
===============================
.. highlights::
    * Required parameters must be at the left side
    * Default parameters must be at the right side
    * There cannot be required parameter after optional

.. code-block:: python

    def add(a, b=20):
        print(a + b)


    add()
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() missing 1 required positional argument: 'a'

    add(1)
    # 21

    add(1, 2)
    # 3

    add(1, 2, 3)
    # Traceback (most recent call last):
    #     ...
    # TypeError: add() takes from 1 to 2 positional arguments but 3 were given

.. code-block:: python

    def add(a=1, b):
        print(a + b)

    # Traceback (most recent call last):
    #     ...
    # SyntaxError: non-default argument follows default argument

.. code-block:: python

    def add(a, b=1, c):
        print(a + b + c)

    # Traceback (most recent call last):
    #     ...
    # SyntaxError: non-default argument follows default argument


Examples
========
.. code-block:: python
    :caption: Example 1

    def add(a, b):
        print(a + b)


    add(1, 2)
    # 3

    add(1.5, 2.5)
    # 4.0

    add('a', 'b')
    # 'ab'

.. code-block:: python
    :caption: Example 2

    def echo(text):
        print(text)


    echo('hello')
    # hello

.. code-block:: python
    :caption: Example 3

    def connect(username, password, host='127.0.0.1', port=22,
                ssl=True, keep_alive=1, persistent=False):

        print('Connecting...')

.. code-block:: python
    :caption: Example 4. Definition of pandas.read_csv() function. Source:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

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

        print('Reading CSV...')


Assignments
===========

Function Parameters Sequence
----------------------------
* Assignment: Function Parameters Sequence
* Filename: function_parameters_sequence.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    #. Define function ``add``
    #. Function parameter is sequence of integers
    #. Print sum of all sequence values

Polish:
    #. Zdefiniuj funkcję ``add``
    #. Parametrem do funkcji ma być sekwencja liczb całkowitych
    #. Wypisz sumę wszystkich wartości sekwencji

Function Parameters Echo
------------------------
* Assignment: Function Parameters Echo
* Filename: function_parameters_echo.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    #. Define function ``echo`` with two parameters
    #. Parameter ``a`` is required
    #. Parameter ``b`` is required
    #. Wypisz ``a`` i ``b``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj funkcję ``echo`` z dwoma parametrami
    #. Parametr ``a`` jest wymagany
    #. Parametr ``b`` jest wymagany
    #. Wypisz ``a`` i ``b``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: python

        >>> echo(1, 2)
        a=1 b=2

        >>> echo(3, 4)
        a=3 b=4

Function Parameters Default
---------------------------
* Assignment: Function Parameters Default
* Filename: function_parameters_default.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min

English:
    #. Define function ``default`` with two parameters
    #. Parameter ``a`` is required
    #. Parameter ``b`` is optional and has default value ``None``
    #. If only one argument was passed, consider second equal to the first one
    #. Print ``a`` i ``b``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj funkcję ``default`` z dwoma parametrami
    #. Parametr ``a`` jest wymagany
    #. Parametr ``b`` jest opcjonalny i ma domyślną wartość ``None``
    #. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    #. Wypisz ``a`` i ``b``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: python

        >>> default(1)
        a=1 b=1

        >>> default(2, 3)
        a=2 b=3
