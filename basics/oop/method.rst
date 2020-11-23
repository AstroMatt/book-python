.. _OOP Methods:

*******
Methods
*******


Rationale
=========
.. highlights::
    * Methods are functions in the class
    * First argument is always instance (``self``)
    * While calling function you never pass ``self``
    * Prevents copy-paste code
    * Improves readability
    * Improves refactoring
    * Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)

.. code-block:: python
    :caption: Syntax

    class MyClass:
        def mymethod(self):
            ...

    my = MyClass()
    my.mymethod()


Methods Without Arguments
=========================
.. code-block:: python
    :caption: Methods without arguments

    class Astronaut:
        def say_hello(self):
            print('My name... José Jiménez')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez


Methods With Required Argument
==============================
.. code-block:: python
    :caption: Methods with required argument

    class Astronaut:
        def say_hello(self, name):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # Traceback (most recent call last):
    #     ...
    # TypeError: say_hello() missing 1 required positional argument: 'name'


Methods With Optional Argument
==============================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Astronaut:
        def say_hello(self, name='Unknown'):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # My name... Unknown


Assignments
===========

OOP Method Call
---------------
* Assignment: OOP Method Call
* Filename: oop_method_call.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 13 min

English:
    #. Use data from "Given" section (see below)
    #. Define class ``Stats``
    #. Define method ``mean()`` in ``Stats`` class
    #. Method takes ``data: list[float]`` as an argument
    #. Method returns arithmetic mean of the ``data``
    #. Returned value must me rounded to one decimal places
    #. Create instance of ``Stats`` class
    #. Iterate over ``DATA`` skipping header
    #. Separate features from label
    #. Call ``mean()`` method of ``Stats`` class passing list of features as an argument
    #. Define ``result: list[float]`` with list of means from each row
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zdefiniuj klasę ``Stats``
    #. Zdefiniuj metodę ``mean()`` w klasie ``Stats``
    #. Metoda przyjmuje ``data: list[float]`` jako argument
    #. Metoda zwraca średnią arytmetyczną z ``data``
    #. Zwracana value ma być zaokrąglona do jednego miejsca po przecinku
    #. Stwórz instancję klasy ``Stats``
    #. Iteruj po ``DATA`` pomijając nagłówek
    #. Rozdziel cechy od etykiety
    #. Wywołuj metodę ``mean()`` klasy ``Stats`` przekazując listę features jako argument
    #. Zdefiniuj ``result: list[float]`` z listą średnich każdego z wierszy
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * ``round()``

Given:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
        ]

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is float for x in result)
    >>> result
    [3.9, 2.5, 3.5, 4.1, 3.9, 2.4]

