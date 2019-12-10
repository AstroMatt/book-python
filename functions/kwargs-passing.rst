**********************
Passing many arguments
**********************


Arbitrary number of positional arguments
========================================
- ``*`` in this context, is not multiplication in mathematical sense
- ``*`` is used for positional arguments
- ``args`` is a convention, but you can use any name
- ``*args`` unpacks from ``tuple``, ``list`` or ``set``

.. code-block:: python
    :caption: Positional arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, 2)

.. code-block:: python
    :caption: Positional arguments passed from sequence

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1, 2)
    echo(*args)


Arbitrary number of keyword arguments
=====================================
- ``**`` in this context, is not power in mathematical sense
- ``**`` is used for keyword arguments
- ``kwargs`` is a convention, but you can use any name
- ``**kwargs`` unpacks from ``dict``

.. code-block:: python
    :caption: Keyword arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(a=1, b=2)

.. code-block:: python
    :caption: Keyword arguments passed from ``dict``

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    kwargs = {'a': 1, 'b': 2}
    echo(**kwargs)


Arbitrary number of positional and keyword arguments
====================================================
.. code-block:: python
    :caption: Positional and keyword arguments passed directly

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, b=2)

.. code-block:: python
    :caption: Positional and keyword arguments passed from sequence and ``dict``

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1,)
    kwargs = {'b': 2}

    echo(*args, **kwargs)


Examples
========

Creating complex numbers
------------------------
.. code-block:: python
    :caption: Defining complex number by passing keyword arguments directly

    complex(real=3, imag=5)
    # (3+5j)

.. code-block:: python
    :caption: Defining complex number by passing keyword arguments in ``dict``

    kwargs = {'real': 3, 'imag': 5}

    complex(**kwargs)
    # (3+5j)

Vectors
-------
.. code-block:: python
    :caption: Passing vector to the function

    def print_cartesian_coordinates(x, y, z):
        print(x)    # 1
        print(y)    # 0
        print(z)    # 1


    vector = (1, 0, 1)

    print_cartesian_coordinates(*vector)

Print formatting
----------------
* Now f-string formatting is preferred

.. code-block:: python
    :caption: ``str.format()`` expects keyword arguments, which keys are used in string. It is cumbersome to pass ``format(name=name, agency=agency)`` for every variable in the code.

    name = 'Jan Twardowski'
    agency = 'POLSA'

    output = "{agency} astronaut {name} first on the Moon".format(**locals())
    print(output)
    # POLSA astronaut Jan Twardowski first on the Moon

Common configuration
--------------------
.. code-block:: python
    :caption: Calling a function which has similar parameters

    def draw_line(x, y, color, type, width, markers):
        ...


    draw_line(1, 2, color='red', type='dashed', width='2px', markers='disc')
    draw_line(3, 4, color='red', type='dashed', width='2px', markers='disc')
    draw_line(5, 6, color='red', type='dashed', width='2px', markers='disc')

.. code-block:: python
    :caption: Passing configuration to the function, which sets parameters from the config

    def draw_chart(a, b, color, type, width, markers):
        ...


    style = {
        'color': 'red',
        'type': 'dashed',
        'width': '2px',
        'markers': 'disc',
    }

    draw_line(x=1, y=2, **style)
    draw_line(x=3, y=4, **style)
    draw_line(x=5, y=6, **style)

.. code-block:: python
    :caption: Database connection configuration read from config file

    config = {
        'host': 'localhost',
        'port': 5432,
        'username': 'my_username',
        'password': 'my_password',
        'database': 'my_database',
    }

    def database_connect(host, port, username, password, database):
        return ...

    connection = database_connect(**config)


Calling function with all variables from higher order function
--------------------------------------------------------------
.. code-block:: python
    :caption: Passing arguments to lower order function. ``locals()`` will return a ``dict`` with all the variables in local scope of the function.

    def lower(a, b, c, d, e):
        print(a, b, c, d, e)

    def higher(a, b, c=0):
        d = 4
        e = 5
        lower(**locals())
        # lower(a=a, b=b, c=c, d=d, e=e)


    higher(1, 2)
    # 1 2 0 4 5

Proxy functions
---------------
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.
    :emphasize-lines: 14

    # ``read_csv`` is a function from ``pandas`` library
    def read_csv(filepath_or_buffer, sep=', ', delimiter=None,
                 header='infer', names=None, index_col=None,
                 usecols=None, squeeze=False, prefix=None,
                 mangle_dupe_cols=True, dtype=None, engine=None,
                 converters=None, true_values=None, false_values=None,
                 skipinitialspace=False, skiprows=None, nrows=None,
                 na_values=None, keep_default_na=True, na_filter=True,
                 verbose=False, skip_blank_lines=True, parse_dates=False,
                 infer_datetime_format=False, keep_date_col=False,
                 date_parser=None, dayfirst=False, iterator=False,
                 chunksize=None, compression='infer', thousands=None,
                 decimal=b'.', lineterminator=None, quotechar='"',
                 quoting=0, escapechar=None, comment=None, encoding=None,
                 dialect=None, tupleize_cols=None, error_bad_lines=True,
                 warn_bad_lines=True, skipfooter=0, doublequote=True,
                 delim_whitespace=False, low_memory=True, memory_map=False,
                 float_precision=None):
        ...

    def my_csv(file, encoding='utf-8', *args, **kwargs):
        return read_csv(file, encoding=encoding, *args, **kwargs)


    my_csv('iris1.csv')
    my_csv('iris2.csv', encoding='iso-8859-2')
    my_csv('iris3.csv', encoding='cp1250', verbose=True)
    my_csv('iris4.csv', verbose=True)

Decorators
----------
.. code-block:: python
    :caption: Decorators are functions, which get pointer to the decorated function as it's argument, and has closure which gets original function arguments as positional and keyword arguments.

    def login_required(original_function):

        def wrapper(*args, **kwargs):
            user = kwargs['request'].user

            if user.is_authenticated():
                return original_function(*args, **kwargs)
            else:
                print('Permission denied')

        return wrapper


    @login_required
    def edit_profile(request):
        ...


Assignments
===========

Iris
----
* Filename: :download:`solution/kwargs_iris.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/functions/data/iris.csv

#. Otwórz link w przeglądarce i skopiuj zawartość do pliku na dysku o nazwie ``iris.csv``
#. Z pliku ``iris.csv`` odseparuj nagłówek i dane
#. Z nagłówka odrzuć rekord ``species``
#. Stwórz funkcję ``print_iris(species, **pomiary)``, która wyświetli zawartość wszystkich argumentów za pomocą ``locals()``
#. Dla każdego rekordu w danych:

    #. Usuń białe spacje
    #. Podziel po przecinku ``,``
    #. Wyniki podziału zapisz do dwóch zmiennych:

        * ``pomiary: Dict[str, float]`` - pomiary
        * ``gatunek: str`` - nazwa gatunku

    #. Odpalaj funkcję ``print_iris()``, podając wartości ``pomiary`` i ``gatunek``
    #. ``gatunek`` ma być podany pozycyjnie
    #. ``pomiary`` mają być podane nazwanie

