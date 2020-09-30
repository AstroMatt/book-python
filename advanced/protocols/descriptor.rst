**********
Descriptor
**********


Rationale
=========
* Add managed attributes to objects
* Outsource functionality into specialized classes
* ``__del__(self)`` is reserved when object is being deleted by garbage collector (destructor)


Protocol
========
* ``__get__(self, parent, parent_type=None) -> self``
* ``__set__(self, parent, value) -> None``
* ``__delete__(self, parent) -> None``


Use Cases
=========
* ``@classmethod``
* ``@staticmethod``
* ``@property``
* functions in general


Syntax
======
.. code-block:: python
    :caption: Definition

    class MyField:
        def __get__(self, parent, parent_type):
            return ...

        def __set__(self, parent, value):
            ...

        def __delete__(self, parent):
            ...

.. code-block:: python
    :caption: Usage

    class MyField:
        def __get__(self, parent, parent_type):
            print('Getter')

        def __set__(self, parent, value):
            print('Setter')

        def __delete__(self, parent):
            print('Deleter')


    class MyClass:
        value = MyField()

        def __init__(self):
            self._currentvalue = 0.0


    my = MyClass()

    my.value = 'something'
    # Getter

    my.value
    # Setter

    del my.value
    # Deleter


.. code-block:: python
    :caption: Inside class

    class MyClass:
        class MyField:
            def __get__(self, parent, parent_type):
                print('Calling MyField.__get__()')

            def __set__(self, parent, value):
                print('Calling MyField.__set__()')

            def __delete__(self, parent):
                print('Calling MyField.__delete__()')

        value = MyField()

        def __init__(self):
            self._currentvalue = 0.0


    my = MyClass()

    my.value = 'something'
    # Calling MyField.__set__()

    my.value
    # Calling MyField.__get__()

    del my.value
    # Calling MyField.__delete__()


Examples
========
.. code-block:: python
    :caption: Kelvin Temperature Validator

    class KelvinValidator:
        def __get__(self, parent, parent_type):
            return round(parent._current_value, 2)

        def __set__(self, parent, value):
            if value < 0.0:
                raise ValueError('Cannot set negative Kelvin')
            parent._current_value = value

        def __delete__(self, parent):
            parent._current_value = 0.0


    class Temperature:
        kelvin = KelvinValidator()

        def __init__(self):
            self._current_value = 0.0


    t = Temperature()

    t.kelvin = -1
    # Traceback (most recent call last):
    # ValueError: Cannot set negative Kelvin

    t.kelvin = 10

    print(t.kelvin)
    # 10

    del t.kelvin

    print(t.kelvin)
    # 0.0

.. code-block:: python
    :caption: Temperature Conversion

    class Kelvin:
        def __get__(self, parent, parent_type):
            return round(parent._current_value, 2)

        def __set__(self, parent, value):
            parent._current_value = value

        def __delete__(self, parent):
            parent._current_value = 0


    class Celsius:
        def __get__(self, parent, parent_type):
            temp = parent._current_value - 273.15
            return round(temp, 2)

        def __set__(self, parent, value):
            temp = value + 273.15
            parent._current_value = temp

        def __delete__(self, parent):
            self.__set__(parent, 0)


    class Fahrenheit:
        def __get__(self, parent, parent_type):
            temp = (parent._current_value - 273.15) * 9 / 5 + 32
            return round(temp, 2)

        def __set__(self, parent, fahrenheit):
            temp = (fahrenheit - 32) * 5 / 9 + 273.15
            parent._current_value = temp

        def __delete__(self, parent):
            self.__set__(parent, 0)


    class Temperature:
        kelvin = Kelvin()
        celsius = Celsius()
        fahrenheit = Fahrenheit()

        def __init__(self):
            self._current_value = 0.0


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

    print()

    del t.celsius
    print(f'K: {t.kelvin}')         # 273.15
    print(f'C: {t.celsius}')        # 0.0
    print(f'F: {t.fahrenheit}')     # 32.0

    print()

    del t.fahrenheit
    print(f'K: {t.kelvin}')         # 255.37
    print(f'C: {t.celsius}')        # -17.78
    print(f'F: {t.fahrenheit}')     # 0

.. code-block:: python
    :caption: Timezone Conversion
    :name: Timezone Conversion

    from dataclasses import dataclass
    from datetime import datetime
    from pytz import timezone


    class Timezone:
        def __init__(self, name):
            self.timezone = timezone(name)

        def __get__(self, parent, *args, **kwargs):
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

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zaimplementuj klasę ``Temperature``
    #. Klasa przetrzymuje wartości jako Kelwiny używając deskryptora
    #. Temperatura musi być zawsze być dodatnia
    #. Użyj deskryptorów do sprawdzania wartości granicznych przy każdej modyfikacji
    #. Wszystkie testy muszą przejść

:Input:
    .. code-block:: python

        class Temperature:
            """
            >>> t = Temperature()
            >>> t.kelvin = 1
            >>> t.kelvin
            1
            >>> t.kelvin = -1
            Traceback (most recent call last):
                ...
            ValueError: Negative temperature
            """

:The whys and wherefores:
    * Using descriptors
    * Data validation

Protocol Descriptor Inheritance
-------------------------------
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

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zamodeluj klasę ``GeographicCoordinate``
    #. Użyj deskryptory do sprawdzania wartości brzegowych
    #. Kasowanie pola powinno ustawiać jego wartość na ``None``
    #. Zablokuj modyfikację pola ``elevation``
    #. Zezwól na ustawianie pola ``elevation`` podczas inicjalizacji
    #. Wszystkie testy muszą przejść

:Input:
    .. code-block:: text

        latitude - type: float, min: -90, max 90
        longitude - type: float, min: -180, max: 180
        elevation - type: float, min: -10994, max: 8848

    .. code-block:: python

        class GeographicCoordinate:
            """
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
            """
            def __str__(self):
                return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'

            def __repr__(self):
                return self.__str__()


:The whys and wherefores:
    * Using descriptors
    * Data validation
