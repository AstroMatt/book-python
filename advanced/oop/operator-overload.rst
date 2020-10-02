.. _OOP Operator Overload:

*****************
Operator Overload
*****************


Rationale
=========
.. highlights::
    * Readable syntax
    * Simpler operations
    * Follong examples uses ``dataclasses`` to focus on action code, not boilerplate

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Vector:
        x: int = 0
        y: int = 0


    Vector(x=1, y=2) + Vector(x=3, y=4)
    # Traceback (most recent call last):
    #   ...
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

    Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
    # Traceback (most recent call last):
    #   ...
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
    "``obj % other``",     "``obj.__mod__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"

.. code-block:: python
    :caption: ``%`` (``__mod__``) operator behavior for ``int`` and ``str``

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

.. note:: ``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting. More information in :ref:`Builtin Printing`.


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

    class Digit:
        def __init__(self, initial_value):
            self.value = initial_value

        def __str__(self):
            return str(self.value)

        def __xor__(self, other):
            return Digit(self.value ** other.value)


    a = Digit(2)
    b = Digit(4)

    a ^ b
    # 16


Builtin Functions and Keywords
==============================
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(obj)``",             "``obj.__abs__()``"
    "``bool(obj)``",            "``obj.__bool__()``"
    "``complex(obj)``",         "``obj.__complex__()``"
    "``del obj``",              "``obj.__del__()``"
    "``delattr(obj, name)``",   "``obj.__delattr__(name)``"
    "``dir(obj)``",             "``obj.__dir__()``"
    "``divmod(obj, other)``",   "``obj.__divmod__(other)``"
    "``float(obj)``",           "``obj.__float__()``"
    "``hash(obj)``",            "``obj.__hash__()``"
    "``hex(obj)``",             "``obj.__hex__()``"
    "``int(obj)``",             "``obj.__int__()``"
    "``iter(obj)``",            "``obj.__iter__()``"
    "``len(obj)``",             "``obj.__len__()``"
    "``next(obj)``",            "``obj.__next__()``"
    "``oct(obj)``",             "``obj.__oct__()``"
    "``pow(obj)``",             "``obj.__pow__()``"
    "``reversed(obj)``",        "``obj.__reversed__()``"
    "``round(obj, ndigits)``",  "``obj.__round__(ndigits)``"

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

.. code-block:: python
    :caption: Contains in ``numpy``

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6]])

    data[1][2]  # 6
    data[1,2]   # 6

.. code-block:: python
    :caption: Intuitive implementation of numpy ``array[row,col]`` accessor

    class array(list):
        def __getitem__(key):
            if isinstance(key, int):
                return super().__getitem__(key)

            if isinstance(key, tuple):
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

    data[:, 2]
    # data.__getitem__((:, 1))

.. code-block:: python

    class Cache(dict):
        def __missing__(self, key):
            ...

Use Case
========
.. code-block:: python

    dragon @ Position(x=50, y=120)
    dragon >> Position(x=50, y=120)

.. code-block:: python

    dragon < Damage(20)
    dragon > Damage(20)

.. code-block:: python

    hero["gold"] += dragon["gold"]


Further Reading
===============
* :ref:`Operator Library`
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types


Assignments
===========

OOP Operator Overload
---------------------
* Assignment name: OOP Operator Overload
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_operator_overload.py`

:English:
    #. Use code from "Input" section (see below)
    #. Override operators of ``Astronaut`` and ``Mission`` for code to work correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Nadpisz operatory ``Astronaut`` i ``Mission`` aby poniższy kod zadziałał poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        class Astronaut:
            def __init__(self, name, experience=()):
                self.name = name
                self.experience = list(experience)

            def __str__(self):
                return f'{self.name}, {self.experience}'

            def __iadd__(self, other):
                raise NotImplementedError

            def __contains__(self, flight):
                raise NotImplementedError


        class Mission:
            def __init__(self, year, name):
                self.year = year
                self.name = name

            def __repr__(self):
                return f'\n\t{self.year}: {self.name}'

            def __eq__(self, other):
                raise NotImplementedError

:Output:
    .. code-block:: text

        >>> astro = Astronaut('Jan Twardowski', missions=[
        ...     Mission(1969, 'Apollo 11'),
        ... ])
        >>> astro += Mission(2024, 'Artemis 3')
        >>> astro += Mission(2035, 'Ares 3')

        >>> print(astro)  # doctest: +NORMALIZE_WHITESPACE
        Jan Twardowski, [
            1969: Apollo 11,
            2024: Artemis 3,
            2035: Ares 3]

        >>> if Mission(2024, 'Artemis 3') in astro:
        ...    print(True)
        ... else:
        ...   print(False)
        True
