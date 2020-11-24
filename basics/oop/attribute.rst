.. _OOP Attributes:

**********
Attributes
**********


Rationale
=========
.. highlights::
    * Attributes are also known as "Properties" or "Fields"
    * ``snake_case`` name convention
    * Attributes store information (state) for instances
    * Access field values using dot (``.``) notation
    * Attributes should be defined only in ``__init__()`` method
    * More information in :ref:`OOP Init Method`

.. glossary::

    attribute
    field
        Variable inside the class.
        Can be used as a synonym of :term:`property` or :term:`state`.

    property
        Variable inside the class.
        Should not change during lifetime of an object.

    state
        Variable inside the class.
        Changes during lifetime of an object.
        Represents current state of an object.

    namespace
        Container for storing related data

.. code-block:: text
    :caption: Class example with distinction of properties and state attributes

    Bucket with Water

        Properties:
            - color
            - width
            - height
            - radius
            - capacity
            - net mass (without water)

        State:
            - volume  (how much water is currently in bucket)
            - gross mass = net mass + water mass (water mass depends on its volume used))

.. figure:: img/bucket.jpg
    :width: 30%
    :align: center


Syntax
======
.. code-block:: python

    class Astronaut:
        pass


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.firstname)
    print(astro.lastname)


Dynamic Attributes
==================
.. code-block:: python
    :caption: Dynamic attributes

    class Astronaut:
        pass


    jose = Astronaut()
    jose.firstname = 'José'
    jose.lastname = 'Jiménez'

    print(f'My name... {jose.firstname} {jose.lastname}')
    # My name... José Jiménez

.. code-block:: python
    :caption: Accessing not existing attributes

    class Astronaut:
        pass


    astro = Astronaut()

    print(astro.missions)
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Astronaut' object has no attribute 'missions'

.. code-block:: python

    class Astronaut:
        pass


    jose = Astronaut()
    mark = Astronaut()

    jose.name = 'José Jiménez'

    print(f'My name... {jose.name}')
    # My name... José Jiménez

    print(f'My name... {mark.name}')
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'Astronaut' object has no attribute 'name'

Namespace
=========
.. code-block:: python

    point_x = 1
    point_y = 2
    point_z = 3

    print(point_x)
    print(point_y)
    print(point_z)

.. code-block:: python

    class Point:
        pass

    point = Point()
    point.x = 1
    point.y = 2
    point.z = 3

    print(point.x)
    print(point.y)
    print(point.z)

Different Types
===============
.. code-block:: python
    :caption: Dynamic attributes

    class Iris:
        pass


    setosa = Iris()
    setosa.features = [5.1, 3.5, 1.4, 0.2]
    setosa.label = 'setosa'

    print(setosa.label)
    # setosa

    print(setosa.features)
    # [5.1, 3.5, 1.4, 0.2]

    sum(setosa.features)
    # 10.2

.. code-block:: python

    class Astronaut:
        pass


    jose = Astronaut()
    jose.age = 36

    mark = Astronaut()
    mark.age = 42.1


Get All Dynamic Attributes and Values
=====================================
* ``obj.__dict__``

.. code-block:: python
    :caption: ``__dict__`` - Getting dynamic fields and values

    class Iris:
        pass


    flower = Iris()
    flower.sepal_length = 5.1
    flower.sepal_width = 3.5
    flower.petal_length = 1.4
    flower.petal_width = 0.2
    flower.species = 'setosa'

    print(flower.__dict__)
    # {'sepal_length': 5.1,
    #  'sepal_width': 3.5,
    #  'petal_length': 1.4,
    #  'petal_width': 0.2,
    #  'species': 'setosa'}


Assignments
===========

OOP Attribute Model
-------------------
* Assignment: OOP Attribute Model
* Filename: oop_attribute_model.py
* Complexity: easy
* Lines of code to write: 15 lines
* Estimated time: 8 min

English:
    #. Use data from "Given" section (see below)
    #. Model the data using classes
    #. How many classes are there?
    #. How many instances are there?
    #. Create instances filling it with data
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zamodeluj dane za pomocą klas
    #. Ile jest klas?
    #. Ile jest instancji?
    #. Stwórz instancje wypełniając je danymi
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: text

        Mark Watney, USA, 1969-07-21
        National Aeronautics and Space Administration, USA, 1958-07-29

Tests:
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Mark Watney' in watney.__dict__.values()
    >>> assert 'USA' in watney.__dict__.values()
    >>> assert '1969-07-21' in watney.__dict__.values()
    >>> assert 'National Aeronautics and Space Administration' in nasa.__dict__.values()
    >>> assert 'USA' in nasa.__dict__.values()
    >>> assert '1958-07-29' in nasa.__dict__.values()

