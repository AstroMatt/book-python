**********
Properties
**********


Setter and Getter Methods
=========================
* Java way
* don't do that in Python

.. code-block:: python
    :caption: Accessing class fields using setter and getter

    class Astronaut:
        def __init__(self, name=None):
            self.name = name

        def set_name(self, name):
            self._name = name

        def get_name(self):
            return self._name


    astro = Astronaut()

    astro.set_name('Mark Watney')
    print(astro.get_name())
    # Mark Watney

.. code-block:: python
    :caption: Problem with setters and getters

    class MyClass:
        def __init__(self):
            self._x = None
            self._y = None

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def del_x(self):
            del self._x

        def get_y(self):
            return self._y

        def set_y(self, value):
            self._x = value

        def del_y(self):
            del self._y

.. code-block:: python
    :caption: Rationale for Setters and Getters

    class Astronaut:
        def __init__(self):
            self._name = None

        def set_name(self, name):
            self._name = name.title()

        def get_name(self):
            firstname, lastname = self._name.split()
            return f'{firstname} {lastname[0]}.'


    astro = Astronaut()

    astro.set_name('JaN TwARdoWskI')
    print(astro.get_name())
    # Jan T.

.. code-block:: python
    :caption: Rationale for Setters and Getters `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor admin
    :emphasize-lines: 9,14-20

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.sensors.models import ZWaveSensor


    @admin.register(ZWaveSensor)
    class ZWaveSensorAdmin(HabitatAdmin):
        change_list_template = 'sensors/change_list_charts.html'
        list_display = ['mission_date', 'mission_time', 'type', 'device', 'value', 'unit']
        list_filter = ['created', 'type', 'unit', 'device']
        search_fields = ['^date', 'device']
        ordering = ['-datetime']

        def get_list_display(self, request):
            list_display = self.list_display

            if request.user.is_superuser:
                list_display = ['earth_datetime'] + list_display

            return list_display


Direct Attribute Access
=======================
* Pythonic way

.. code-block:: python
    :caption: Accessing class fields. Either put ``name`` as an argument for ``__init__()`` or create dynamic field in runtime

    class Astronaut:
        def __init__(self, name=None):
            self.name = name


    astro = Astronaut()
    astro.name = 'Jan Twardowski'

    print(astro.name)
    # Jan Twardowski


Properties
==========
* ``@property`` - for defining getters
* ``@value.getter`` - defining getter for field (require field to be ``@property``)
* ``@value.setter`` - defining setter for field (require field to be ``@property``)
* ``@value.deleter`` - defining deleter for field (require field to be ``@property``)

Rationale
---------
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions (TypeError)
* Check argument type

.. code-block:: python
    :caption: Property class

    property()
    # <property object at 0x10ff07940>

    property().getter
    # <built-in method getter of property object at 0x10ff07998>

    property().setter
    # <built-in method setter of property object at 0x10ff07940>

    property().deleter
    # <built-in method deleter of property object at 0x10ff07998>

Property decorator
------------------
* ``@decorator`` syntax is just syntactic sugar; the syntax:

    .. code-block:: python

        class MyClass:

            @property
            def attribute(self):
                return self._attribute

* really means the same thing as

    .. code-block:: python

        class MyClass:

            def attribute(self):
                return self._attribute

            attribute = property(attribute)

Creating properties with ``property`` class
-------------------------------------------
* Property's arguments are method pointers ``get_name``, ``set_name``, ``del_name`` and a docstring

.. code-block:: python
    :caption: Properties

    class Astronaut:
        def __init__(self):
            self._protected = None

        def get_name(self):
            return self._protected

        def set_name(self, value):
            self._protected = value

        def del_name(self):
            del self._protected

        name = property(get_name, set_name, del_name, "I am the 'name' property.")

Creating properties with ``@property`` decorator
------------------------------------------------
.. code-block:: python
    :emphasize-lines: 5-11

    class Astronaut:
        name = property()

        def __init__(self):
            self._protected = None

        @name.getter
        def name(self):
            return self._protected

        @name.setter
        def name(self, value):
            self._protected = value

        @name.deleter
        def name(self):
            del self._protected

.. code-block:: python
    :caption: Properties as a decorators
    :emphasize-lines: 5-7

    class Astronaut:
        def __init__(self):
            self._protected = None

        @property
        def name(self):
            return self._protected

        @name.setter
        def name(self, value):
            self._protected = value

        @name.deleter
        def name(self):
            del self._protected


Use Cases
=========
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


Examples
========
.. code-block:: python
    :caption: Using ``@property`` as a getter

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
    :caption: ``@x.setter``

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
    # ValueError: Kelvin Temperature cannot be negative


Deleter
-------
* ``@value.deleter`` - for defining deleter for field ``value``
* Require ``value`` to be ``@property``

.. code-block:: python
    :caption: ``@x.deleter``

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
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 35 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_property.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Add ``position`` property which returns tuple ``(x, y, z)``
    #. Deleting ``position`` sets all attributes to 0 (``x=0``, ``y=0``, ``z=0``)
    #. Prevent setting position
    #. All tests must pass

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Dodaj property ``position``, który zwraca tuple ``(x, y, z)``
    #. Usunięcie ``position`` ustawia wszystkie atrybuty na 0 (``x=0``, ``y=0``, ``z=0``)
    #. Zablokuj edycję atrybutów
    #. Wszystkie testy muszą przejść

:Input:
    .. code-block:: python

        class Point:
            """
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
            """
