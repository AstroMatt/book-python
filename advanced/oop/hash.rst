****
Hash
****


Rationale
=========
.. highlights::
    * Return the hash value of the object (if it has one)
    * ``hash() ->  int``
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

    key = 'my_key'

    my_dict = {
        'a': 'key can be str',
        2: 'key can be int',
        3.3: 'key can be float',
        ('a', 2, 3.3): 'key can be tuple',
        key: 'key can be str',
    }

.. code-block:: python
    :caption: ``set()`` elements has to be hashable

    {1, 1, 2}
    # {1, 2}

    {1, 1.1, 'a'}
    # {1, 1.1, 'a'}

    {'a', (1, 2)}
    # {'a', (1, 2)}


Dict Keys
=========
.. code-block:: python

    data = tuple((1, 2, 3))

    result = {}
    result[data] = 'Mark Watney'
    # {(1, 2, 3): 'Mark Watney'}

.. code-block:: python

    data = list([1, 2, 3])

    result = {}
    result[data] = 'Mark Watney'
    # TypeError: unhashable type: 'list'

.. code-block:: python

    class list(list):
        def __hash__(self):
            return 1


    data = list([1, 2, 3])

    result = {}
    result[data] = 'Mark Watney'

    print(result)
    # {[1, 2, 3]: 'Mark Watney'}

.. code-block:: python
    :caption: ``set()`` elements has to be hashable

    class Astronaut:
        def __init__(self, name):
            self.name = name


    jan = Astronaut('Jan Twardowski')
    data = {jan, jan}
    len(data)
    # 1

    data = {Astronaut('Jan Twardowski'), Astronaut('Jan Twardowski')}
    len(data)
    # 2

Hash Method
===========
.. code-block:: python
    :caption: Generating hash and object comparision

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __hash__(self, *args, **kwargs):
            """
            __hash__ should return the same value for objects that are equal.
            It also shouldn't change over the lifetime of the object;
            generally you only implement it for immutable objects.
            """
            return hash(self.firstname) + hash(self.lastname)

        def __eq__(self, other):
            if self.firstname == other.firstname and \
                    self.lastname == other.lastname:
                return True
            else:
                return False

.. code-block:: python
    :caption: Generating hash and object comparision. Since Python 3.7 ``dict`` has fixed order

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __hash__(self):
            return hash(self.__dict__)

        def __eq__(self, other):
            if self.__dict__ == other.__dict__:
                return True
            else:
                return False


Assignments
===========
.. todo:: Create assignments
