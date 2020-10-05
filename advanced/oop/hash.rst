.. _OOP Hash:

****
Hash
****


Rationale
=========
.. highlights::
    * Return the hash value of the object (if it has one)
    * ``hash(obj) ->  int``
    * They are used to quickly compare dictionary keys during a dictionary lookup
    * ``set()`` elements has to be hashable
    * ``dict()`` keys has to be hashable
    * User-defined classes have ``__eq__()`` and ``__hash__()`` methods by default
    * All objects compare unequal (except with themselves)
    * ``x.__hash__()`` returns an appropriate value such that ``x == y`` implies both that ``x is y`` and ``hash(x) == hash(y)``


Examples
========
.. code-block:: python
    :caption: ``dict()`` keys has to be hashable

    data = {}

    data[1] = 'whatever'
    data[1.1] = 'whatever'
    data['a'] = 'whatever'
    data[True] = 'whatever'
    data[False] = 'whatever'
    data[None] = 'whatever'

    data[(1,2)] = 'whatever'

    data[[1,2]] = 'whatever'
    # Traceback (most recent call last):
    #   ...
    # TypeError: unhashable type: 'list'

    data[{1,2}] = 'whatever'
    # Traceback (most recent call last):
    #   ...
    # TypeError: unhashable type: 'set'

    data[frozenset({1,2})] = 'whatever'

    data[{'a':1}] = 'cokolwiek'
    # Traceback (most recent call last):
    #   ...
    # TypeError: unhashable type: 'dict'

.. code-block:: python
    :caption: ``set()`` elements has to be hashable

    {1, 1, 2}
    # {1, 2}

    {1, 1.1, 'a'}
    # {1, 1.1, 'a'}

    {'a', (1, 2)}
    # {'a', (1, 2)}


Use Cases
=========
.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    data = set()

    data.add(Astronaut('Mark Watney'))
    data
    # {<__main__.Astronaut object at 0x10a66d850>}

    data.add(Astronaut('Mark Watney'))
    data
    # {<__main__.Astronaut object at 0x10a66df10>,
    #  <__main__.Astronaut object at 0x10a66d850>}

    len(data)
    # 2

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    data = set()
    astro = Astronaut('Mark Watney')

    data.add(astro)
    data
    # {<__main__.Astronaut object at 0x10a6627c0>}

    data.add(astro)
    data
    # {<__main__.Astronaut object at 0x10a6627c0>}

    len(data)
    # 1

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Mark Watney')
    data = {astro, astro}
    len(data)
    # 1

    data = {Astronaut('Mark Watney'), Astronaut('Mark Watney')}
    len(data)
    # 2


Hashable
========
.. code-block:: python

    key = list([1, 2, 3])
    hash(key)
    # Traceback (most recent call last):
    #   ...
    # TypeError: unhashable type: 'list'

.. code-block:: python

    class list(list):
        def __hash__(self):
            return 0

    key = list([1, 2, 3])
    hash(key)
    0

.. code-block:: python

    data = {}

    key = list([1,2,3])
    data[key] = 'whatever'
    # Traceback (most recent call last):
    #   ...
    # TypeError: unhashable type: 'list'

    class list(list):
        def __hash__(self):
            return 0

    data[key] = 'whatever'
    data
    # {[1, 2, 3]: 'whatever'}


Hash Method
===========
* ``__hash__`` should return the same value for objects that are equal
* It also shouldn't change over the lifetime of the object
* Generally you only implement it for immutable objects

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __hash__(self, *args, **kwargs):
            firstname = hash(self.firstname)
            lastname = hash(self.lastname)
            return hash(firstname + lastname)

        def __eq__(self, other):
            return (self.firstname == other.firstname) \
                    and (self.lastname == other.lastname)


Assignments
===========
.. todo:: Create assignments
