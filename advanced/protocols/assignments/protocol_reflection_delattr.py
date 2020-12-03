"""
* Assignment: Protocol Reflection Delattr
* Filename: protocol_reflection_delattr.py
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create class `Point` with `x`, `y`, `z` attributes
    2. Prevent deleting attributes
    3. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zablokuj usuwanie atrybutów
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)

    >>> del pt.x
    Traceback (most recent call last):
    PermissionError: Cannot delete attributes

    >>> del pt.notexisting
    Traceback (most recent call last):
    PermissionError: Cannot delete attributes
"""

# Solution
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError('Cannot delete attributes')
