***********
Collections
***********

* https://docs.python.org/3/library/collections.html

It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

    ================  ====================================================================
    Name              Description
    ----------------  --------------------------------------------------------------------
    ``namedtuple``    factory function for creating tuple subclasses with named fields
    ``deque``         list-like container with fast appends and pops on either end
    ``ChainMap``      dict-like class for creating a single view of multiple mappings
    ``Counter``       dict subclass for counting hashable objects
    ``OrderedDict``   dict subclass that remembers the order entries were added
    ``defaultdict``   dict subclass that calls a factory function to supply missing values
    ``UserDict``      wrapper around dictionary objects for easier dict subclassing
    ``UserList``      wrapper around list objects for easier list subclassing
    ``UserString``    wrapper around string objects for easier string subclassing
    ================  ====================================================================


``OrderedDict``
===============
.. code-block:: python

    jose = {'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}

    print(jose)
    # {'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}

    print(jose['firstname'], jose['lastname'], jose['agency'])
    # José Jiménez NASA

.. code-block:: python

    from collections import OrderedDict

    jose = OrderedDict(firstname='José', lastname='Jiménez', agency='NASA')
    print(jose)
    # OrderedDict([
    #   ('firstname', 'José'),
    #   ('lastname', 'Jiménez'),
    #   ('agency', 'NASA')])

    dict(jose)
    {'firstname': 'José', 'lastname': 'Jiménez', 'agency': 'NASA'}

``namedtuple``
==============
.. code-block:: python

    from collections import namedtuple


    Point = namedtuple('Point', ('x', 'y'))

    p1 = Point(x=50, y=120)
    p2 = Point(50, 120)

    print(p1)
    # Point(x=50, y=120)

    print(p1.x)
    # 50

    print(p1.y)
    # 120

    print(p2)
    # Point(x=50, y=120)

.. code-block:: python

    from collections import namedtuple

    Astronaut = namedtuple('Astronaut', ['firstname', 'lastname', 'agency'])
    jose = Astronaut(firstname='José', lastname='Jiménez', agency='NASA')

    print(jose)
    # Astronaut(firstname='José', lastname='Jiménez', agency='NASA')

    print(jose.firstname, jose.lastname, jose.agency)
    # José Jiménez NASA


Counter
=======
.. code-block:: python

    import random


    random_numbers = [random.randint(0, 10) for a in range(0, 50)]
    counter = dict()

    for number in random_numbers:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    counter.items()
    # [(7, 12), (4, 8), (9, 6), (1, 5), (2, 4)]

.. code-block:: python

    import random
    from collections import Counter


    random_numbers = [random.randint(0, 10) for a in range(0, 50)]
    counter = Counter(random_numbers)

    counter.most_common(5)
    # [(7, 12), (4, 8), (9, 6), (1, 5), (2, 4)]

UserString
==========
.. code-block:: python

    from collections import UserString


    class str(UserString):
        def __add__(self, other):
            return f'{self} {other}'


    result = str('José') + 42
    print(result)
    # José 42

.. code-block:: python

    from collections import UserString


    class str(UserString):
        def __add__(self, other):
            return f'{self} {other}'


    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f'({self.x}, {self.y})'


    p = Point(x=10, y=20)

    out = str('José') + p
    print(out)
    # José (10, 20)\


Assignments
===========
.. todo:: Create assignments
