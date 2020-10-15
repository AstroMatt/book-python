.. _Protocol Property:

********
Property
********


Rationale
=========
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions (TypeError)
* Check argument type


Protocol
========
* ``value = property()`` - creates property
* ``@value.getter`` - getter for attribute (``value`` has to be ``property``)
* ``@value.setter`` - setter for attribute (``value`` has to be ``property``)
* ``@value.deleter`` - deleter for attribute (``value`` has to be ``property``)
* ``@property`` - creates property and a getter

Syntax:
    .. code-block:: python

        class MyClass:

            @property
            def myattribute(self):
                return ...

Alternative:
    .. code-block:: python

        class MyClass:
            myattribute = property()

            @myattribute.getter
            def myattribute(self):
                return ...

Are equivalent to:
    .. code-block:: python

        class MyClass:

            def myattribute(self):
                return ...

            myattribute = property(myattribute)


Example
=======
.. code-block:: python

    class Astronaut:
        name = property()

        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        @property
        def name(self):
            return f'{self._firstname} {self._lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')
    print(astro.name)
    # Mark W.

.. code-block:: python

    class Temperature:
        kelvin = property()

        def __init__(self, kelvin=None):
            self._kelvin = kelvin

        @kelvin.setter
        def kelvin(self, value):
            if value < 0:
                raise ValueError('Negative Kelvin Temperature')


    t = Temperature()
    t.kelvin = 10
    t.kelvin = -1
    # Traceback (most recent call last):
    #     ...
    # ValueError: Negative Kelvin Temperature


Attribute Access
================
* Java way: Setter and Getter
* Pythonic way: Properties, Reflection, Descriptors

.. code-block:: python
    :caption: Accessing class fields using setter and getter

    class Astronaut:
        def __init__(self, name=None):
            self._name = name

        def set_name(self, name):
            self._name = name

        def get_name(self):
            return self._name


    astro = Astronaut()
    astro.set_name('Mark Watney')
    print(astro.get_name())
    # Mark Watney

.. code-block:: python
    :caption: Accessing class fields. Either put ``name`` as an argument for ``__init__()`` or create dynamic field in runtime

    class Astronaut:
        def __init__(self, name=None):
            self.name = name


    astro = Astronaut()
    astro.name = 'Jan Twardowski'
    print(astro.name)
    # Jan Twardowski


Property class
==============
* Property's arguments are method pointers ``get_name``, ``set_name``, ``del_name`` and a docstring
* Don't do that

.. code-block:: python

    class Astronaut:
        def __init__(self, name=None):
            self._name = name

        def get_name(self):
            return self._name

        def set_name(self, value):
            self._name = value

        def del_name(self):
            del self._name

        name = property(get_name, set_name, del_name, "I am the 'name' property.")


@property Decorator
===================
* Prefer ``name = property()``

.. code-block:: python

    class Astronaut:
        name = property()

        def __init__(self, name=None):
            self._name = name

        @name.getter
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @name.deleter
        def name(self):
            del self._name

.. code-block:: python

    class Astronaut:
        def __init__(self, name=None):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @name.deleter
        def name(self):
            del self._name


Use Cases
=========

Astronaut
---------
.. code-block:: python

    class Astronaut:
        def __init__(self):
            self._name = None

        def set_name(self, name):
            self._name = name.title()

        def get_name(self):
            if self._name:
                firstname, lastname = self._name.split()
                return f'{firstname} {lastname[0]}.'

        def del_name(self):
            self._name = None


    astro = Astronaut()

    astro.set_name('JaN TwARdoWskI')
    print(astro.get_name())
    # Jan T.

    astro.del_name()
    print(astro.get_name())
    # None

.. code-block:: python

    class Astronaut:
        name = property()

        def __init__(self):
            self._name = None

        @name.getter
        def name(self):
            if self._name:
                firstname, lastname = self._name.split()
                return f'{firstname} {lastname[0]}.'

        @name.setter
        def name(self, name):
            self._name = name.title()

        @name.deleter
        def name(self):
            self._name = None


    astro = Astronaut()

    astro.name = 'JAN TwARdoWski'
    print(astro.name)
    # Jan T.

    del astro.name
    print(astro.name)
    # None

Temperature
-----------
.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            print('You are trying to access a value')
            return self._protected


    t = Temperature(100)

    print(t.value)
    # You are trying to access a value
    # 100

.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            return self._protected

        @value.setter
        def value(self, new_value):
            if new_value < 0.0:
                raise ValueError('Kelvin Temperature cannot be negative')
            else:
                self._protected = new_value


    t = Temperature(100)
    t.value = -10
    # Traceback (most recent call last):
    #     ...
    # ValueError: Kelvin Temperature cannot be negative

.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            return self._protected

        @value.deleter
        def value(self):
            print('Resetting temperature')
            self._protected = 0.0


    t = Temperature(100)

    del t.value
    # Resetting temperature

    print(t.value)
    # 0.0


Assignments
===========

Protocol Property
-----------------
* Assignment name: Protocol Property
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 14 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_property.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Add ``position`` property which returns tuple ``(x, y, z)``
    #. Deleting ``position`` sets all attributes to 0 (``x=0``, ``y=0``, ``z=0``)
    #. Prevent setting position
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Define klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Dodaj property ``position``, który zwraca tuple ``(x, y, z)``
    #. Usunięcie ``position`` ustawia wszystkie atrybuty na 0 (``x=0``, ``y=0``, ``z=0``)
    #. Zablokuj edycję atrybutów
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> pt = Point(x=1, y=2, z=3)
        >>> pt.position
        (1, 2, 3)
        >>> del pt.position
        >>> pt.position
        (0, 0, 0)
        >>> pt.position = (4, 5, 6)
        Traceback (most recent call last):
            ...
        PermissionError: Cannot modify values
