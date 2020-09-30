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
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname',)


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'
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
.. code-block:: python

    class Iris:
        __slots__ = ('species', 'kingdom')

    class Setosa(Iris):
        __slots__ = ('name',)

    class Virginica(Iris):
        __slots__ = ('species', 'kingdom', 'name')  # redundant species and kingdom


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
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

    resultDict = [IrisDict(*row) for row in DATA[1:]]
    resultSlots = [IrisSlots(*row) for row in DATA[1:]]

    print(result)

    i = result[0]

    i.__dict__
    # AttributeError: 'Iris' object has no attribute '__dict__'

    i.__slots__
    # ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    [getattr(i,x) for x in i.__slots__]
    # [5.8, 2.7, 5.1, 1.9, 'virginica']

    {x: getattr(i,x) for x in i.__slots__}
    # {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'}



Assignments
===========
.. todo:: Create assignments
