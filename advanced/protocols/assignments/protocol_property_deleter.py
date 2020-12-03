"""
* Assignment: Protocol Property Deleter
* Filename: protocol_property_deleter.py
* Complexity: easy
* Lines of code: 11 lines
* Time: 5 min

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
    >>> del pt.position
    >>> pt.x, pt.y, pt.z
    (0, 0, 0)
"""


# Solution
class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.deleter
    def position(self):
        self.x = 0
        self.y = 0
        self.z = 0
