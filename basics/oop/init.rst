.. _OOP Init Method:

***********
Init Method
***********


.. highlights::
    * It's a first method run after object is initiated
    * All classes has default ``__init__()``
    * ``__init__()`` is not a constructor!


Initializer Method Without Arguments
====================================
.. code-block:: python
    :caption: Initializer method without arguments

    class Astronaut:
        def __init__(self):
            print('My name... José Jiménez')


    jose = Astronaut()
    # My name... José Jiménez


Initializer Method With Arguments
=================================
.. code-block:: python
    :caption: Initializer method with arguments

    class Astronaut:
        def __init__(self, firstname, lastname='Unknown'):
            print(f'My name... {firstname} {lastname}')


    jan = Astronaut('Jan')
    # My name... Jan

    jose = Astronaut('José', 'Jiménez')
    # My name... José Jiménez

    mark = Astronaut(firstname='José', lastname='Jiménez')
    # My name... José Jiménez

    melissa = Astronaut('Melissa', lastname='Lewis')
    # My name... José Jiménez

    ryan = Astronaut(lastname='Stone', firstname='Ryan')
    # My name... José Jiménez

    ivan = Astronaut()
    # TypeError: __init__() missing 1 required positional argument: 'firstname'


Initializing Attributes
=======================
.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self):
            self.firstname = 'Mark'
            self.lastname = 'Watney'


    mark = Astronaut()

    print(mark.firstname)       # Mark
    print(mark.lastname)        # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self):
            self.firstname = 'Mark'
            self.lastname = 'Watney'


    mark = Astronaut()
    print(mark.firstname)       # Mark
    print(mark.lastname)        # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut()
    print(ivan.firstname)       # Mark
    print(ivan.lastname)        # Watney
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self, a, b):
            self.firstname = a
            self.lastname = b


    mark = Astronaut('Mark', 'Watney')
    print(mark.firstname)       # Mark
    print(mark.lastname)        # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut(a='Ivan', b='Ivanovich')
    print(ivan.firstname)       # Ivan
    print(ivan.lastname)        # Ivanovich
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    mark = Astronaut('Mark', 'Watney')
    print(mark.firstname)       # Mark
    print(mark.lastname)        # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut(firstname='Ivan', lastname='Ivanovich')
    print(ivan.firstname)       # Ivan
    print(ivan.lastname)        # Ivanovich
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.name = f'{firstname} {lastname}'


    mark = Astronaut('Mark', 'Watney')

    print(mark.name)           # Mark Watney
    print(mark.firstname)      # AttributeError: 'Astronaut' object has no attribute 'firstname'
    print(mark.lastname)       # AttributeError: 'Astronaut' object has no attribute 'lastname'

.. code-block:: python
    :caption: Init time attributes

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z


    p1 = Point(10, 20)
    p2 = Point(x=10, y=20)
    p3 = Point(10, 20, 30)
    p4 = Point(10, 20, z=30)
    p5 = Point(x=10, y=20, z=30)

.. code-block:: python
    :caption: Init time attributes

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')

    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa


    virginica = Iris(
        sepal_length=5.8,
        sepal_width=2.7,
        petal_length=5.1,
        petal_width=1.9,
        species='virginica')

    print(virginica.__dict__)
    # {'sepal_length': 5.8,
    #  'sepal_width': 2.7,
    #  'petal_length': 5.1,
    #  'petal_width': 1.9,
    #  'species': 'virginica'}

.. code-block:: python
    :caption: Since Python 3.7 there is a ``@dataclass`` decorator, which automatically generates ``__init__()`` arguments and fields. More information in :ref:`OOP Dataclass`.

    from dataclasses import dataclass


    @dataclass
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str = 'Iris'


    setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')

    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa


    virginica = Iris(
        sepal_length=5.8,
        sepal_width=2.7,
        petal_length=5.1,
        petal_width=1.9,
        species='virginica')

    print(virginica.__dict__)
    # {'sepal_length': 5.8,
    #  'sepal_width': 2.7,
    #  'petal_length': 5.1,
    #  'petal_width': 1.9,
    #  'species': 'virginica'}


Checking Values
===============
.. code-block:: python

    class Kelvin:
        MINIMAL_VALUE = 0.0

        def __init__(self, value):
            if type(value) not in (float, int):
                raise TypeError('Temperature must be int or float')
            if value < self.MINIMAL_VALUE:
                raise ValueError('Temperature must be greater than 0')
            self.value = value


    a = Kelvin(273.15)
    print(a.value)
    # 273.15

    b = Kelvin(-300)
    # ValueError: Temperature must be greater than 0


Assignments
===========

OOP Init Print
--------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/oop_init_print.py`

:English:
    #. Create one class ``Temperature``
    #. Create three instances of ``Temperature`` class
    #. Values must be passed at the initialization
    #. At initialization instances print:

        * Instance ``celsius`` prints temperature 36.6
        * Instance ``fahrenheit`` prints temperature 97.88
        * Instance ``kelvin`` prints temperature 309.75

    #. Do not convert units (print only given numbers)
    #. Do not store values in the instances (only print on instance creation)
    #. Do not use ``@dataclass``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz jedną klasę ``Temperature``
    #. Stwórz trzy instancje klasy ``Temperature``
    #. Wartości mają być podawane przy inicjalizacji
    #. Przy inicjalizacji instancje wypisują:

        * Instancja ``celsius`` wyświetla temperaturę 36.6
        * Instancja ``fahrenheit`` wyświetla temperaturę 97.88
        * Instancja ``kelvin`` wyświetla temperaturę 309.75

    #. Nie konwertuj jednostek (użyj tylko podanych numerów)
    #. Nie przechowuj informacji w instancjach (tylko wypisz przy inicjalizacji)
    #. Nie używaj ``@dataclass``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        36.6
        97.88
        309.75

OOP Init Model
--------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/oop_init_model.py`

:English:
    #. Use data from "Input" section (see below)
    #. Model the data using classes
    #. Create instances for each record
    #. Values must be passed at the initialization
    #. Create instances of a first class using positional arguments
    #. Create instances of a second class using keyword arguments
    #. Using ``__dict__`` print all fields from each instance
    #. Do not use ``@dataclass``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zamodeluj dane za pomocą klas
    #. Stwórz instancje dla każdego wpisu
    #. Wartości mają być podawane przy inicjalizacji
    #. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    #. Twórz instancje drugiej klasy używając argumentów nazwanych
    #. Za pomocą ``__dict__`` wypisz wszystkie pola każdej z instancji
    #. Nie używaj ``@dataclass``

:Input:
    .. code-block:: text

        Jan Twardowski, Poland, 1961-04-12
        Mark Watney, USA, 1969-07-21
        European Space Agency, Europe, 1975-05-30
        National Aeronautics and Space Administration, USA, 1958-07-29
        Polish Space Agency, Poland, 2014-09-26

:The whys and wherefores:
    * :ref:`OOP Classes and Instances`
    * :ref:`OOP Attributes`
