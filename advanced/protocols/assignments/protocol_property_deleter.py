"""
* Assignment: Protocol Property Deleter
* Filename: protocol_property_deleter.py
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Point` with `x`, `y`, `z` attributes
    3. Define property `position` in class `Point`
    4. Deleting `position` sets all attributes to 0 (`x=0`, `y=0`, `z=0`)
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zdefiniuj property `position` w klasie `Point`
    4. Usunięcie `position` ustawia wszystkie atrybuty na 0 (`x=0`, `y=0`, `z=0`)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> del pt.position
    >>> pt.x, pt.y, pt.z
    (0, 0, 0)
"""


# Given
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


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
