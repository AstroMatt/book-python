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

.. literalinclude:: assignments/oop_stringify_str.py
    :caption: :download:`Solution <assignments/oop_stringify_str.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_repr.py
    :caption: :download:`Solution <assignments/oop_stringify_repr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_format.py
    :caption: :download:`Solution <assignments/oop_stringify_format.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_nested.py
    :caption: :download:`Solution <assignments/oop_stringify_nested.py>`
    :end-before: # Solution
