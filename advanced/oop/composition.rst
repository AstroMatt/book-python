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

    class Car:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class Truck:
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

.. literalinclude:: assignments/oop_composition_syntax.py
    :caption: :download:`Solution <assignments/oop_composition_syntax.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_composition_decompose.py
    :caption: :download:`Solution <assignments/oop_composition_decompose.py>`
    :end-before: # Solution
