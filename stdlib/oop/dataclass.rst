.. _Stdlib OOP Dataclass:

*************
OOP Dataclass
*************


Syntax
======
* This are not static fields!
* Dataclasses require Type Annotations
* Introduced in Python 3.7
* Backported to Python 3.6 via ``python3 -m pip install dataclasses``


Examples
========

Example 1
---------
.. code-block:: python
    :caption: ``class``

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z


    p0 = Point()
    # Traceback (most recent call last):
    # TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'

    p1 = Point(10)
    # Traceback (most recent call last):
    # TypeError: __init__() missing 1 required positional argument: 'y'

    p2 = Point(10, 20)
    p3 = Point(10, 20, 30)
    p4 = Point(10, 20, z=30)
    p5 = Point(10, 20, z=30)
    p6 = Point(x=10, y=20, z=30)

.. code-block:: python
    :caption: ``dataclass``

    from dataclasses import dataclass


    @dataclass
    class Point:
        x: int
        y: int
        z: int = 0


    p0 = Point()
    # Traceback (most recent call last):
    # TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'

    p1 = Point(10)
    # Traceback (most recent call last):
    # TypeError: __init__() missing 1 required positional argument: 'y'

    p2 = Point(10, 20)
    p3 = Point(10, 20, 30)
    p4 = Point(10, 20, z=30)
    p5 = Point(10, 20, z=30)
    p6 = Point(x=10, y=20, z=30)

Example 2
---------
.. code-block:: python
    :caption: ``class``

    class Astronaut:
        firstname: str
        lastname: str

        def __init__(self, firstname: str, lastname: str, agency: str = 'POLSA'):
            self.firstname = firstname
            self.lastname = lastname
            self.agency = agency


    twardowski = Astronaut('Jan', 'Twardowski')

    print(twardowski.firstname)   # Jan
    print(twardowski.lastname)    # Twardowski
    print(twardowski.agency)       # POLSA

.. code-block:: python
    :caption: ``dataclass``

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        firstname: str
        lastname: str
        agency: str = 'POLSA'


    twardowski = Astronaut('Jan', 'Twardowski')

    print(twardowski.firstname)   # Jan
    print(twardowski.lastname)    # Twardowski
    print(twardowski.agency)       # POLSA

Example 3
---------
.. code-block:: python
    :caption: ``class``

    from datetime import datetime


    class StarWarsMovie:
        title: str
        episode_id: int
        opening_crawl: str
        director: str
        producer: str
        release_date: datetime
        characters: tuple[str]
        planets: tuple[str]
        starships: tuple[str]
        vehicles: tuple[str]
        species: tuple[str]
        created: datetime
        edited: datetime
        url: str

        def __init__(self, title: str, episode_id: int, opening_crawl: str,
                     director: str, producer: str, release_date: datetime,
                     characters: tuple[str], planets: tuple[str], starships: tuple[str],
                     vehicles: tuple[str], species: tuple[str], created: datetime,
                     edited: datetime, url: str):

            self.title = title
            self.episode_id = episode_id
            self.opening_crawl= opening_crawl
            self.director = director
            self.producer = producer
            self.release_date = release_date
            self.characters = characters
            self.planets = planets
            self.starships = starships
            self.vehicles = vehicles
            self.species = species
            self.created = created
            self.edited = edited
            self.url = url

.. code-block:: python
    :caption: ``dataclass``

    from dataclasses import dataclass
    from datetime import datetime


    @dataclass
    class StarWarsMovie:
        title: str
        episode_id: int
        opening_crawl: str
        director: str
        producer: str
        release_date: datetime
        characters: tuple[str]
        planets: tuple[str]
        starships: tuple[str]
        vehicles: tuple[str]
        species: tuple[str]
        created: datetime
        edited: datetime
        url: str


``__init__`` vs. ``__post_init__``
==================================
.. code-block:: python
    :caption: ``class``

    class Kelvin:
        def __init__(self, value):
            if value < 0.0:
                raise ValueError('Temperature must be greater than 0')
            else:
                self.value = value


    t1 = Kelvin(273.15)

    print(t1.value)
    # 273.15

    t2 = Kelvin(-10)
    # Traceback (most recent call last):
    # ValueError: Temperature must be greater than 0

.. code-block:: python
    :caption: ``dataclass``

    from dataclasses import dataclass


    @dataclass
    class Kelvin:
        value: float = 0.0

        def __post_init__(self):
            if self.value < 0.0:
                raise ValueError('Temperature must be greater than 0')


    t1 = Kelvin(273.15)

    print(t1.value)
    # 273.15

    t2 = Kelvin(-10)
    # Traceback (most recent call last):
    # ValueError: Temperature must be greater than 0


Field Factory
=============
.. code-block:: python

    from dataclasses import dataclass, field


    @dataclass
    class Point:
        x: int
        y: int = field(repr=False)
        z: int = field(repr=False, default=10)
        t: int = 20


List attributes
===============
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer

.. warning:: Note, You should not set mutable objects as a default function argument. More information: :ref:`Argument Mutability <OOP Mutability Argument>`.

    .. code-block:: python
        :emphasize-lines: 2,10,14

        class Astronaut:
            def __init__(self, name, missions=[]):
                self.name = name
                self.missions = missions


        watney = Astronaut('Mark Watney')
        watney.missions.append('Ares 3')
        print(watney.missions)
        # [Ares 3]

        twardowski = Astronaut('Jan Twardowski')
        print(twardowski.missions)
        # [Ares 3]

.. code-block:: python
    :emphasize-lines: 7

    from dataclasses import dataclass, field


    @dataclass
    class Container:
        data: list[int] = field(default_factory=list)

    c = Container([1, 2, 3])
    c.data += [4, 5, 6]


Dataclass parameters
====================
.. csv-table:: Dataclass options
    :header: "Option", "Default", "Description (if True)"
    :widths: 10, 10, 80

    "``init``", "``True``", "Generate ``__init__()`` method"
    "``repr``", "``True``", "Generate ``__repr__()`` method"
    "``eq``", "``True``", "Generate ``__eq__()`` and ``__ne__()`` methods"
    "``order``", "``False``", "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    "``unsafe_hash``", "``False``", "if False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    "``frozen``", "``False``", "if ``True``: assigning to fields will generate an exception"

init
----
* Generate ``__init__()`` method

.. code-block:: python

    from dataclasses import dataclass


    @dataclass(init=False)
    class Point:
        x: int
        y: int


    p = Point(10, 20)
    # Traceback (most recent call last):
    # TypeError: Point() takes no arguments

repr
----
* ``repr=True`` by default
* Generate ``__repr__()`` for pretty printing

.. code-block:: python

    from dataclasses import dataclass

    @dataclass(repr=True)
    class Point:
        x: int
        y: int


    p = Point(10, 20)

    print(p)
    # Point(x=10, y=20)

.. code-block:: python

    from dataclasses import dataclass

    @dataclass(repr=False)
    class Point:
        x: int
        y: int


    p = Point(10, 20)

    print(p)
    # <__main__.Point object at 0x110bf5550>

frozen
------
* ``frozen=False`` by default
* Prevents object from modifications

.. code-block:: python

    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Point:
        x: int
        y: int


    p = Point(10, 20)

    p.x = 30
    # Traceback (most recent call last):
    # dataclasses.FrozenInstanceError: cannot assign to field 'x'

eq
--
* ``eq=True`` by default
* when ``eq=False`` compare objects by ``id()`` not values
* when ``eq=True`` compare objects by value not ``id()``

.. code-block:: python

    from dataclasses import dataclass

    @dataclass(eq=True)
    class Astronaut:
        firstname: str
        lastname: str


    astro1 = Astronaut('Mark', 'Watney')
    astro2 = Astronaut('Mark', 'Watney')
    astro3 = Astronaut('Jan', 'Twardowski')

    astro1 == astro1    # True
    astro1 == astro2    # True
    astro1 == astro3    # False

    astro1 != astro1    # False
    astro1 != astro2    # False
    astro1 != astro3    # True


.. code-block:: python

    from dataclasses import dataclass

    @dataclass(eq=False)
    class Astronaut:
        firstname: str
        lastname: str


    astro1 = Astronaut('Mark', 'Watney')
    astro2 = Astronaut('Mark', 'Watney')
    astro3 = Astronaut('Jan', 'Twardowski')

    astro1 == astro1    # True
    astro1 == astro2    # False
    astro1 == astro3    # False

    astro1 != astro1    # False
    astro1 != astro2    # True
    astro1 != astro3    # True

other flags
-----------
.. code-block:: python

    from dataclasses import dataclass

    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
    class Astronaut:
        firstname: str
        lastname: str

    astro1 = Astronaut('Mark', 'Watney')
    astro2 = Astronaut('Mark', 'Watney')
    astro3 = Astronaut('Jan', 'Twardowski')


Under the hood
==============
.. code-block:: python
    :caption: Your code

    from dataclasses import dataclass


    @dataclass
    class ShoppingCartItem:
        name: str
        unit_price: float
        quantity: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity

.. code-block:: python
    :caption: Dataclass will generate
    :emphasize-lines: 6-

    class ShoppingCartItem:

        def total_cost(self) -> float:
            return self.unit_price * self.quantity

        def __init__(self, name: str, unit_price: float, quantity: int = 0) -> None:
            self.name = name
            self.unit_price = unit_price
            self.quantity = quantity

        def __repr__(self):
            return f'ShoppingCartItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity={self.quantity!r})'

        def __eq__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) == (other.name, other.unit_price, other.quantity)
            return NotImplemented

        def __ne__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) != (other.name, other.unit_price, other.quantity)
            return NotImplemented

        def __lt__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) < (other.name, other.unit_price, other.quantity)
            return NotImplemented

        def __le__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) <= (other.name, other.unit_price, other.quantity)
            return NotImplemented

        def __gt__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) > (other.name, other.unit_price, other.quantity)
            return NotImplemented

        def __ge__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity) >= (other.name, other.unit_price, other.quantity)
            return NotImplemented

Examples
========
.. code-block:: python

    from dataclasses import dataclass


    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]


    @dataclass
    class Iris:
        sepal_length: int
        sepal_width: int
        petal_length: int
        petal_width: int
        species: str


    flowers = list(Iris(*row) for row in DATA[1:])
    print(flowers)
    # [
    #   Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
    #   Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
    #   Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
    #   Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
    #   Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
    #   Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa'),
    #   Iris(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4, species='versicolor'),
    #   Iris(sepal_length=7.6, sepal_width=3.0, petal_length=6.6, petal_width=2.1, species='virginica'),
    #   Iris(sepal_length=4.6, sepal_width=3.1, petal_length=1.5, petal_width=0.2, species='setosa')
    # ]


Assignments
===========

.. literalinclude:: solution/oop_dataclass_syntax.py
    :caption: :download:`Solution <solution/oop_dataclass_syntax.py>`
    :end-before: # Solution

.. literalinclude:: solution/oop_dataclass_addressbook.py
    :caption: :download:`Solution <solution/oop_dataclass_addressbook.py>`
    :end-before: # Solution

.. literalinclude:: solution/oop_dataclass_json.py
    :caption: :download:`Solution <solution/oop_dataclass_json.py>`
    :end-before: # Solution
