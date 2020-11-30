.. Unpacking Arguments:

*******************
Unpacking Arguments
*******************


Recap
=====
* argument - Value/variable/reference being passed to the function
* positional argument - Value passed to function - order is important
* keyword arguments - Value passed to function resolved by name - order is not important
* keyword arguments must be on the right side
* order of keyword arguments doesn't matter

.. code-block:: python

    echo(1)          # positional argument
    echo(a=1)        # keyword argument
    echo(1, 2)       # positional arguments
    echo(2, 1)       # positional arguments
    echo(a=1, b=2)   # keyword arguments
    echo(b=2, a=1)   # keyword arguments, order doesn't matter
    echo(1, b=2)     # positional and keyword arguments
    echo(a=1, 2)     # SyntaxError: positional argument follows keyword argument


Rationale
=========
.. figure:: img/unpacking-assignment,args,params.png
    :scale: 40%
    :align: center

    Unpacking and Arbitrary Number of Parameters and Arguments


Positional Arguments
====================
* ``*`` is used for positional arguments
* there is no convention, but you can use any name
* ``*`` unpacks from ``tuple``, ``list`` or ``set``

.. code-block:: python

    def echo(a, b, c=0):
        print(f'{a=}, {b=}, {c=}')


    echo(1, 2)
    # a=1, b=2, c=0

    data = (1, 2)
    echo(*data)
    # a=1, b=2, c=0

    data = (1, 2)
    echo(data)
    # Traceback (most recent call last):
    # TypeError: echo() missing 1 required positional argument: 'b'


Keyword Arguments
=================
* ``**`` is used for keyword arguments
* there is no convention, but you can use any name
* ``**`` unpacks from ``dict``

.. code-block:: python
    :caption: Keyword arguments passed directly

    def echo(a, b, c=0):
        print(f'{a=}, {b=}, {c=}')


    echo(a=1, b=2)
    # a=1, b=2, c=0

    data = {'a': 1, 'b': 2}
    echo(**data)
    # a=1, b=2, c=0


Positional and Keyword Arguments
================================
.. code-block:: python

    def echo(a, b, c=0):
        print(f'{a=}, {b=}, {c=}')

    echo(1, b=2)
    # a=1, b=2, c=0

    data1 = (1,)
    data2 = {'b': 2}
    echo(*data1, **data2)
    # a=1, b=2, c=0

    data1 = (1, 2)
    data2 = {'b': 2}
    echo(*data1, **data2)
    # Traceback (most recent call last):
    # TypeError: echo() got multiple values for argument 'b'


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


    result = Iris(*DATA)
    print(result.species)
    # 'versicolor'

.. code-block:: python

    DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


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
    # [virginica, setosa, versicolor,
    #  virginica, versicolor, setosa]

.. code-block:: python

    from dataclasses import dataclass

    MOVEMENT = [(0, 0),
                (1, 0),
                (2, 1, 1),
                (3, 2),
                (3, 3, -1),
                (2, 3)]


    @dataclass
    class Point:
        x: int
        y: int
        z: int = 0


    movement = [Point(x,y) for x,y in MOVEMENT]
    # Traceback (most recent call last):
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

    DATA = {"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"}

    class Iris:
        def __init__(self, sepalLength, sepalWidth, petalLength, petalWidth, species):
            self.sepal_length = sepalLength
            self.sepal_width = sepalWidth
            self.petal_length = petalLength
            self.petal_width = petalWidth
            self.species = species

    iris = Iris(**DATA)
    iris.species
    # 'virginica'

.. code-block:: python

    DATA = [{"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"},
            {"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},
            {"sepalLength":5.7,"sepalWidth":2.8,"petalLength":4.1,"petalWidth":1.3,"species":"versicolor"},
            {"sepalLength":6.3,"sepalWidth":2.9,"petalLength":5.6,"petalWidth":1.8,"species":"virginica"},
            {"sepalLength":6.4,"sepalWidth":3.2,"petalLength":4.5,"petalWidth":1.5,"species":"versicolor"},
            {"sepalLength":4.7,"sepalWidth":3.2,"petalLength":1.3,"petalWidth":0.2,"species":"setosa"}]


    class Iris:
        def __init__(self, sepalLength, sepalWidth, petalLength, petalWidth, species):
            self.sepal_length = sepalLength
            self.sepal_width = sepalWidth
            self.petal_length = petalLength
            self.petal_width = petalWidth
            self.species = species

        def __repr__(self):
            return f'{self.species}'


    result = [Iris(**row) for row in DATA]
    print(result)
    # [virginica, setosa, versicolor,
    #  virginica, versicolor, setosa]


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
        'host': 'example.com',
        'port': 5432,
        'username': 'myusername',
        'password': 'mypassword',
        'database': 'mydatabase'}


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

    def login_required(func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated():
                raise PermissionError
            return func(*args, **kwargs)
        return wrapper


    @login_required
    def edit_profile(request):
        ...


Assignments
===========

.. literalinclude:: solution/unpacking_arguments_define.py
    :caption: :download:`Solution <solution/unpacking_arguments_define.py>`
    :end-before: # Solution
