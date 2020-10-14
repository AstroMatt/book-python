.. _OOP Dynamic Typing:

**************
Dynamic Typing
**************


Duck typing
===========
* `The Unreasonable Effectiveness of Dynamic Typing for Practical Programs by Robert Smallshire <http://www.infoq.com/presentations/dynamic-static-typing>`_

.. code-block:: python
    :caption: Syntax similarities

    data = {1}
    isinstance(data, set)   # True
    isinstance(data, dict)  # False

    data = {1: 1}
    isinstance(data, set)   # False
    isinstance(data, dict)  # True

    data = {}
    isinstance(data, set)   # False
    isinstance(data, dict)  # True

.. code-block:: python

    data = {1:1}

    type(data)
    # <class 'dict'>
    data
    # {1:1}

    _ = data.pop(1)

    type(data)
    # <class 'dict'>
    data
    # {}

.. code-block:: python

    data = {1}

    type(data)
    # <class 'set'>
    data
    # {1}

    _ = data.pop()

    type(data)
    # <class 'set'>
    data
    # set()


Everything is an object
=======================
* even function is an object!

Object properties
-----------------
.. code-block:: python

    def add_numbers(a: int, b: float) -> float:
        """Function add numbers"""
        return a + b


    print(add_numbers.__doc__)
    # Function add numbers

    print(add_numbers.__name__)
    # add_numbers

    print(add_numbers.__annotations__)
    # {'a': <class 'int'>, 'b': <class 'float'>, 'return': <class 'float'>}

    print(add_numbers.__class__)
    # <class 'function'>

Object methods
--------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers(1, 2)
    # 3

    add_numbers.__call__(1, 2)
    # 3

    add_numbers()
    # TypeError: function() missing 2 required positional arguments: 'a' and 'b'

    add_numbers.__call__()
    # TypeError: function() missing 2 required positional arguments: 'a' and 'b'

Injecting properties
--------------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.myattr = 10

    print(add_numbers.myattr)
    # 10

Injecting methods
-----------------
 .. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.say_hello = lambda name: print(f'My name... {name}')

    add_numbers.say_hello('José Jiménez')
    # My name... José Jiménez


Proxy methods
=============
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, *args, **kwargs):
            if 'z' in kwargs:
                z = kwargs.pop('z')
            else:
                *args, z = args

            super().__init__(*args, **kwargs)
            self.z = z

        def __str__(self):
            return f'Point3D(x={self.x}, y={self.y}, z={self.z})'


    p1 = Point3D(x=1, y=2, z=3)
    p2 = Point3D(1, 2, 3)
    p3 = Point3D(1, 2, z=3)

    print(p1)
    # Point3D(x=1, y=2, z=3)

    print(p2)
    # Point3D(x=1, y=2, z=3)

    print(p3)
    # Point3D(x=1, y=2, z=3)


Container Class
===============
* A.K.A. Placeholder class

.. code-block:: python
    :caption: Dynamically creating fields

    class Container:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


    a = Container(firstname='Jan', lastname='Twardowski')
    a.firstname          # Jan
    a.lastname           # 'Twardowski'

    b = Container(species='Setosa')
    b.species            # 'Setosa'

.. code-block:: python
    :caption: Dynamically creating fields

    class Astronaut:
        def __init__(self, lastname, **kwargs):
            self.lastname = lastname

            for key, value in kwargs.items():
                setattr(self, key, value)


    jan = Astronaut(lastname='Twardowski', addresses=())
    ivan = Astronaut(firstname='Иван', lastname='Иванович', agency='Roscosmos')

    print(jan.lastname)   # Twardowski
    print(ivan.firstname)  # Иван

    print(jan.__dict__)    # {'lastname': 'Twardowski', 'addresses': ()}
    print(ivan.__dict__)    # {'lastname': 'Иванович', 'firstname': 'Иван', 'agency': 'Roscosmos'}

.. code-block:: python

    class Container:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs


    a = Container(firstname='Jan', lastname='Twardowski')
    print(a.firstname)          # Jan
    print(a.lastname)           # 'Twardowski'

    b = Container(species='Setosa')
    print(b.species)             # 'Setosa'


Example
=======
.. code-block:: python

    DATA = [
        {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
            {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},

        {"firstname": "José", "lastname": "Jiménez", "addresses": [
            {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
            {"street": "", "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},

        {"firstname": "Mark", "lastname": "Watney", "addresses": [
            {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
            {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},

        {"firstname": "Иван", "lastname": "Иванович", "addresses": [
            {"street": "", "city": "Космодро́м Байкону́р", "postcode": "", "region": "Кызылординская область", "country": "Қазақстан"},
            {"street": "", "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},

        {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

        {"firstname": "Alex", "lastname": "Vogel", "addresses": [
            {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
    ]


    class Container:
        def __init__(self, *args, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        def __repr__(self):
            name = self.__class__.__name__
            arguments = tuple(self.__dict__.values())
            return f'\n\n{name}{arguments}'

    result = [Container(**data)
              for data in DATA]

    print(result)
    # [Container('Jan', 'Twardowski', [{'street': 'Kamienica Pod św. Janem Kapistranem', 'city': 'Kraków', 'postcode': '31-008', 'region': 'Małopolskie', 'country': 'Poland'}]),
    #  Container('José', 'Jiménez', [{'street': '2101 E NASA Pkwy', 'city': 'Houston', 'postcode': 77058, 'region': 'Texas', 'country': 'USA'}, {'street': '', 'city': 'Kennedy Space Center', 'postcode': 32899, 'region': 'Florida', 'country': 'USA'}]),
    #  Container('Mark', 'Watney', [{'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'postcode': 91109, 'region': 'California', 'country': 'USA'}, {'street': '2825 E Ave P', 'city': 'Palmdale', 'postcode': 93550, 'region': 'California', 'country': 'USA'}]),
    #  Container('Иван', 'Иванович', [{'street': '', 'city': 'Космодро́м Байкону́р', 'postcode': '', 'region': 'Кызылординская область', 'country': 'Қазақстан'}, {'street': '', 'city': 'Звёздный городо́к', 'postcode': 141160, 'region': 'Московская область', 'country': 'Россия'}]),
    #  Container('Melissa', 'Lewis', []),
    #  Container('Alex', 'Vogel', [{'street': 'Linder Hoehe', 'city': 'Köln', 'postcode': 51147, 'region': 'North Rhine-Westphalia', 'country': 'Germany'}])]


Assignments
===========
.. todo:: Create assignments
