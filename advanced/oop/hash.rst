.. _OOP Hash:

****
Hash
****


Rationale
=========
* Used for quickly compare two objects
* All objects compare unequal (except with themselves)
* ``set()`` elements has to be hashable
* ``dict()`` keys has to be hashable
* Used to quickly compare dictionary keys during a dictionary lookup

.. code-block:: python

    class MyClass:
        def __hash__(self, *args, **kwargs):
            return 1234

        def __eq__(self, other):
            return hash(self) == hash(other)


Hash Method
===========
* ``hash(obj) ->  int``
* ``hash()`` returns the hash value of the object (if it has one)
* ``__hash__`` should return the same value for objects that are equal
* User-defined classes have ``__eq__()`` and ``__hash__()`` methods by default
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
            return hash(self) == hash(other)


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
    :caption: ``set()`` elements must be hashable

    {1, 1, 2}
    # {1, 2}

    {1, 1.1, 'a'}
    # {1, 1.1, 'a'}

    {'a', (1, 2)}
    # {'a', (1, 2)}


Set Definition
==============
.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Mark Watney')
    data = {astro, astro}
    print(data)
    # {<__main__.Astronaut object at 0x105be25b0>}

    data = {Astronaut('Mark Watney'), Astronaut('Mark Watney')}
    print(data)
    # {<__main__.Astronaut object at 0x105be20a0>,
    #  <__main__.Astronaut object at 0x105be2040>}

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, other):
            return hash(self) == hash(other)


    astro = Astronaut('Mark Watney')
    data = {astro, astro}
    print(data)
    # {<__main__.Astronaut object at 0x105bc77c0>}

    data = {Astronaut('Mark Watney'), Astronaut('Mark Watney')}
    print(data)
    # {<__main__.Astronaut object at 0x105bc7700>}


Use Cases
=========
.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    data = set()
    astro = Astronaut('Mark Watney')

    data.add(astro)
    print(data)
    # {<__main__.Astronaut object at 0x105bde070>}

    data.add(astro)
    print(data)
    # {<__main__.Astronaut object at 0x105bde070>}

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    data = set()

    data.add(Astronaut('Mark Watney'))
    print(data)
    # {<__main__.Astronaut object at 0x105bc7d00>}

    data.add(Astronaut('Mark Watney'))
    print(data)
    # {<__main__.Astronaut object at 0x105bc7d00>,
    #  <__main__.Astronaut object at 0x105bc7e20>}

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, other):
            return hash(self) == hash(other)


    data = set()

    data.add(Astronaut('Mark Watney'))
    print(data)
    # {<__main__.Astronaut object at 0x105bde9d0>}

    data.add(Astronaut('Mark Watney'))
    print(data)
    # {<__main__.Astronaut object at 0x105bde9d0>}


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


Assignments
===========
.. todo:: Create assignments
