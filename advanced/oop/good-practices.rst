**************************
Good Engineering Practises
**************************


Tell - don't ask
================
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

.. code-block:: python
    :caption: Tell - don't ask (Bad)

    class Rocket:
        status = 'off'


    soyuz = Rocket()
    soyuz.status = 'on'

.. code-block:: python
    :caption: Tell - don't ask (Good)

    class Rocket:
        status = 'off'

        def ignite(self):
            self.status = 'on'


    soyuz = Rocket()
    soyuz.ignite()


.. code-block:: python

    class Dragon:
        def __init__(self):
            self.status = 'dead'


    wawelski = Dragon()


    while wawelski.status != 'dead':
        ...


Objects and instances
=====================
.. code-block:: python
    :caption: Implicit passing instance to class as ``self``.

    text = 'Jan,Twardowski'

    text.split(',')                     # ['Jan', 'Twardowski']

.. code-block:: python
    :caption: Explicit passing instance to class overriding ``self``.

    text = 'Jan,Twardowski'

    str.split(text, ',')                # ['Jan', 'Twardowski']

.. code-block:: python
    :caption: Passing anonymous objects as instances.

    'Jan,Twardowski'.split(',')         # ['Jan', 'Twardowski']
    str.split('Jan,Twardowski', ',')    # ['Jan', 'Twardowski']


.. _OOP SOLID:

S.O.L.I.D.
==========

Single responsibility principle
-------------------------------
a class should have only a single responsibility (i.e. changes to only one part of the software's specification should be able to affect the specification of the class)

The single responsibility principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, "A class should have only one reason to change."

Open/closed principle
---------------------
software entities ... should be open for extension, but closed for modification

The name open/closed principle has been used in two ways.
Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different.

.. code-block:: python

    class DragonLevel1:
        def _initial_health(self):
            return 10

        def __init__(self):
            self.current_health = self._get_initial_health()


    class DragonLevel2(Dragon):
        def _initial_health(self):
            return 20


    lvl1 = DragonLevel1()
    lvl2 = DragonLevel2()

    print(lvl1.current_health)
    print(lvl2.current_health)

Liskov substitution principle
-----------------------------
objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. See also design by contract.

Substitutability is a principle in object-oriented programming stating that, in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e. an object of type T may be substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.).

.. code-block:: python
    :emphasize-lines: 23

    class CacheInterface:
        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    class CacheDatabase(CacheInterface):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    db: CacheInterface = CacheDatabase()
    db.set('name', 'Jan Twardowski')
    db.is_valid('name')
    db.get('name')

Interface segregation principle
-------------------------------
many client-specific interfaces are better than one general-purpose interface

The interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. ISP is one of the five SOLID principles of object-oriented design, similar to the High Cohesion Principle of GRASP.

.. code-block:: python
    :caption: Mixin classes - multiple inheritance.

    class JSONSerializable:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class PickleSerializable:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class User(JSONSerializable, PickleSerializable):
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

Dependency inversion principle
------------------------------
one should depend upon abstractions, [not] concretions

In object-oriented design, the dependency inversion principle refers to a specific form of decoupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

    #. High-level modules should not depend on low-level modules. Both should depend on abstractions.
    #. Abstractions should not depend on details. Details should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction this design principle inverts the way some people may think about object-oriented programming.


GRASP
=====
**General responsibility assignment software patterns (or principles)**, abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.

The different patterns and principles used in GRASP are controller, creator, indirection, information expert, high cohesion, low coupling, polymorphism, protected variations, and pure fabrication. All these patterns answer some software problem, and these problems are common to almost every software development project. These techniques have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.


Assignments
===========
.. todo:: Create assignments
