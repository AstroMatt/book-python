.. _OOP Descriptor:

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
    #    ...
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

        def __delete__(self, parent):
            parent.utc = datetime(1, 1, 1)


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

Protocol Descriptor Simple
--------------------------
* Assignment name: Protocol Descriptor Simple
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_descriptor_simple.py`

:English:
    #. Use data from "Input" section (see below)
    #. Implement class ``Temperature``
    #. Class stores values in Kelvins using descriptor
    #. Temperature must always be positive
    #. Use descriptors to check boundaries at each value modification
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zaimplementuj klasę ``Temperature``
    #. Klasa przetrzymuje wartości jako Kelwiny używając deskryptora
    #. Temperatura musi być zawsze być dodatnia
    #. Użyj deskryptorów do sprawdzania wartości granicznych przy każdej modyfikacji
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> t = Temperature()
        >>> t.kelvin = 1
        >>> t.kelvin
        1
        >>> t.kelvin = -1
        Traceback (most recent call last):
            ...
        ValueError: Negative temperature

:The whys and wherefores:
    * Using descriptors
    * Data validation

Protocol Descriptor Inheritance
-------------------------------
* Assignment name: Protocol Descriptor Inheritance
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_descriptor_inheritance.py`

:English:
    #. Use data from "Input" section (see below)
    #. Model the class ``GeographicCoordinate``
    #. Use descriptors to check value boundaries
    #. Deleting field should set it to ``None``
    #. Disable modification of ``elevation`` field
    #. Allow to set ``elevation`` field at the class initialization
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zamodeluj klasę ``GeographicCoordinate``
    #. Użyj deskryptory do sprawdzania wartości brzegowych
    #. Kasowanie pola powinno ustawiać jego wartość na ``None``
    #. Zablokuj modyfikację pola ``elevation``
    #. Zezwól na ustawianie pola ``elevation`` podczas inicjalizacji
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: text

        latitude - min: -90.0, max 90.0
        longitude -  min: -180.0, max: 180.0
        elevation -  min: -10994.0, max: 8848.0

    .. code-block:: python

        class GeographicCoordinate:
            def __str__(self):
                return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'

            def __repr__(self):
                return self.__str__()

:Output:
    .. code-block:: text

        >>> GeographicCoordinate(90, 0, 0)
        Latitude: 90, Longitude: 0, Elevation: 0
        >>> GeographicCoordinate(-90, 0, 0)
        Latitude: -90, Longitude: 0, Elevation: 0
        >>> GeographicCoordinate(0, +180, 0)
        Latitude: 0, Longitude: 180, Elevation: 0
        >>> GeographicCoordinate(0, -180, 0)
        Latitude: 0, Longitude: -180, Elevation: 0
        >>> GeographicCoordinate(0, 0, +8848)
        Latitude: 0, Longitude: 0, Elevation: 8848
        >>> GeographicCoordinate(0, 0, -10994)
        Latitude: 0, Longitude: 0, Elevation: -10994

        >>> place1 = GeographicCoordinate(50, 120, 8000)
        >>> str(place1)
        'Latitude: 50, Longitude: 120, Elevation: 8000'

        >>> place2 = GeographicCoordinate(22, 33, 44)
        >>> str(place2)
        'Latitude: 22, Longitude: 33, Elevation: 44'

        >>> place1.longitude = 0
        >>> place1.latitude = 0
        >>> place1.elevation = 0
        Traceback (most recent call last):
          ...
        PermissionError: Changing value is prohibited.

        >>> place1.latitude = 1
        >>> place1.longitude = 2
        >>> str(place1)
        'Latitude: 1, Longitude: 2, Elevation: 8000'

        >>> str(place2)
        'Latitude: 22, Longitude: 33, Elevation: 44'


        >>> GeographicCoordinate(-91, 0, 0)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

        >>> GeographicCoordinate(+91, 0, 0)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

        >>> GeographicCoordinate(0, -181, 0)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

        >>> GeographicCoordinate(0, +181, 0)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

        >>> GeographicCoordinate(0, 0, -10995)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

        >>> GeographicCoordinate(0, 0, +8849)
        Traceback (most recent call last):
          ...
        ValueError: Out of bounds

:The whys and wherefores:
    * Using descriptors
    * Data validation
