.. _OOP Solid:

**********
S.O.L.I.D.
**********


Recap
=====
* Rigidity - mixing higher level with low level implementation
* Fragility - if you change something, some other thing will break
* Reusability
* Coupling - interdependencies a.k.a "spaghetti code"
* K.I.S.S.
* D.R.Y.
* OOP:

    * Encapsulation
    * Polymorphism
    * Inheritance


Rationale
=========
* SRP: The Single Responsibility Principle
* OCP: The Open / Closed Principle
* LSP: The Liskov Substitution Principle
* ISP: The Interface Segregation Principle
* DIP: The Dependency Inversion Principle

.. figure:: img/oop-solid.png
    :scale: 40%
    :align: center

    S.O.L.I.D. Principles


Single Responsibility Principle
===============================
.. epigraph::

    A class should have one, and only one, reason to change.

    -- Robert C. Martin

Every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility.

.. figure:: img/oop-solid-srp.png
    :scale: 40%
    :align: center

    S.O.L.I.D. - Single Responsibility Principle

.. code-block:: python
    :caption: Bad

    from dataclasses import dataclass


    @dataclass
    class Hero:
        HEALTH_MIN: int = 10
        HEALTH_MAX: int = 20
        _health: int = 0
        _position_x: int = 0
        _position_y: int = 0

        def __post_init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

        def is_alive(self) -> bool:
            return self._health > 0

        def is_dead(self) -> bool:
            return self._health <= 0

        def position_set(self, x: int, y: int) -> None:
            self._position_x = x
            self._position_y = y

        def position_change(self, right=0, left=0, down=0, up=0):
            x = self._position_x + right - left
            y = self._position_y + down - up
            self.position_set(x, y)

        def position_get(self) -> tuple[int, int]:
            return self._position_x, self._position_y


.. code-block:: python
    :caption: Good

    from dataclasses import dataclass


    @dataclass
    class HasHealth:
        HEALTH_MIN: int = 10
        HEALTH_MAX: int = 20
        _health: int = 0

        def __post_init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

        def is_alive(self) -> bool:
            return self._health > 0

        def is_dead(self) -> bool:
            return self._health <= 0


    @dataclass
    class HasPosition:
        _position_x: int = 0
        _position_y: int = 0

        def position_set(self, x: int, y: int) -> None:
            self._position_x = x
            self._position_y = y

        def position_change(self, right=0, left=0, down=0, up=0):
            x = self._position_x + right - left
            y = self._position_y + down - up
            self.position_set(x, y)

        def position_get(self) -> tuple[int, int]:
            return self._position_x, self._position_y


    class Hero(HasHealth, HasPosition):
        pass


Open/Closed Principle
=====================
.. epigraph::

    Modules [classes] should be open for extension, but closed for modification.

    -- Bertrand Mayer

.. figure:: img/oop-solid-ocp.png
    :scale: 40%
    :align: center

    S.O.L.I.D. - Open/Closed Principle

.. code-block:: python

    from random import randint


    class Critter:
        HEALTH_MIN: int = 0
        HEALTH_MAX: int = 10

        def __init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)


    class Skeleton(Critter):
        HEALTH_MIN: int = 10
        HEALTH_MAX: int = 20


    class Troll(Hero):
        HEALTH_MIN: int = 100
        HEALTH_MAX: int = 200


    class Dragon(Critter):
        HEALTH_MIN: int = 1000
        HEALTH_MAX: int = 2000

.. code-block:: python

    from random import randint


    class Critter:
        HEALTH_MIN: int
        HEALTH_MAX: int

        def __init__(self):
            self._health = self._get_initial_health()

        def _get_initial_health(self):
            return randint(self.HEALTH_MIN, self.HEALTH_MAX)


    class Regular(Critter):
        pass


    class Elite(Critter):
        def _get_initial_health(self):
            hp = super()._get_initial_health()
            return hp * 2


    class Boss(Critter):
        def _get_initial_health(self):
            hp = super()._get_initial_health()
            return hp * 10


Liskov Substitution Principle
=============================
.. epigraph::

    Derived classes must be usable through the base class interface, without the need for the user to know the difference.

    -- Barbara Liskov

* Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program

.. figure:: img/oop-solid-lsp.png
    :scale: 40%
    :align: center

    S.O.L.I.D. - Liskov Substitution Principle

.. code-block:: python

    class mystr(str):
        pass


    a = str('Mark Watney')
    a.upper()
    # MARK WATNEY

    b = mystr('Mark Watney')
    b.upper()
    # MARK WATNEY


Interface Segregation Principle
===============================
* many specific interfaces are better than one general-purpose interface

The interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. ISP is one of the five SOLID principles of object-oriented design, similar to the High Cohesion Principle of GRASP.

.. figure:: img/oop-solid-isp.png
    :scale: 40%
    :align: center

    S.O.L.I.D. Principles - Interface Segregation Principle

.. code-block:: python
    :caption: Bad

    class Mixin:
        def json_loads(self):
            raise NotImplementedError

        def json_dumps(self):
            raise NotImplementedError

        def pickle_loads(self):
            raise NotImplementedError

        def pickle_dumps(self):
            raise NotImplementedError

        def csv_loads(self):
            raise NotImplementedError

        def csv_dumps(self):
            raise NotImplementedError


    class User(Mixin):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


.. code-block:: python
    :caption: Good

    class JSONMixin:
        def json_loads(self):
            raise NotImplementedError

        def json_dumps(self):
            raise NotImplementedError


    class PickleMixin:
        def pickle_loads(self):
            raise NotImplementedError

        def pickle_dumps(self):
            raise NotImplementedError


    class CSVMixin:
        def csv_loads(self):
            raise NotImplementedError

        def csv_dumps(self):
            raise NotImplementedError


    class User(JSONMixin, PickleMixin, CSVMixin):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


Dependency Inversion Principle
==============================
.. epigraph::

    Clients should not be forced to depend on methods that they do not use.
    Program to an interface, not an implementation.

    -- Robert C. Martin

* https://medium.com/swlh/isp-the-interface-segregation-principle-a3416f3ac8f5
* one should depend upon abstractions, not concretions
* decoupling software modules

.. figure:: img/oop-solid-dip.png
    :scale: 40%
    :align: center

    S.O.L.I.D. - Dependency Inversion Principle

.. figure:: img/oop-solid-deps.png
    :scale: 40%
    :align: center

    Class Dependencies should depend upon abstractions, not concretions

When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

    #. High-level modules should not depend on low-level modules. Both should depend on abstractions.
    #. Abstractions should not depend on details. Details should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction this design principle inverts the way some people may think about object-oriented programming.

.. code-block:: python
    :caption: Bad

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
    :caption: Good

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

