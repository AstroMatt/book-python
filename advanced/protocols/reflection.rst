**********
Reflection
**********


Rationale
=========
* Act on accessing an attribute


Syntax
======
Built-in Functions:

    * ``setattr(obj, 'attribute_name', 'new value') -> None``
    * ``delattr(obj, 'attribute_name') -> None``
    * ``getattr(obj, 'attribute_name', 'default value') -> Any``
    * ``hasattr(obj, 'attribute_name') -> bool``

Protocol:

    * ``__setattr__(self, attribute_name, value)``
    * ``__delattr__(self, attribute_name)``
    * ``__getattr__(self, attribute_name, default)``
    * ``__getattribute__(self, attribute_name, default)``


Set Attribute
=============
* Called when trying to set attribute to a value
* ``setattr(astro, 'name', 'value')`` is equivalent to ``astro.name = 'value'``
* Call Stack:

    * ``astro.name = 'Mark Watney'``
    * => ``setattr(astro, 'name', 'Mark Watney')``
    * => ``astro.__setattr__('name', 'Mark Watney')``

.. code-block:: python

    class Astronaut:

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "set" value.')
            else:
                return super().__setattr__(name, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.


Delete Attribute
================
* Called when trying to delete attribute
* ``delattr(astro, 'name')`` is equivalent to ``del astro.name``
* Call stack:

    * ``del astro.name``
    * => ``delattr(astro, 'name')``
    * => ``astro.__delattr__(name)``

.. code-block:: python

    class Astronaut:

        def __delattr__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "delete" value.')
            else:
                return super().__delattr__(name)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro._salary = 100

    del astro.name
    del astro._salary
    # PermissionError: Field "_salary" is protected, cannot "delete" value.


Get Attribute
=============
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* ``getattr(astro, 'name')`` is equivalent to ``astro.name``
* if ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``
* Call stack:

    * ``astro.name``
    * => ``getattr(astro, 'name')``
    * => ``astro.__getattribute__('name')``
    * if ``astro.__getattribute__('name')`` raise ``AttributeError``
    * => ``astro.__getattr__('name')``

.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "get" value.')
            else:
                return super().__getattribute__(name)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    print(astro._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.


Get Attribute if Does Not Exist
===============================
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes
* If ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``

.. code-block:: python
    :caption: Example ``__getattr__()``

    class Astronaut:
        def __init__(self):
            self.fullname = None

        def __getattr__(self, name):
            return 'Sorry, field does not exist'


    astro = Astronaut()
    astro.name = 'Mark Watney'

    print(astro.name)
    # Mark Watney

    print(astro._salary)
    # Sorry, field does not exist

.. code-block:: python

    class Astronaut:
        def __init__(self):
            self.fullname = None

        def __getattribute__(self, name):
            print('Getattribute called... ')
            result = super().__getattribute__(name)
            print(f'Result was: "{result}"')
            return result

        def __getattr__(self, name):
            print('Not found. Getattr called...')
            print(f'Creating attibute {name} with `None` value')
            super().__setattr__(name, None)


    astro = Astronaut()
    astro.name = 'Mark Watney'

    astro.name
    # Getattribute called...
    # Result was: "Mark Watney"

    astro._salary
    # Getattribute called...
    # Not found. Getattr called...
    # Creating attibute _salary with `None` value

    astro._salary
    # Getattribute called...
    # Result was: "None"


Has Attribute
=============
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calls ``__getattribute__()`` and checks if raises ``AttributeError``

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(hasattr(astro, 'firstname'))     # True
    print(hasattr(astro, 'lastname'))      # True
    print(hasattr(astro, 'fullname'))      # False

    astro.fullname = 'Mark Watney'

    print(hasattr(astro, 'fullname'))
    # True


Examples
========
.. code-block:: python

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "get" value.')
            else:
                return super().__getattribute__(name)

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "set" value.')
            else:
                return super().__setattr__(name, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.

    print(astro._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.

.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, name, value):
            if value < 0.0:
                raise ValueError('Kelvin temperature cannot be negative')
            else:
                return super().__setattr__(name, value)


    t = Temperature(100)

    t.kelvin = 20
    print(t.kelvin)
    # 20

    t.kelvin = -10
    # ValueError: Kelvin temperature cannot be negative

.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, name, value):
            super().__setattr__(name, value)

            if name == 'kelvin':
                self.celsius = 273.15 + self.kelvin
                self.fahrenheit = (self.kelvin-273.15) * 1.8 + 32


    t = Temperature(100)

    print(t.kelvin)
    # 100

    print(t.celsius)
    # 373.15

    print(t.fahrenheit)
    # -279.66999999999996


Assignments
===========

Protocol Reflection
-------------------
* Assignment name: Protocol Reflection
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 30 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_reflection.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent adding new attributes
    #. Prevent deleting attributes
    #. Prevent changing attributes
    #. Allow to set attributes only at the initialization
    #. All tests must pass

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj możliwość dodawania nowych atrybutów
    #. Zablokuj możliwość usuwania atrybutów
    #. Zablokuj edycję atrybutów
    #. Pozwól na ustawianie atrybutów tylko przy inicjalizacji klasy
    #. Wszystkie testy muszą przejść

:Input:
    .. code-block:: python

        class Point:
            """
            >>> pt = Point(1, 2, 3)
            >>> pt.x
            1
            >>> pt.y
            2
            >>> pt.z
            3

            >>> del pt.x
            Traceback (most recent call last):
                ...
            PermissionError: Cannot delete attibutes

            >>> del pt.notexisting
            Traceback (most recent call last):
                ...
            PermissionError: Cannot delete attibutes

            >>> pt.x = 10
            Traceback (most recent call last):
                ...
            PermissionError: Cannot modify existing attributes

            >>> pt.notexisting = 10
            Traceback (most recent call last):
                ...
            PermissionError: Cannot set other attributes than x,y,z
            """
