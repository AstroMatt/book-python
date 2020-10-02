.. _OOP Solid:

**********
S.O.L.I.D.
**********


Single responsibility principle
===============================
* Class should have only a single responsibility
* A class should have only one reason to change. -- Robert C. Martin

The single responsibility principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility.

.. code-block:: python
    :caption: Bad

    from dataclasses import dataclass


    @dataclass
    class Dragon:
        HEALTH_MIN: int = 0
        HEALTH_MAX: int = 10
        _positinion_x: int = 0
        _positinion_y: int = 0
        _health: int = 0

        def __post_init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

        def is_dead(self) -> bool:
            if self._health <= 0:
                return True
            else:
                return False

        def is_alive(self) -> bool:
            return not self.is_dead()

        def position_set(self, x: int, y: int) -> None:
            self._positinion_x = x
            self._positinion_y = y

        def position_change(self, right=0, left=0, down=0, up=0):
            x = self._positinion_x + right - left
            y = self._positinion_y + down - up
            self.set(x, y)

        def position_get(self) -> tuple[int, int]:
            return self._positinion_x, self._positinion_y


.. code-block:: python
    :caption: Good

    from dataclasses import dataclass


    @dataclass
    class HasHealth:
        HEALTH_MIN: int = 0
        HEALTH_MAX: int = 10
        _health: int = 0

        def __post_init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

        def is_dead(self) -> bool:
            if self._health <= 0:
                return True
            else:
                return False

        def is_alive(self) -> bool:
            return not self.is_dead()


    @dataclass
    class HasPosition:
        _positinion_x: int = 0
        _positinion_y: int = 0

        def position_set(self, x: int, y: int) -> None:
            self._positinion_x = x
            self._positinion_y = y

        def position_change(self, right=0, left=0, down=0, up=0):
            x = self._positinion_x + right - left
            y = self._positinion_y + down - up
            self.set(x, y)

        def position_get(self) -> tuple[int, int]:
            return self._positinion_x, self._positinion_y


        class Dragon(HasHealth, HasPosition):
            pass


Open/Closed Principle
=====================
* Class should be open for extension, but closed for modification

.. code-block:: python

    class Dragon:
        HEALTH_MIN: int = 0
        HEALTH_MAX: int = 10

        def __init__(self) -> None:
            self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)


    class RedDragon(Dragon):
        HEALTH_MIN: int = 10
        HEALTH_MAX: int = 20


    class BlackDragon(Dragon):
        HEALTH_MIN: int = 30
        HEALTH_MAX: int = 40

.. code-block:: python

    from random import randint


    class Dragon:
        def __init__(self):
            self._health = self._get_initial_health()

        def _get_initial_health(self):
            return randint(10, 20)


    class RedDragon(Dragon):
        def _get_initial_health(self):
            return randint(30, 40)


    class BlackDragon(Dragon):
        def _get_initial_health(self):
            return randint(20, 30)


Liskov substitution principle
=============================
* Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program

.. code-block:: python

    class mystr(str):
        pass

    a = str('Mark Watney')
    a.upper()
    # MARK WATNEY

    b = mystr('Mark Watney')
    b.upper()
    # MARK WATNEY


Interface segregation principle
===============================
* many specific interfaces are better than one general-purpose interface

The interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. ISP is one of the five SOLID principles of object-oriented design, similar to the High Cohesion Principle of GRASP.

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


Dependency inversion principle
==============================
* one should depend upon abstractions, [not] concretions
* decoupling software modules

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

