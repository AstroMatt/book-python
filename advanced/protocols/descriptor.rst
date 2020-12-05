.. _Protocol Descriptor:

**********
Descriptor
**********


Rationale
=========
* Add managed attributes to objects
* Outsource functionality into specialized classes
* Descriptors: ``classmethod``, ``staticmethod``, ``property``, functions in general
* ``__del__(self)`` is reserved when object is being deleted by garbage collector (destructor)


Protocol
========
* ``__get__(self, parent, *args) -> self``
* ``__set__(self, parent, value) -> None``
* ``__delete__(self, parent) -> None``

.. code-block:: python

    class Descriptor:
        def __get__(self, parent, *args):
            return ...

        def __set__(self, parent, value):
            ...

        def __delete__(self, parent):
            ...


Example
=======
.. code-block:: python

    class MyField:
        def __get__(self, parent, *args):
            print('Getter')

        def __set__(self, parent, value):
            print('Setter')

        def __delete__(self, parent):
            print('Deleter')


    class MyClass:
        value = MyField()


    my = MyClass()

    my.value = 'something'
    # Setter

    my.value
    # Getter

    del my.value
    # Deleter


Use Cases
=========
.. code-block:: python
    :caption: Kelvin Temperature Validator

    class KelvinValidator:
        def __set__(self, parent, value):
            if value < 0.0:
                raise ValueError('Cannot set negative Kelvin')
            parent._value = value


    class Temperature:
        kelvin = KelvinValidator()

        def __init__(self):
            self._value = None


    t = Temperature()

    t.kelvin = 10
    print(t.kelvin)
    # 10

    t.kelvin = -1
    # Traceback (most recent call last):
    # ValueError: Cannot set negative Kelvin

.. code-block:: python
    :caption: Temperature Conversion

    class Kelvin:
        def __get__(self, parent, *args):
            return round(parent._value, 2)

        def __set__(self, parent, value):
            parent._value = value


    class Celsius:
        def __get__(self, parent, *args):
            value = parent._value - 273.15
            return round(value, 2)

        def __set__(self, parent, value):
            parent._value = value + 273.15


    class Fahrenheit:
        def __get__(self, parent, *args):
            value = (parent._value - 273.15) * 9 / 5 + 32
            return round(value, 2)

        def __set__(self, parent, fahrenheit):
            parent._value = (fahrenheit - 32) * 5 / 9 + 273.15


    class Temperature:
        kelvin = Kelvin()
        celsius = Celsius()
        fahrenheit = Fahrenheit()

        def __init__(self):
            self._value = 0.0


    t = Temperature()

    t.kelvin = 273.15
    print(f'K: {t.kelvin}')         # 273.15
    print(f'C: {t.celsius}')        # 0.0
    print(f'F: {t.fahrenheit}')     # 32.0

    print()

    t.fahrenheit = 100
    print(f'K: {t.kelvin}')         # 310.93
    print(f'C: {t.celsius}')        # 37.78
    print(f'F: {t.fahrenheit}')     # 100.0

    print()

    t.celsius = 100
    print(f'K: {t.kelvin}')         # 373.15
    print(f'C: {t.celsius}')        # 100.0
    print(f'F: {t.fahrenheit}')     # 212.0

.. code-block:: python

    class ValueRange:
        name: str
        min: float
        max: float
        value: float

        def __init__(self, name, min, max):
            self.name = name
            self.min = min
            self.max = max

        def __set__(self, parent, value):
            if value not in range(self.min, self.max):
                raise ValueError(f'{self.name} is not between {self.min} to {self.max}')
            self.value = value


    class Astronaut:
        name: str
        age = ValueRange('Age', min=28, max=42)
        height = ValueRange('Height', min=150, max=200)

        def __init__(self, name, age, height):
            self.name = name
            self.height = height
            self.age = age

        def __repr__(self):
            name = self.name
            age = self.age.value
            height = self.height.value
            return f'Astronaut({name=}, {age=}, {height=})'


    Astronaut('Mark Watney', age=38, height=170)
    # Astronaut(name='Mark Watney', age=38, height=170)

    Astronaut('Mark Watney', age=44, height=170)
    # Traceback (most recent call last):
    # ValueError: Age is not between 28 to 42

    Astronaut('Mark Watney', age=38, height=210)
    # Traceback (most recent call last):
    # ValueError: Height is not between 150 to 200

.. figure:: img/datetime-compare.png
    :scale: 66%
    :align: center

    Comparing datetime works only when all has the same timezone (UTC). More information in :ref:`Stdlib Datetime Timezone`

.. code-block:: python
    :caption: Descriptor Timezone Converter
    :name: Descriptor Timezone Converter

    from dataclasses import dataclass
    from datetime import datetime
    from pytz import timezone


    class Timezone:
        def __init__(self, name):
            self.timezone = timezone(name)

        def __get__(self, parent, *args):
            return parent.utc.astimezone(self.timezone)

        def __set__(self, parent, new_datetime):
            local_time = self.timezone.localize(new_datetime)
            parent.utc = local_time.astimezone(timezone('UTC'))


    @dataclass
    class Time:
        utc = datetime.now(tz=timezone('UTC'))
        warsaw = Timezone('Europe/Warsaw')
        moscow = Timezone('Europe/Moscow')
        est = Timezone('America/New_York')
        pdt = Timezone('America/Los_Angeles')


    t = Time()

    print('Launch of a first man to space:')
    t.moscow = datetime(1961, 4, 12, 9, 6, 59)
    print(t.utc)        # 1961-04-12 06:06:59+00:00
    print(t.warsaw)     # 1961-04-12 07:06:59+01:00
    print(t.moscow)     # 1961-04-12 09:06:59+03:00
    print(t.est)        # 1961-04-12 01:06:59-05:00
    print(t.pdt)        # 1961-04-11 22:06:59-08:00

    print('First man set foot on a Moon:')
    t.warsaw = datetime(1969, 7, 21, 3, 56, 15)
    print(t.utc)        # 1969-07-21 02:56:15+00:00
    print(t.warsaw)     # 1969-07-21 03:56:15+01:00
    print(t.moscow)     # 1969-07-21 05:56:15+03:00
    print(t.est)        # 1969-07-20 22:56:15-04:00
    print(t.pdt)        # 1969-07-20 19:56:15-07:00


Assignments
===========

.. literalinclude:: assignments/protocol_descriptor_simple.py
    :caption: :download:`Solution <assignments/protocol_descriptor_simple.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_descriptor_valuerange.py
    :caption: :download:`Solution <assignments/protocol_descriptor_valuerange.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_descriptor_inheritance.py
    :caption: :download:`Solution <assignments/protocol_descriptor_inheritance.py>`
    :end-before: # Solution
