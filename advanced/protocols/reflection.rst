.. _Protocol Reflection:

**********
Reflection
**********


Rationale
=========
* When accessing an attribute
* Built-in Functions:

    * ``setattr(obj, 'attrname', 'new_value') -> None``
    * ``delattr(obj, 'attrname') -> None``
    * ``getattr(obj, 'attrname', 'default_value') -> Any``
    * ``hasattr(obj, 'attrname') -> bool``

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Mark Watney')

    if astro._salary is None:
        astro._salary = 100
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '_salary'


    if not hasattr(astro, '_salary'):
        astro._salary = 100

    print(astro._salary)
    # 100


    attrname = input('Type attribute name: ')
    value = getattr(astro, attrname, 'no such attribute')
    print(value)

    # Type attribute name: >? name
    # Mark Watney

    # Type attribute name: >? _salary
    # 100

    # Type attribute name: >? notexisting
    # no such attribute


Protocol
========
* ``__setattr__(self, attrname, value) -> None``
* ``__delattr__(self, attrname) -> None``
* ``__getattribute__(self, attrname, default) -> Any``
* ``__getattr__(self, attrname, default) -> Any``

.. code-block:: python

    class Reflection:

        def __setattr__(self, attrname, value):
            ...

        def __delattr__(self, attrname):
            ...

        def __getattribute__(self, attrname, default):
            ...

        def __getattr__(self, attrname, default):
            ...


Example
=======
.. code-block:: python

    class Immutable:
        def __setattr__(self, attrname, value):
            raise PermissionError('Immutable')

.. code-block:: python

    class Protected:
        def __setattr__(self, attrname, value):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(attrname, value)


Set Attribute
=============
* Called when trying to set attribute to a value
* Call Stack:

    * ``astro.name = 'Mark Watney'``
    * => ``setattr(astro, 'name', 'Mark Watney')``
    * => ``astro.__setattr__('name', 'Mark Watney')``

.. code-block:: python

    class Astronaut:
        def __setattr__(self, attrname, value):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(attrname, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # Traceback (most recent call last):
    # PermissionError: Field is protected


Delete Attribute
================
* Called when trying to delete attribute
* Call stack:

    * ``del astro.name``
    * => ``delattr(astro, 'name')``
    * => ``astro.__delattr__(name)``

.. code-block:: python

    class Astronaut:
        def __delattr__(self, attrname):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__delattr__(attrname)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro._salary = 100

    del astro.name
    del astro._salary
    # Traceback (most recent call last):
    # PermissionError: Field is protected


Get Attribute
=============
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* If attribute is not found, then raises ``AttributeError`` and calls ``__getattr__()``
* Call stack:

    * ``astro.name``
    * => ``getattr(astro, 'name')``
    * => ``astro.__getattribute__('name')``
    * if ``astro.__getattribute__('name')`` raises ``AttributeError``
    * => ``astro.__getattr__('name')``

.. code-block:: python

    class Astronaut:
        def __getattribute__(self, attrname):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__getattribute__(attrname)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    print(astro._salary)
    # Traceback (most recent call last):
    # PermissionError: Field is protected


Get Attribute if Missing
========================
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes

.. code-block:: python
    :caption: Example ``__getattr__()``

    class Astronaut:
        def __init__(self):
            self.name = None

        def __getattr__(self, attrname):
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
            self.name = None

        def __getattribute__(self, attrname):
            print('Getattribute called... ')
            result = super().__getattribute__(attrname)
            print(f'Result was: "{result}"')
            return result

        def __getattr__(self, attrname):
            print('Not found. Getattr called...')
            print(f'Creating attribute {attrname} with `None` value')
            super().__setattr__(attrname, None)



    astro = Astronaut()
    astro.name = 'Mark Watney'

    astro.name
    # Getattribute called...
    # Result was: "Mark Watney"
    # 'Mark Watney'

    astro._salary
    # Getattribute called...
    # Not found. Getattr called...
    # Creating attribute _salary with `None` value

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
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Mark Watney')

    hasattr(astro, 'name')
    # True

    hasattr(astro, 'mission')
    # False

    astro.mission = 'Ares3'
    hasattr(astro, 'mission')
    # True


Use Cases
=========
.. code-block:: python

    class Astronaut:
        def __getattribute__(self, attrname):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__getattribute__(attrname)

        def __setattr__(self, attrname, value):
            if attrname.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(attrname, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # Traceback (most recent call last):
    # PermissionError: Field is protected

    print(astro._salary)
    # Traceback (most recent call last):
    # PermissionError: Field is protected

.. code-block:: python

    class Temperature:
        kelvin: float

        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, attrname, value):
            if attrname == 'kelvin' and value < 0.0:
                raise ValueError('Kelvin temperature cannot be negative')
            else:
                return super().__setattr__(attrname, value)


    t = Temperature(100)

    t.kelvin = 20
    print(t.kelvin)
    # 20

    t.kelvin = -10
    # Traceback (most recent call last):
    # ValueError: Kelvin temperature cannot be negative

.. code-block:: python

    class Temperature:
        kelvin: float
        celsius: float
        fahrenheit: float

        def __getattr__(self, attrname):
            if attrname == 'kelvin':
                return super().__getattribute__('kelvin')
            if attrname == 'celsius':
                return self.kelvin - 273.15
            if attrname == 'fahrenheit':
                return (self.kelvin-273.15) * 1.8 + 32


    t = Temperature()
    t.kelvin = 373.15

    print(t.kelvin)
    # 373.15

    print(t.celsius)
    # 100.0

    print(t.fahrenheit)
    # 212.0


Assignments
===========

.. literalinclude:: assignments/protocol_reflection_delattr.py
    :caption: :download:`Solution <assignments/protocol_reflection_delattr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_reflection_setattr.py
    :caption: :download:`Solution <assignments/protocol_reflection_setattr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_reflection_frozen.py
    :caption: :download:`Solution <assignments/protocol_reflection_frozen.py>`
    :end-before: # Solution
