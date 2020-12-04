"""
* Assignment: Protocol Reflection Frozen
* Filename: protocol_reflection_frozen.py
* Complexity: easy
* Lines of code: 6 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Point` with `x`, `y`, `z` attributes
    3. Prevent creation of new attributes
    4. Allow to define `x`, `y`, `z` but only at the initialization
    5. Prevent later modification of `x`, `y`, `z`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zablokuj tworzenie nowych atrybutów
    4. Pozwól na zdefiniowanie `x`, `y`, `z` ale tylko przy inicjalizacji
    5. Zablokuj późniejsze modyfikacje `x`, `y`, `z`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)

    >>> pt.notexisting = 10
    Traceback (most recent call last):
    PermissionError: Cannot set other attributes than x,y,z

    >>> pt.x = 10
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes

    >>> pt.y = 20
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes

    >>> pt.z = 30
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes
"""


# Given
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Solution
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x,y,z')
        if hasattr(self, name):
            raise PermissionError('Cannot modify existing attributes')
        return super().__setattr__(name, value)
