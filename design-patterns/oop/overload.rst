.. _OOP Overload:

********
Overload
********


Rationale
=========
.. highlights::
    * Operator Overload
    * Readable syntax
    * Simpler operations
    * Following examples uses ``dataclasses`` to focus on action code, not boilerplate

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Vector:
        x: int = 0
        y: int = 0


    Vector(x=1, y=2) + Vector(x=3, y=4)
    # Traceback (most recent call last):
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

    Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
    # Traceback (most recent call last):
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Vector:
        x: int = 0
        y: int = 0

        def __add__(self, other):
            return Vector(
                self.x + other.x,
                self.y + other.y)


    Vector(x=1, y=2) + Vector(x=3, y=4)
    # Vector(x=4, y=6)

    Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
    # Vector(x=9, y=12)


Numerical Operators
===================
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj += other``",    "``obj.__iadd__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj -= other``",    "``obj.__isub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj *= other``",    "``obj.__imul__(other)``"
    "``obj / other``",     "``obj.__div__(other)``"
    "``obj /= other``",    "``obj.__idiv__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"

``%`` (``__mod__``) operator behavior for ``int`` and ``str``:

.. code-block:: python

    3 % 2                         # 1
    4 % 2                         # 0

    'Echo' % 2                    # TypeError: not all arguments converted during string formatting
    'Echo %s' % 2                 # 'Echo 2'
    'Echo %d' % 2                 # 'Echo 2'
    'Echo %f' % 2                 # 'Echo 2.0'
    'Echo %s %s' % (1, 2)         # 'Echo 1 2'
    'Echo %s %d %f' % (1, 2, 3)   # 'Echo 1 2 3.000000'

    'Echo %(firstname)s %(lastname)s' % {'firstname': 'Mark', 'lastname': 'Watney'}
    # 'Echo Mark Watney'

    'Echo %(name)s %(age)d' % {'name': 'Mark Watney', 'age': 44}
    # 'Echo Mark Watney 44'

``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting. More information in :ref:`Builtin Printing`.


Comparison Operators
====================
.. csv-table:: Comparison Operators Overload
    :header: "Operator", "Method"

    "``obj == other``",   "``obj.__eq__(other)``"
    "``obj != other``",   "``obj.__ne__(other)``"
    "``obj < other``",    "``obj.__lt__(other)``"
    "``obj <= other``",   "``obj.__le__(other)``"
    "``obj > other``",    "``obj.__gt__(other)``"
    "``obj >= other``",   "``obj.__ge__(other)``"

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Vector:
        x: int = 0
        y: int = 0

        def __eq__(self, other):
            if (self.x == other.x) and (self.y == other.y):
                return True
            else:
                return False

    Vector(x=1, y=2) == Vector(x=3, y=4)
    # False

    Vector(x=1, y=2) == Vector(x=1, y=2)
    # True


Boolean Operators
=================
.. csv-table:: Boolean Operators Overload
    :header: "Operator", "Method"

    "``-obj``",           "``obj.__neg__()``"
    "``+obj``",           "``obj.__pos__()``"
    "``~obj``",           "``obj.__invert__()``"
    "``obj & other``",    "``obj.__and__(other)``"
    "``obj | other``",    "``obj.__or__(other)``"
    "``obj ^ other``",    "``obj.__xor__(other)``"
    "``obj << other``",   "``obj.__lshift__(other)``"
    "``obj >> other``",   "``obj.__rshift__(other)``"

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Digit:
        value: int

        def __xor__(self, other):
            return Digit(self.value ** other.value)


    a = Digit(2)
    b = Digit(4)

    a ^ b
    # Digit(value=16)


Builtin Functions and Keywords
==============================
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(obj)``",                      "``obj.__abs__()``"
    "``bool(obj)``",                     "``obj.__bool__()``"
    "``complex(obj)``",                  "``obj.__complex__()``"
    "``del obj``",                       "``obj.__del__()``"
    "``delattr(obj, name)``",            "``obj.__delattr__(name)``"
    "``dir(obj)``",                      "``obj.__dir__()``"
    "``divmod(obj, other)``",            "``obj.__divmod__(other)``"
    "``float(obj)``",                    "``obj.__float__()``"
    "``getattr(obj, name, default)``",   "``obj.__getattr__(name, default)``"
    "``hash(obj)``",                     "``obj.__hash__()``"
    "``hex(obj)``",                      "``obj.__hex__()``"
    "``int(obj)``",                      "``obj.__int__()``"
    "``iter(obj)``",                     "``obj.__iter__()``"
    "``len(obj)``",                      "``obj.__len__()``"
    "``next(obj)``",                     "``obj.__next__()``"
    "``oct(obj)``",                      "``obj.__oct__()``"
    "``pow(obj)``",                      "``obj.__pow__()``"
    "``reversed(obj)``",                 "``obj.__reversed__()``"
    "``round(obj, ndigits)``",           "``obj.__round__(ndigits)``"
    "``setattr(obj, name)``",            "``obj.__setattr__(name)``"

.. code-block:: python

    from math import sqrt
    from dataclasses import dataclass

    @dataclass
    class Vector:
        x: int = 0
        y: int = 0

        def __abs__(self):
            return sqrt(self.x**2 + self.y**2)


    abs(Vector(x=3, y=4))
    # 5.0

.. code-block:: python

    class Astronaut:
        def __float__(self) -> float:
            return 1961.0

        def __int__(self) -> int:
            return 1969

        def __len__(self) -> int:
            return 170

        def __str__(self) -> str:
            return 'My name... José Jiménez'

        def __repr__(self) -> str:
            return f'Astronaut()'

    astro = Astronaut()

    float(astro)
    # 1961.0

    int(astro)
    # 1969

    len(astro)
    # 170

    repr(astro)
    # Astronaut()

    str(astro)
    # 'My name... José Jiménez'

    print(astro)
    # My name... José Jiménez


Accessors Overload
==================
.. csv-table:: Operator Overload
    :header: "Operator", "Method", "Remarks"
    :widths: 15, 45, 40

    "``obj(x)``",      "``obj.__call__(x)``"
    "``obj[x]``",      "``obj.__getitem__(x)``"
    "``obj[x]``",      "``obj.__missing__(x)``", "(when ``x`` is not in ``obj``)"
    "``obj[x] = 10``", "``obj.__setitem__(x, 10)``"
    "``del obj[x]``",  "``obj.__delitem__(x)``"
    "``x in obj``",    "``obj.__contains__(x)``"

.. code-block:: python

    data = dict()

    data['a'] = 10
    # data.__setitem__('a', 10) -> None

    data['a']
    # data.__getitem__('a') -> 10

    data['x']
    # data.__getitem__('x') -> data.__missing__() -> KeyError: 'x'

    data()
    # data.__call__() -> TypeError: 'dict' object is not callable

Contains in ``numpy``:

.. code-block:: python

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6]])

    data[1][2]
    # 6

    data[1,2]
    # 6

    data[1:2]
    # array([[2,3],
    #        [5,6]])

    data[1:2, 0]
    # array([2,3])

    data[1:2, 1:]
    # array([[5,6]])

Intuitive implementation of numpy ``array[row,col]`` accessor:

.. code-block:: python

    class array(list):
        def __getitem__(key):
            if isinstance(key, int):
                return super().__getitem__(key)

            if isinstance(key, tuple):
                row = key[0]
                col = key[1]
                return super().__getitem__(row).__getitem__(col)

            if isinstance(key, slice):
                start = key[0] if key[0] else 0
                stop = key[1] if key[0] else len(self)
                step = key[2] if key[2] else 1
                return ...


    data[1]
    # data.__getitem__(1)

    data[1,2]
    # data.__getitem__((1,2))

    data[1:2]
    # data.__getitem__(1:2)
    # data.__getitem__(slice(1,2))

    data[:, 2]
    # data.__getitem__((:, 2))
    # data.__getitem__((slice(), 2))


Eq Works at Both Sides
======================
.. code-block::

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    class Cosmonaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    a = Astronaut('Mark', 'Watney')
    c = Cosmonaut('Mark', 'Watney')

    print(a == c)
    # False

.. code-block::

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __eq__(self, other):
            return (self.firstname == other.firstname
                    and self.lastname == other.lastname)


    class Cosmonaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    a = Astronaut('Mark', 'Watney')
    c = Cosmonaut('Mark', 'Watney')

    print(a == c)
    # True

.. code-block::

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    class Cosmonaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __eq__(self, other):
            return (self.firstname == other.firstname
                    and self.lastname == other.lastname)


    a = Astronaut('Mark', 'Watney')
    c = Cosmonaut('Mark', 'Watney')

    print(a == c)
    # True


Use Case
========
.. code-block:: python

    hero @ Position(x=50, y=120)
    hero >> Direction(left=10, up=20)

.. code-block:: python

    hero < Damage(20)
    hero > Damage(20)

.. code-block:: python

    hero["gold"] += dragon["gold"]

.. code-block:: python

    class Cache(dict):
        def __init__(self, func):s
            self._func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self._func(*key)
            return self[key]


    @Cache
    def myfunction(a, b):
        return a * b


    myfunction(2, 4)           # 8         # Computed
    myfunction('hi', 3)        # 'hihihi'  # Computed
    myfunction('ha', 3)        # 'hahaha'  # Computed

    myfunction('ha', 3)        # 'hahaha'  # Fetched from cache
    myfunction('hi', 3)        # 'hihihi'  # Fetched from cache
    myfunction(2, 4)           # 8         # Fetched from cache
    myfunction(4, 2)           # 8         # Computed

    myfunction
    # {
    #   (2, 4): 8,
    #   ('hi ', 3): 'hihihi',
    #   ('ha', 3): 'hahaha',
    #   (4, 2): 8,
    # }


Further Reading
===============
* :ref:`Operator Library`
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types


Assignments
===========

.. literalinclude:: ../_assignments/oop_overload_easy1.py
    :caption: :download:`Solution <../_assignments/oop_overload_easy1.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_overload_easy2.py
    :caption: :download:`Solution <../_assignments/oop_overload_easy2.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_overload_medium1.py
    :caption: :download:`Solution <../_assignments/oop_overload_medium1.py>`
    :end-before: # Solution
