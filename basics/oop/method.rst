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

OOP Method Sequence
-------------------
* Assignment name: OOP Method Sequence
* Complexity level: easy
* Lines of code to write: 18 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_method_iris.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Define class ``Iris``
    #. Define method ``mean()`` in ``Iris`` class
    #. Method takes sequence as an argument
    #. Method must return arithmetic mean of the sequence
    #. Iterate over ``DATA`` omitting header
    #. Separate ``features`` from ``label``
    #. Call ``mean()`` method of ``Iris`` class passing ``features`` as an argument
    #. Sum all mean results
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefinuj klasę ``Iris``
    #. Zdefinuj metodę ``mean()`` w klasie ``Iris``
    #. Metoda przyjmuje sekwencję jako argument
    #. Metoda ma zwracać średnią arytmetyczną z sekwencji
    #. Iteruj po ``DATA`` pomijając nagłówek
    #. Rozdziel ``features`` od ``label``
    #. Wywołuj metodę ``mean()`` klasy ``Iris`` przekazując ``features`` jako argument
    #. Zsumuj wyniki wszystkich średnich
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

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

:Output:
    .. code-block:: python

        result: float
        # 73.39999999999999
