"""
* Assignment: Protocol Property Setter
* Filename: protocol_property_setter.py
* Complexity: easy
* Lines of code: 9 lines
* Estimated time: 5 min

English:
    1. Define class `Point` with `x`, `y`, `z` attributes
    2. Define property `position` in class `Point`
    3. Deleting `position` sets all attributes to 0 (`x=0`, `y=0`, `z=0`)
    4. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zdefiniuj property `position` w klasie `Point`
    3. Usunięcie `position` ustawia wszystkie atrybuty na 0 (`x=0`, `y=0`, `z=0`)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position = (4, 5, 6)
    Traceback (most recent call last):
    PermissionError: Cannot modify values
"""


# Solution
class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.setter
    def position(self, new_value):
        raise PermissionError('Cannot modify values')
