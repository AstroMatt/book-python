.. _OOP Stringify Objects:

*****************
Stringify Objects
*****************


Rationale
=========
.. code-block:: python

    import datetime
    date = datetime.datetime(1961, 4, 12, 6, 7)

    str(date)
    # '1961-04-12 06:07:00'

    repr(date)
    # 'datetime.datetime(1961, 4, 12, 6, 7)'

    format(date, '%Y-%m-%d')
    # '1961-04-12'


String
======
.. highlights::
    * Calling function ``str(obj)`` calls ``obj.__str__()``
    * Calling function ``print(obj)`` calls ``str(obj)``, which calls ``obj.__str__()``
    * Method ``obj.__str__()`` must return ``str``
    * for end-user

.. code-block:: python

    class Astronaut:
        pass

    astro = Astronaut()
    str(astro)
    # '<__main__.Astronaut object at 0x10ba3d760>'

.. code-block:: python
    :caption: Object without ``__str__()`` method overloaded prints their memory address

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('José Jiménez')

    print(astro)        # <__main__.Astronaut object at 0x114175dd0>
    str(astro)          # '<__main__.Astronaut object at 0x114175dd0>'
    astro.__str__()     # '<__main__.Astronaut object at 0x114175dd0>'

.. code-block:: python
    :caption: Objects can verbose print if ``__str__()`` method is present

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'My name... {self.name}'


    astro = Astronaut('José Jiménez')

    print(astro)        # My name... José Jiménez
    str(astro)          # 'My name... José Jiménez'
    astro.__str__()     # 'My name... José Jiménez'


Representation
==============
.. highlights::
    * Calling function ``repr(obj)`` calls ``obj.__repr__()``
    * Method ``obj.__repr__()`` must return ``str``
    * for developers
    * object representation
    * copy-paste for creating object with the same values
    * useful for debugging
    * printing ``list`` will call ``__repr__()`` method on each element

.. code-block:: python

    class Astronaut:
        pass

    astro = Astronaut()
    repr(astro)
    # '<__main__.Astronaut object at 0x10ba3d760>'


.. code-block:: python
    :caption: Using ``__repr__()`` on a class

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'Astronaut(name="{self.name}")'


     astro = Astronaut('José Jiménez')

     repr(astro)        # 'Astronaut(name="José Jiménez")'
     astro              # Astronaut(name="José Jiménez")

.. code-block:: python
    :caption: Printing ``list`` will call ``__repr__()`` method on each element

    class Astronaut:
        def __init__(self, name):
            self.name = name

    crew = [
        Astronaut('Jan Twardowski'),
        Astronaut('Mark Watney'),
        Astronaut('Melissa Lewis'),
    ]

    print(crew)
    # [
    #   <__main__.Astronaut object at 0x107871160>,
    #   <__main__.Astronaut object at 0x107c422e8>,
    #   <__main__.Astronaut object at 0x108156be0>
    # ]

.. code-block:: python
    :caption: Printing ``list`` will call ``__repr__()`` method on each element

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'{self.name}'

    crew = [
        Astronaut('Jan Twardowski'),
        Astronaut('Mark Watney'),
        Astronaut('Melissa Lewis'),
    ]

    print(crew)
    # [Jan Twardowski, Mark Watney, Melissa Lewis]


Format
======
.. highlights::
    * Calling function ``format(obj, fmt)`` calls ``obj.__format__(fmt)``
    * Method ``obj.__format__()`` must return ``str``
    * Used for advanced formatting

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __format__(self, mood):
            if mood == 'happy':
                return f"Yuppi, we're going to space!"
            elif mood == 'scared':
                return f"I hope we don't crash"


     jose = Astronaut('José Jiménez')

     print(f'{jose:happy}')
     # Yuppi, we're going to space!

     print(f'{jose:scared}')
     # I hope we don't crash

.. code-block:: python

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR


    class Duration:
        def __init__(self, seconds):
            self.seconds = seconds

        def __format__(self, unit):
            if unit == 'minutes':
                result = self.seconds / MINUTE
            elif unit == 'hours':
                result = self.seconds / HOUR
            elif unit == 'days':
                result = self.seconds / DAY
            return str(round(result, 2))

    duration = Duration(seconds=3600)

    print(f'Duration was {duration:minutes} min')       # Duration was 60.0 min
    print(f'Duration was {duration:hours} hour')        # Duration was 1.0 hour
    print(f'Duration was {duration:days} day')          # Duration was 0.04 day

.. code-block:: python

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR


    class Duration:
        def __init__(self, seconds):
            self.seconds = seconds

        def __format__(self, unit):
            if unit in ('s', 'sec', 'seconds'):
                result = self.seconds / SECOND
            elif unit in ('m', 'min', 'minutes'):
                result = self.seconds / MINUTE
            elif unit in ('h', 'hr', 'hours'):
                result = self.seconds / HOUR
            elif unit in ('d', 'days'):
                result = self.seconds / DAY
            return str(round(result, 2))


    duration = Duration(seconds=3600)

    print(f'Duration: {duration:s} seconds')
    print(f'Duration: {duration:m} minutes')
    print(f'Duration: {duration:h} hours')
    print(f'Duration: {duration:d} days')

.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def to_fahrenheit(self):
            return (self.kelvin-273.15) * 1.8 + 32

        def to_celsius(self):
            return self.kelvin - 273.15

        def __format__(self, unit):
            if unit == 'kelvin':
                value = self.kelvin
            elif unit == 'celsius':
                value = self.to_celsius()
            elif unit == 'fahrenheit':
                value = self.to_fahrenheit()
            return f'{value:.2f}'


    temp = Temperature(309.75)

    print(f'Temperature is {temp:kelvin} K')       # Temperature is 309.75 K
    print(f'Temperature is {temp:celsius} C')      # Temperature is 36.6 C
    print(f'Temperature is {temp:fahrenheit} F')   # Temperature is 97.88 F

.. code-block:: python

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __format__(self, name):

            if name == 'in_2D':
                result = f"Point(x={self.x}, y={self.y})"
            elif name == 'in_3D':
                result = f"Point(x={self.x}, y={self.y}, z={self.z})"
            elif name == 'as_dict':
                result = self.__dict__
            elif name == 'as_tuple':
                result = tuple(self.__dict__.values())
            elif name == 'as_json':
                import json
                result = json.dumps(self.__dict__)
            return str(result)


    point = Point(x=1, y=2)

    print(f'{point:in_2D}')           # 'Point(x=1, y=2)'
    print(f'{point:in_3D}')           # 'Point(x=1, y=2, z=0)'
    print(f'{point:as_tuple}')        # '(1, 2, 0)'
    print(f'{point:as_dict}')         # "{'x': 1, 'y': 2, 'z': 0}"
    print(f'{point:as_json}')         # '{"x": 1, "y": 2, "z": 0}'


Assignments
===========

OOP Stringify Str
-----------------
* Assignment: OOP Stringify Str
* Filename: oop_stringify_str.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 5 min

English:
    #. Use code from "Given" section (see below)
    #. While printing object show: species name and a sum of ``self.features``
    #. Result of sum round to one decimal place
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj kodu z sekcji "Given" (patrz poniżej)
    #. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę ``self.features``
    #. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
        ]

        class Iris:
            def __init__(self, features, label):
                self.features = features
                self.label = label

Tests:
    >>> for *features, label in DATA:
    ...    iris = Iris(features, label)
    ...    print(iris)
    setosa 9.4
    versicolor 16.3
    virginica 19.3

OOP Stringify Repr
------------------
* Assignment: OOP Stringify Repr
* Filename: oop_stringify_repr.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 5 min

English:
    #. Use code from "Given" section (see below)
    #. Print representation of each instance with values (use ``repr()``)
    #. Result of sum round to two decimal places
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj kodu z sekcji "Given" (patrz poniżej)
    #. Wypisz reprezentację każdej z instancji z wartościami (użyj ``repr()``)
    #. Wynik sumowania zaokrąglij do dwóch miejsc po przecinku
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
        ]


        class Iris:
            def __init__(self, features, label):
                self.features = features
                self.label = label

Tests:
    >>> result = [Iris(X,y) for *X,y in DATA]
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa'),
     Iris(features=[7.0, 3.2, 4.7, 1.4], label='versicolor'),
     Iris(features=[7.6, 3.0, 6.6, 2.1], label='virginica')]

OOP Stringify Format
--------------------
* Assignment: OOP Stringify Format
* Filename: oop_stringify_format.py
* Complexity: easy
* Lines of code to write: 8 lines
* Estimated time: 5 min

English:
    #. Use code from "Given" section (see below)
    #. Overload ``__format__()`` to convert length units
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj kodu z sekcji "Given" (patrz poniżej)
    #. Przeciąż ``__format__()`` aby konwertował jednostki długości
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 km = 1000 m
    * 1 m = 100 cm

Given:
    .. code-block:: python

        class Distance:
            def __init__(self, meters):
                self.meters = meters

Tests:
    >>> result = Distance(meters=1337)
    >>> format(result, 'km')
    '1.337'
    >>> format(result, 'cm')
    '133700'
    >>> format(result, 'm')
    '1337'

OOP Stringify Nested
--------------------
* Assignment: OOP Stringify Nested
* Filename: oop_stringify_nested.py
* Complexity: medium
* Lines of code to write: 9 lines
* Estimated time: 21 min

English:
    #. Use code from "Given" section (see below)
    #. Overload ``str`` and ``repr`` to achieve desired printing output
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj kodu z sekcji "Given" (patrz poniżej)
    #. Przeciąż ``str`` i ``repr`` aby osiągnąć oczekiwany rezultat wypisywania
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Define ``Crew.__str__()``
    * Define ``Astronaut.__str__()`` and ``Astronaut.__repr__()``
    * Define ``Mission.__repr__()``

Given:
    .. code-block:: python
        :caption: Address Book

        class Crew:
            def __init__(self, members=()):
                self.members = list(members)

        class Astronaut:
            def __init__(self, name, experience=()):
                self.name = name
                self.experience = list(experience)

        class Mission:
            def __init__(self, year, name):
                self.year = year
                self.name = name

Tests:
    >>> melissa = Astronaut('Melissa Lewis')
    >>> print(f'Commander: \\n{melissa}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Commander:
    Melissa Lewis

    >>> mark = Astronaut('Mark Watney', experience=[
    ...    Mission(2035, 'Ares 3')])
    >>> print(f'Space Pirate: \\n{mark}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Space Pirate:
    Mark Watney veteran of [
          2035: Ares 3]

    >>> crew = Crew([
    ...     Astronaut('Jan Twardowski', experience=[
    ...         Mission(1969, 'Apollo 11'),
    ...         Mission(2024, 'Artemis 3'),
    ...     ]),
    ...     Astronaut('José Jiménez'),
    ...     Astronaut('Mark Watney', experience=[
    ...         Mission(2035, 'Ares 3'),
    ...     ]),
    ... ])

    >>> print(f'Crew: \\n{crew}')  # doctest: +NORMALIZE_WHITESPACE
    Crew:
    Jan Twardowski veteran of [
          1969: Apollo 11,
          2024: Artemis 3]
    José Jiménez
    Mark Watney veteran of [
          2035: Ares 3]

