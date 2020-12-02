"""
* Assignment: OOP Constructor Syntax
* Filename: oop_constructor_syntax.py
* Complexity: easy
* Lines of code: 6 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Point` with methods:
        a. `__new__()` returning new `Point` class instances
        b. `__init__()` taking `x` and `y` and stores them as attributes
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Point` z metodami:
        a. `__new__()` zwraca nową instancję klasy `Point`
        b. `__init__()` przyjmuje `x` i `y` i zapisuje je jako atrybuty
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Point)
    >>> assert hasattr(Point, '__new__')
    >>> assert hasattr(Point, '__init__')
    >>> pt = Point.__new__(Point)
    >>> assert type(pt) is Point
    >>> pt.__init__(1, 2)
    >>> assert pt.x == 1
    >>> assert pt.y == 2
"""

# Solution
class Point:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, x, y):
        self.x = x
        self.y = y
