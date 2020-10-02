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

    class Lamp:
        status = 'off'


    lamp = Ligt()
    lamp.status = 'on'
    lamp.status = 'off'

.. code-block:: python
    :caption: Tell - don't ask (Good)

    class Ligt:
        status = 'off'

        def turn_on(self):
            self.status = 'on'

        def turn_off(self):
            self.status = 'off'


    light = Ligt()
    light.turn_on()
    light.turn_off()

.. code-block:: python
    :caption: Tell - don't ask (Bad)

    class Dragon:
        self.status = 'alive'


    dragon = Dragon()
    while dragon.status == 'alive':
        ...

.. code-block:: python
    :caption: Tell - don't ask (Good)

    class Dragon:
        self.status = 'alive'

        def is_alive():
            return True

    dragon = Dragon()

    while dragon.is_alive():
        ...


Objects and instances
=====================
.. code-block:: python

    text = str('Jan,Twardowski')
    text.split(',')
    # ['Jan', 'Twardowski']

    text = str('Jan,Twardowski')
    str.split(text, ',')
    # ['Jan', 'Twardowski']

.. code-block:: python

    'Jan,Twardowski'.split(',')
    # ['Jan', 'Twardowski']

    str.split('Jan,Twardowski', ',')
    # ['Jan', 'Twardowski']


.. _OOP SOLID:

S.O.L.I.D.
==========

Single responsibility principle
-------------------------------
a class should have only a single responsibility (i.e. changes to only one part of the software's specification should be able to affect the specification of the class)

The single responsibility principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, "A class should have only one reason to change."

.. code-block:: python

    class Position:
        x: int
        y: int

        def __init__(self, x=0, y=0):
            self.set(x,y)

        def set(self, x, y):
            self.x = x
            self.y = y

        def change(self, right=0, left=0, down=0, up=0):
            x = self.x + right - left
            x = self.y + down - up
            self.set(x, y)

        def get(self):
            return self._position

.. code-block:: python

    @dataclass
    class Destructable:
        _current_health: int = 0
        _status: Status = Status.ALIVE

        class IsDead(Exception):
            pass

        def __post_init__(self) -> None:
            self._current_health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

        def _update_status(self) -> None:
            if self._current_health > 0:
                self._status = Status.ALIVE
            else:
                self._status = Status.DEAD

        def is_dead(self) -> bool:
            if self._status == Status.DEAD:
                return True
            else:
                return False

        def is_alive(self) -> bool:
            return not self.is_dead()


Open/closed principle
---------------------
software entities ... should be open for extension, but closed for modification

The name open/closed principle has been used in two ways.
Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different.

.. code-block:: python

    class Dragon:
        def __init__(self):
            self.health = self._get_initial_health()


    class DragonLevel1(Dragon):
        def _get_initial_health(self):
            return 10

    class DragonLevel2(Dragon):
        def _get_initial_health(self):
            return 20


    lvl1 = DragonLevel1()
    lvl2 = DragonLevel2()

    print(lvl1.health)
    print(lvl2.health)

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

Dependency inversion principle
------------------------------
one should depend upon abstractions, [not] concretions

In object-oriented design, the dependency inversion principle refers to a specific form of decoupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

    #. High-level modules should not depend on low-level modules. Both should depend on abstractions.
    #. Abstractions should not depend on details. Details should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction this design principle inverts the way some people may think about object-oriented programming.

.. code-block:: python
    :caption: Switch moves business logic to the execution place

    watney = 'Astronaut'

    if watney == 'Astronaut':
        print('Hello')
    elif watney == 'Cosmonaut':
        print('Привет!')
    elif watney == 'Taikonaut':
        print('你好')
    else:
        print('Default Value')

.. code-block:: python

    class Astronaut:
        def say_hello():
            print('Hello')

    class Cosmonaut:
        def say_hello():
            print('Привет!')

    class Taikonaut:
        def say_hello():
            print('你好')

    watney = Astronaut()
    watney.say_hello()


GRASP
=====
**General responsibility assignment software patterns (or principles)**, abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.

The different patterns and principles used in GRASP are controller, creator, indirection, information expert, high cohesion, low coupling, polymorphism, protected variations, and pure fabrication. All these patterns answer some software problem, and these problems are common to almost every software development project. These techniques have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.


Assignments
===========
.. todo:: Create assignments
