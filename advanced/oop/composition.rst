***************************
Inheritance vs. Composition
***************************


* Mixin Classes
* Composition over Inheritance


Problem with inheritance
========================
.. code-block:: python
    :caption: Inheritance pattern

    class Vehicle:
        def run(self):
            pass

        def drive(self):
            pass

        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle):
        pass


    class Truck(Vehicle):
        pass


.. code-block:: python
    :caption: Problem with inheritance

     class Vehicle:
         def run(self):
             pass

         def drive(self):
             pass

         def window_open(self):
             pass

         def window_close(self):
             pass


     class Car(Vehicle):
         pass


     class Truck(Vehicle):
         pass


     class Motorbike(Vehicle):
         """Motorbike is a vehicle, but doesn't have windows."""

         def window_open(self):
             raise NotImplementedError

         def window_close(self):
             raise NotImplementedError

.. code-block:: python

    class Vehicle:
        def run(self):
            pass

        def drive(self):
            pass


    class HasWindows:
        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle, HasWindows):
        pass

    class Truck(Vehicle, HasWindows):
        pass

    class Motorbike(Vehicle):
        pass


Multi level inheritance problem
===============================
.. code-block:: python
    :caption: Multi level inheritance is a bad pattern here

    class ToJSON:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class ToPickle(ToJSON):
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class User(ToPickle):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    user = User(
        firstname='Jan',
        lastname='Twardowski',
        address='Copernicus Crater, Moon'
    )

    print(user.to_json())
    # {"firstname": "Jan", "lastname": "Twardowski", "address": "Copernicus Crater, Moon"}

    print(user.to_pickle())
    # b'\x80\x03c__main__\nUser\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06X\x07\x00\x00\x00addressq\x07X\x17\x00\x00\x00Copernicus Crater, Moonq\x08ub.'


Composition using Mixin classes
===============================
.. code-block:: python
    :caption: Mixin classes - multiple inheritance.

    class JSONMixin:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class PickleMixin:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class User(JSONMixin, PickleMixin):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    user = User(
        firstname='Jan',
        lastname='Twardowski',
        address='Copernicus Crater, Moon'
    )

    print(user.to_json())
    # {"firstname": "Jan", "lastname": "Twardowski", "address": "Copernicus Crater, Moon"}

    print(user.to_pickle())
    # b'\x80\x03c__main__\nUser\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06X\x07\x00\x00\x00addressq\x07X\x17\x00\x00\x00Copernicus Crater, Moonq\x08ub.'


Assignments
===========

OOP Composition Mars
--------------------
* Assignment name: OOP Composition Mars
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_composition_mars.py`

:English:
    #. Create class ``Habitat``
    #. Create class ``Rocket``
    #. Create class ``Astronaut``
    #. Compose class ``MarsMission`` from ``Habitat``, ``Rocket``, ``Astronaut``

:Polish:
    #. Stwórz klasę ``Habitat``
    #. Stwórz klasę ``Rocket``
    #. Stwórz klasę ``Astronaut``
    #. Skomponuj klasę ``MarsMission`` z ``Habitat``, ``Rocket``, ``Astronaut``

OOP Composition Moveable
------------------------
* Assignment name: OOP Composition Moveable
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_composition_moveable.py`

:English:
    .. todo:: English Translation

:Polish:
    #. Stwórz niemutowalną klasę ``Point``
    #. Klasa ``Point`` ma ``x: int`` oraz ``y: int``
    #. Gdy ``x`` lub ``y`` są ujemne (podnieś ``ValueError``)
    #. Stwórz klasę ``Movable``
    #. W klasie ``Movable`` zdefiniuj metodę ``get_position() -> Point``
    #. W klasie ``Movable`` zdefiniuj metodę ``set_position(x: int, y: int) -> NoReturn``
    #. W klasie ``Movable`` zdefiniuj metodę ``change_position(left: int = 0, right: int = 0, up: int = 0, down: int = 0)``
    #. Przyjmij górny lewy róg ekranu za punkt początkowy:

        * idąc w prawo dodajesz ``x``
        * idąc w lewo odejmujesz ``x``
        * idąc w górę odejmujesz ``y``
        * idąc w dół dodajesz ``y``

    #. Testy muszą przechodzić

:Tests:
    .. code-block:: python

        """
        >>> class Astronaut(Moveable):
        ...     pass

        >>> astro = Astronaut()
        >>> astro.get_position()
        Point(x=0, y=0)

        >>> astro.change_position(right=10)
        >>> astro.get_position()
        Point(x=10, y=0)

        >>> astro.change_position(left=5)
        >>> astro.get_position()
        Point(x=5, y=0)

        >>> astro.change_position(down=10)
        >>> astro.get_position()
        Point(x=5, y=10)

        >>> astro.change_position(up=5)
        >>> astro.get_position()
        Point(x=5, y=5)

        >>> astro.set_position(x=0, y=0)
        >>> astro.get_position()
        Point(x=0, y=0)
        """

:Hints:
    * ``@dataclass(frozen=True)``
