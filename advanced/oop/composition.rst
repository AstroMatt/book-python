.. _OOP Composition:

***************************
Inheritance vs. Composition
***************************


Rationale
=========
* Composition over Inheritance


Code Duplication
================
.. code-block:: python

    class Car(Vehicle):
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class Truck(Vehicle):
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


Inheritance
===========
.. code-block:: python

    class Vehicle:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class Car(Vehicle):
        pass


    class Truck(Vehicle):
        pass


Inheritance Problem
===================
.. code-block:: python

    class Vehicle:
        def engine_start(self):
            pass

        def engine_stop(self):
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


Composition
===========
* Mixin Classes

.. code-block:: python

    class Vehicle:
        pass

    class HasEngine:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class HasWindows:
        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle, HasEngine, HasWindows):
        pass

    class Truck(Vehicle, HasEngine, HasWindows):
        pass

    class Motorbike(Vehicle, HasEngine):
        pass


Case Study
==========
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


    class Astronaut(ToPickle):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.to_json())
    # {"firstname": "Mark", "lastname": "Watney"}

    print(astro.to_pickle())
    # b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
    # b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
    # b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'

.. code-block:: python
    :caption: Mixin classes - multiple inheritance.

    class ToJSON:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class ToPickle:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class Astronaut(ToJSON, ToPickle):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.to_json())
    # {"firstname": "Mark", "lastname": "Watney"}

    print(astro.to_pickle())
    # b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
    # b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
    # b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'


Assignments
===========

OOP Composition Mars
--------------------
* Assignment name: OOP Composition Mars
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/oop_composition_mars.py`

:English:
    #. Create class ``Habitat``
    #. Create class ``Rocket``
    #. Create class ``Astronaut``
    #. Compose class ``MarsMission`` from ``Habitat``, ``Rocket``, ``Astronaut``
    #. Assignment demonstrates syntax, so do not add any attributes and methods
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Habitat``
    #. Stwórz klasę ``Rocket``
    #. Stwórz klasę ``Astronaut``
    #. Skomponuj klasę ``MarsMission`` z ``Habitat``, ``Rocket``, ``Astronaut``
    #. Zadanie demonstruje skłądnię, nie dodawaj żadnych atrybutów i metod
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isclass
        >>> assert isclass(Habitat)
        >>> assert isclass(Astronaut)
        >>> assert isclass(Rocket)
        >>> assert isclass(MarsMission)
        >>> assert issubclass(MarsMission, Habitat)
        >>> assert issubclass(MarsMission, Astronaut)
        >>> assert issubclass(MarsMission, Rocket)

OOP Composition Movable
------------------------
* Assignment name: OOP Composition Movable
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_composition_movable.py`

:English:
    #. Define class ``Point``
    #. Class ``Point`` has attributes ``x: int = 0`` and ``y: int = 0``
    #. When ``x`` or ``y`` has negative value raise en exception ``ValueError('Coordinate cannot be negative')``
    #. Define class ``Movable``
    #. In ``Movable`` define method ``get_position(self) -> Point``
    #. In ``Movable`` define method ``set_position(self, x: int, y: int) -> None``
    #. In ``Movable`` define method ``change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None``
    #. Assume left-top screen corner as a initial coordinates position:

        #. going right add to ``x``
        #. going left subtract from ``x``
        #. going up subtract from ``y``
        #. going down add to ``y``

    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj klasę ``Point``
    #. Klasa ``Point`` ma atrybuty ``x: int = 0`` oraz ``y: int = 0``
    #. Gdy ``x`` lub ``y`` mają wartość ujemną podnieś wyjątek ``ValueError('Coordinate cannot be negative')``
    #. Zdefiniuj klasę ``Movable``
    #. W ``Movable`` zdefiniuj metodę ``get_position(self) -> Point``
    #. W ``Movable`` zdefiniuj metodę ``set_position(self, x: int, y: int) -> None``
    #. W ``Movable`` zdefiniuj metodę ``change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None``
    #. Przyjmij górny lewy róg ekranu za punkt początkowy:

        * idąc w prawo dodajesz ``x``
        * idąc w lewo odejmujesz ``x``
        * idąc w górę odejmujesz ``y``
        * idąc w dół dodajesz ``y``

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isclass, ismethod
        >>> assert isclass(Point)
        >>> assert isclass(Movable)
        >>> assert hasattr(Point, 'x')
        >>> assert hasattr(Point, 'y')
        >>> assert hasattr(Movable, 'get_position')
        >>> assert hasattr(Movable, 'set_position')
        >>> assert hasattr(Movable, 'change_position')
        >>> assert ismethod(Movable().get_position)
        >>> assert ismethod(Movable().set_position)
        >>> assert ismethod(Movable().change_position)

        >>> class Astronaut(Movable):
        ...     pass

        >>> astro = Astronaut()

        >>> astro.set_position(x=1, y=2)
        >>> astro.get_position()
        Point(x=1, y=2)

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(right=1)
        >>> astro.get_position()
        Point(x=2, y=1)

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(left=1)
        >>> astro.get_position()
        Point(x=0, y=1)

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(down=1)
        >>> astro.get_position()
        Point(x=1, y=2)

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(up=1)
        >>> astro.get_position()
        Point(x=1, y=0)

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(left=2)
        Traceback (most recent call last):
            ...
        ValueError: Coordinate cannot be negative

        >>> astro.set_position(x=1, y=1)
        >>> astro.change_position(up=2)
        Traceback (most recent call last):
            ...
        ValueError: Coordinate cannot be negative
