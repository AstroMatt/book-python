.. _OOP Dataclass:

*************
OOP Dataclass
*************


Syntax
======
* This are not static fields!
* Dataclasses require Type Annotations
* Introduced in Pyton 3.7
* Backported to Python 3.6 via ``pip install dataclasses``


Examples
========
.. code-block:: python
    :caption: Defining classes

    class Point:
        def __init__(self, x=0, y=0, z=0):
            self.x = x
            self.y = y
            self.z = z

    p = Point(x=10, y=20, z=30)

.. code-block:: python
    :caption: Defining dataclasses

    from dataclasses import dataclass


    @dataclass
    class Point:
        x: int
        y: int
        z: int

    p = Point(x=10, y=20, z=30)

Example 2
---------
.. code-block:: python
    :caption: Defining classes

    class Astronaut:
        def __init__(self, first_name: str, last_name: str, agency: str = 'POLSA'):
            self.first_name = first_name
            self.last_name = last_name
            self.agency = agency


    twardowski = Astronaut(first_name='Jan', last_name='Twardowski')

    twardowski.first_name   # Jan
    twardowski.last_name    # Twardowski
    twardowski.agency       # POLSA

.. code-block:: python
    :caption: Defining dataclasses

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        first_name: str
        last_name: str
        agency: str = 'POLSA'


    twardowski = Astronaut(first_name='Jan', last_name='Twardowski')

    twardowski.first_name   # Jan
    twardowski.last_name    # Twardowski
    twardowski.agency       # POLSA


``__init__`` vs. ``__post_init__``
==================================

Classes
-------
.. code-block:: python

    class Kelvin:
        def __init__(self, value):
            if value < 0.0:
                raise ValueError('Temperature must be greater than 0')
            else:
                self.value = value


    temp = Kelvin(-300)

Dataclasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Kelvin:
        value: float = 0.0

        def __post_init__(self):
            if self.value < 0.0:
                raise ValueError('Temperature must be greater than 0')


    temp = Kelvin(-300)


Field Factory
=============
.. code-block:: python

    from dataclasses import dataclass, field


    @dataclass
    class C:
        x: int
        y: int = field(repr=False)
        z: int = field(repr=False, default=10)
        t: int = 20

.. code-block:: python

    from dataclasses import dataclass, field


    @dataclass
    class C:
        my_list: list = field(default_factory=list)


    c = C([1, 2, 3])
    c.my_list += [4]


.. code-block:: python

    from dataclasses import dataclass, field
    from typing import List


    @dataclass
    class C:
        my_list: List[int] = field(default_factory=list)

    c = C()
    c.my_list += [1, 2, 3]

Why?
----
* :ref:`Initial arguments mutability and shared state`

.. code-block:: python

    class Contact:
        def __init__(self, name, addresses=[]):
            self.name = name
            self.addresses = addresses


    twardowski = Contact(name='Jan Twardowski')
    twardowski.addresses.append('Johnson Space Center')
    print(twardowski.addresses)
    # [Johnson Space Center]

    watney = Contact(name='Mark Watney')
    print(watney.addresses)
    # [Johnson Space Center]

So what?
--------
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer



Use cases
=========

Old style classes
-----------------
.. code-block:: python

    class StarWarsMovie:

        def __init__(self, title: str, episode_id: int, opening_crawl: str,
                     director: str, producer: str, release_date: datetime,
                     characters: Tuple[str], planets: Tuple[str], starships: Tuple[str],
                     vehicles: Tuple[str], species: Tuple[str], created: datetime,
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

            if type(self.release_date) is str:
                self.release_date = dateutil.parser.parse(self.release_date)

            if type(self.created) is str:
                self.created = dateutil.parser.parse(self.created)

            if type(self.edited) is str:
                self.edited = dateutil.parser.parse(self.edited)

Dataclasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class StarWarsMovie:
        title: str
        episode_id: int
        opening_crawl: str
        director: str
        producer: str
        release_date: datetime
        characters: Tuple[str]
        planets: Tuple[str]
        starships: Tuple[str]
        vehicles: Tuple[str]
        species: Tuple[str]
        created: datetime
        edited: datetime
        url: str

        def __post_init__(self):
            if type(self.release_date) is str:
                self.release_date = dateutil.parser.parse(self.release_date)

            if type(self.created) is str:
                self.created = dateutil.parser.parse(self.created)

            if type(self.edited) is str:
                self.edited = dateutil.parser.parse(self.edited)


More advanced options
=====================
.. code-block:: python

    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)

.. csv-table:: More advanced options
    :header: "Option", "Default", "Description (if True)"

    "``init``", "``True``", "Generate ``__init__()`` method"
    "``repr``", "``True``", "Generate ``__repr__()`` method"
    "``eq``", "``True``", "Generate ``__eq__()`` method"
    "``order``", "``False``", "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    "``unsafe_hash``", "``False``", "if False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    "``frozen``", "``False``", "if ``True``: assigning to fields will generate an exception"



Under the hood
==============

Write
-----
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class ShoppingCartItem:
        name: str
        unit_price: float
        quantity: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity

Dataclass will add
------------------
.. code-block:: python
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
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]


    @dataclass
    class Iris:
        sepal_length: int
        sepal_width: int
        petal_length: int
        petal_width: int
        species: str


    header, *data = INPUT
    flowers = list(Iris(*row) for row in data)

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

Address Book (dataclass)
------------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/dataclass_addressbook.py`

:English:
    #. Model data using ``dataclasses``

:Polish:
    #. Zamodeluj dane wykorzystując ``dataclass``

:Input:
    .. code-block:: json
        :caption: Data for AddressBook

        [
            {"first_name": "Jan", "last_name": "Twardowski", "addresses": [
                {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

            {"first_name": "José", "last_name": "Jiménez", "addresses": [
                {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
                {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

            {"first_name": "Mark", "last_name": "Watney", "addresses": [
                {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
                {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

            {"first_name": "Иван", "last_name": "Иванович", "addresses": [
                {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
                {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

            {"first_name": "Melissa", "last_name": "Lewis", "addresses": []},

            {"first_name": "Alex", "last_name": "Vogel", "addresses": [
                {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
        ]

Deserialize data from API
-------------------------
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 30 min
* Solution: :download:`solution/dataclass_json.py`

:English:
    #. You received input data in JSON format from the API
    #. Using ``dataclass`` Model data as class ``User``
    #. Parse fields with dates and store as ``datetime`` objects
    #. Parse fields with ``true`` and ``false`` values and store as ``bool`` objects
    #. Iterate over records and create instances of this class
    #. Collect all instances to one list

:Polish:
    #. Otrzymałeś z API dane wejściowe w formacie JSON
    #. Wykorzystując ``dataclass`` zamodeluj dane za pomocą klasy ``User``
    #. Sparsuj pola zwierające daty i zapisz je jako obiekty ``datetime``
    #. Sparsuj pola zawierające ``true`` lub ``false`` i zapamiętaj ich wartości jako obiekty ``bool``
    #. Iterując po rekordach twórz instancje tej klasy
    #. Zbierz wszystkie instancje do jednej listy

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Serialize and deserialize nested objects
    * Model data from API

:Input:
    .. code-block:: text

        [{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Jan","last_name":"Twardowski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]
