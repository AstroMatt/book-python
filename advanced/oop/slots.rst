
*****
Slots
*****


.. highlights::
    * faster attribute access
    * space savings in memory

Instead of having a dynamic dict that allows adding attributes to objects at anytime, there is a static structure which does not allow additions after creation. This saves the overhead of one dict for every object that uses slots

Unfortunately there is a side effect to slots. They change the behavior of the objects that have slots in a way that can be abused by control freaks and static typing weenies. This is bad, because the control freaks should be abusing the metaclasses and the static typing weenies should be abusing decorators, since in Python, there should be only one obvious way of doing something.

The space savings is from:

    * Storing value references in slots instead of ``__dict__``.
    * Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``.

Using
=====
.. code-block:: python

    class Astronaut:
        __slots__ = ()


    astro = Astronaut()

    astro.name = 'Mark Watney'
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname',)


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Astronaut' object has no attribute 'lastname'


``__slots__`` and ``__dict__``
==============================
.. code-block:: python
    :caption: Using ``__slots__`` will prevent from creating ``__dict__``

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.__slots__)
    # ('firstname', 'lastname')

    print(astro.__dict__)
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

.. code-block:: python

    class Astronaut:
        __slots__ = ('__dict__', 'firstname')


    astro = Astronaut()

    astro.firstname = 'Mark'   # will use __slots__
    astro.lastname = 'Watney'  # not in __slots__, will use __dict__

    print(astro.__slots__)
    # ('__dict__', 'firstname')

    print(astro.__dict__)
    # {'lastname': 'Watney'}


Inheritance
===========
* Slots are inherited too

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')

    class NASAAstronaut(Iris):
        __slots__ = ('mission',)

    class ESAAstronaut(Iris):
        # redundant 'firstname' and 'mission'
        __slots__ = ('firstname', 'firstname', 'mission')


Examples
========
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

    result = {attr: getattr(astro, attr)
              for attr in astro.__slots__}

    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}

.. code-block:: python

    class IrisDict:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'Iris(...)'


    class IrisSlots:
        __slots__ = ('sepal_length', 'sepal_width', 'petal_length',
                     'petal_width', 'species')

        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'Iris(...)'


    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ]

    result_dict = [IrisDict(*row) for row in DATA[1:]]
    result_slots = [IrisSlots(*row) for row in DATA[1:]]

    result_slots[0].__dict__
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Iris' object has no attribute '__dict__'

    result_slots[0].__slots__
    # ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    [getattr(i,x) for x in result_slots[0].__slots__]
    # [5.8, 2.7, 5.1, 1.9, 'virginica']

    {x: getattr(i,x) for x in result_slots[0].__slots__}
    # {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'}



Assignments
===========
.. todo:: Create assignments
