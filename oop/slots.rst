.. _OOP Slots:

*****
Slots
*****


Rationale
=========
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Example
=======
.. code-block:: python

    class Astronaut:
        __slots__ = ()


    astro = Astronaut()

    astro.name = 'Mark Watney'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


``__slots__`` and ``__dict__``
==============================
* Using ``__slots__`` will prevent from creating ``__dict__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()
    astro.name = 'Mark Watney'

    print(astro.__slots__)
    # ('name',)

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

.. code-block:: python

    class Astronaut:
        __slots__ = ('__dict__', 'name')


    astro = Astronaut()
    astro.name = 'Mark Watney'   # will use __slots__
    astro.mission = 'Ares 3'     # will use __dict__

    print(astro.__slots__)
    # ('__dict__', 'name')

    print(astro.__dict__)
    # {'mission': 'Ares 3'}


Slots and Methods
=================
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def say_hello(self):
            print(f'My name... {self.name}')


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.say_hello()


Slots and Init
==============
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name)
            self.name = name


    astro = Astronaut('Mark Watney')
    print(astro.name)
    # Mark Watney

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name, mission):
            self.name = name
            self.mission = mission


    astro = Astronaut('Mark Watney', 'Ares 3')
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Inheritance
===========
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        pass


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'

    print(astro.mission)
    # Ares 3

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        __slots__ = ('name', 'mission')


    astro = Astronaut()
    astro.firstname = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)


    class Astronaut(Pilot):
        __slots__ = ('mission',)


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'


Use Cases
=========
.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()
    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.firstname)
    # Mark

    print(astro.lastname)
    # Watney

    print(astro.__slots__)
    # ('firstname', 'lastname')

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

    result = {attr: getattr(astro, attr)
              for attr in astro.__slots__}

    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
===========

.. todo:: Convert assignments to literalinclude

OOP Slots Define
----------------
* Assignment: OOP Slots Define
* Complexity: easy
* Lines of code: 11 lines
* Time: 13 min
* Filename: :download:`assignments/oop_slots_define.py`

English:
    #. Use code from "Input" section (see below)
    #. Define class ``Iris`` with attributes: ``sepal_length, sepal_width, petal_length, petal_width, species``
    #. All attributes must be in ``__slots__``
    #. Define method ``__repr__`` which prints class name and all values positionally, ie. ``Iris(5.8, 2.7, 5.1, 1.9, 'virginica')``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj klasę ``Iris`` z atrybutami: ``sepal_length, sepal_width, petal_length, petal_width, species``
    #. Wszystkie atrybuty muszą być w ``__slots__``
    #. Zdefiniuj metodę ``__repr__`` wypisującą nazwę klasy i wszystkie wartości atrybutów pozycyjnie, np. ``Iris(5.8, 2.7, 5.1, 1.9, 'virginica')``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa')]

Tests:
    >>> result = [Iris(*row) for row in DATA[1:]]
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
     Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
     Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
     Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
     Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
     Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]

    >>> iris = result[0]
    >>> iris
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

    >>> iris.__slots__
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> [getattr(iris, x) for x in iris.__slots__]
    [5.8, 2.7, 5.1, 1.9, 'virginica']

    >>> {x: getattr(iris, x) for x in iris.__slots__}
    {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'}

    >>> iris.__dict__
    Traceback (most recent call last):
    AttributeError: 'Iris' object has no attribute '__dict__'

    >>> values = tuple(getattr(iris, x) for x in iris.__slots__)
    >>> print(f'Iris{values}')
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

Hint:
    * In ``__repr__()`` use tuple comprehension to get ``self.__slots__`` values
