*****************************
Arbitrary Number of Arguments
*****************************


Positional Arguments
====================
* ``*`` is used for positional arguments
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks from ``tuple``, ``list`` or ``set``

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

.. code-block:: python
    :caption: Positional arguments passed from sequence

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1, 2)
    echo(args)
    # Traceback (most recent call last):
    #    ...
    # TypeError: echo() missing 1 required positional argument: 'b'


Keyword Arguments
=================
* ``**`` is used for keyword arguments
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks from ``dict``

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


Positional and Keyword Arguments
================================
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


Objects From Sequence
=====================
.. code-block:: python

    DATA = (6.0, 3.4, 4.5, 1.6, 'versicolor')

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    iris = Iris(*DATA)
    iris.species
    # 'versicolor'

.. code-block:: python

    DATA = [
        (6.0, 3.4, 4.5, 1.6, 'versicolor'),
        (4.9, 3.1, 1.5, 0.1, 'setosa'),
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'{self.species}'

    result = [Iris(*row) for row in DATA]
    print(result)
    # [versicolor, setosa]

.. code-block:: python

    from dataclasses import dataclass

    MOVEMENT = [
        (0, 0),
        (1, 0),
        (2, 1, 1),
        (3, 2),
        (3, 3, -1),
        (2, 3),
    ]

    @dataclass
    class Point:
        x: int
        y: int
        z: int = 0

    movement = [Point(x,y) for x,y in MOVEMENT]
    # ValueError: too many values to unpack (expected 2)

    movement = [Point(*coordinates) for coordinates in MOVEMENT]

    movement
    # [Point(x=0, y=0, z=0),
    #  Point(x=1, y=0, z=0),
    #  Point(x=2, y=1, z=1),
    #  Point(x=3, y=2, z=0),
    #  Point(x=3, y=3, z=-1),
    #  Point(x=2, y=3, z=0)]


Objects From Mappings
=====================
.. code-block:: python

    DATA = {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"}

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    iris = Iris(**DATA)
    iris.species
    # 'versicolor'

.. code-block:: python

    DATA = [
        {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1, "species": "setosa"},
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'{self.species}'


    result = [Iris(**row) for row in DATA]
    print(result)
    # ['versicolor', 'setosa']


Examples
========
.. code-block:: python
    :caption: Defining complex number by passing keyword arguments directly

    complex(real=3, imag=5)
    # (3+5j)


    number = {'real': 3, 'imag': 5}
    complex(**number)
    # (3+5j)


.. code-block:: python
    :caption: Passing vector to the function

    def cartesian_coordinates(x, y, z):
        print(x)    # 1
        print(y)    # 0
        print(z)    # 1


    vector = (1, 0, 1)
    cartesian_coordinates(*vector)

.. code-block:: python
    :caption: Passing point to the function

    def cartesian_coordinates(x, y, z):
        print(x)    # 1
        print(y)    # 0
        print(z)    # 1


    point = {'x': 1, 'y': 0, 'z': 1}
    cartesian_coordinates(**point)

.. code-block:: python
    :caption: ``str.format()`` expects keyword arguments, which keys are used in string. It is cumbersome to pass ``format(name=name, agency=agency)`` for every variable in the code. Since Python 3.6 f-string formatting are preferred.

    firstname = 'Jan'
    lastname = 'Twardowski'
    location = 'Moon'

    result = 'Astronaut {firstname} {lastname} on the {location}'.format(**locals())
    print(result)
    # Astronaut Jan Twardowski on the Moon

.. code-block:: python
    :caption: Calling a function which has similar parameters. Passing configuration to the function, which sets parameters from the config

    def draw_line(x, y, color, type, width, markers):
        ...


    draw_line(x=1, y=2, color='red', type='dashed', width='2px', markers='disc')
    draw_line(x=3, y=4, color='red', type='dashed', width='2px', markers='disc')
    draw_line(x=5, y=6, color='red', type='dashed', width='2px', markers='disc')


    style = {'color': 'red',
             'type': 'dashed',
             'width': '2px',
             'markers': 'disc'}

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
        'database': 'my_database'}


    def database_connect(host, port, username, password, database):
        return ...


    connection = database_connect(**config)

.. code-block:: python
    :caption: Calling function with all variables from higher order function. ``locals()`` will return a ``dict`` with all the variables in local scope of the function.

    def template(template, **user_data):
        print('Template:', template)
        print('Data:', user_data)


    def controller(firstname, lastname, uid=0):
        groups = ['admins', 'astronauts']
        permission = ['all', 'everywhere']
        return template('user_details.html', **locals())

        # template('user_details.html',
        #    firstname='Jan',
        #    lastname='Twardowski',
        #    uid=0,
        #    groups=['admins', 'astronauts'],
        #    permission=['all', 'everywhere'])


    controller('Jan', 'Twardowski')
    # Template: user_details.html
    # Data: {'firstname': 'Jan',
    #        'lastname': 'Twardowski',
    #        'uid': 0,
    #        'groups': ['admins', 'astronauts'],
    #        'permission': ['all', 'everywhere']}

.. code-block:: python
    :caption: Proxy functions. One of the most common use of ``*args``, ``**kwargs``.

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


    def mycsv(file, encoding='utf-8', decimal=b',',
              lineterminator='\n', *args, **kwargs):

        return read_csv(file, encoding=encoding, decimal=decimal,
                        lineterminator=lineterminator, *args, **kwargs)


    mycsv('iris1.csv')
    mycsv('iris2.csv', encoding='iso-8859-2')
    mycsv('iris3.csv', encoding='cp1250', verbose=True)
    mycsv('iris4.csv', verbose=True, usecols=['Sepal Length', 'Species'])

.. code-block:: python
    :caption: Decorators. Decorators are functions, which get pointer to the decorated function as it's argument, and has closure which gets original function arguments as positional and keyword arguments.

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

Function Args/Kwargs Arguments Define
-------------------------------------
* Assignment name: Function Args/Kwargs Arguments Define
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_argskwargs_arguments_define.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create function ``mean(*args)``, which calculates arithmetic mean for ``args``
    #. Do not import any libraries and modules
    #. Separate header from data
    #. Define ``result: list[tuple[str, float]]``
    #. Iterate over ``DATA`` separating ``features`` from ``label``
    #. To ``result`` append ``label`` and arithmetic mean of ``features``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz funkcję ``mean(*args)``, która liczy średnią arytmetyczną dla ``args``
    #. Nie importuj żadnych biliotek i modułów
    #. Odseparuj nagłówek od danych
    #. Zdefiniuj ``result: list[tuple[str, float]]``
    #. Iteruj po ``DATA`` separując ``features`` od ``label``
    #. Do ``result`` dodawaj ``label`` oraz wynik średniej arytmetycznej ``features``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 5.7, 'virginica'),
            (6.4, 1.5, 'versicolor'),
            (4.7,  'setosa'),
        ]

:Output:
    .. code-block:: text

        >>> mean(1)
        1.0

        >>> mean(1, 3)
        2.0

        >>> mean(1, 2, 3)
        2.0

        >>> mean()
        Traceback (most recent call last):
            ...
        ValueError: At least one argument is required

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [('virginica', 3.875),
         ('setosa', 2.65),
         ('versicolor', 3.475),
         ('virginica', 6.0),
         ('versicolor', 3.95),
         ('setosa', 4.7)]

