"""
* Assignment: Protocol Reflection Frozen
* Filename: protocol_reflection_frozen.py
* Complexity: easy
* Lines of code to write: 11 lines
* Estimated time: 13 min

English:
    1. Create class `Point` with `x`, `y`, `z` attributes
    2. Prevent creation of new attributes
    3. Allow to define `x`, `y`, `z` but only at the initialization
    4. Prevent later modification of `x`, `y`, `z`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zablokuj tworzenie nowych atrybutów
    3. Pozwól na zdefiniowanie `x`, `y`, `z` ale tylko przy inicjalizacji
    4. Zablokuj późniejsze modyfikacje `x`, `y`, `z`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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
