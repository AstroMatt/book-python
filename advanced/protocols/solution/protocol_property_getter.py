"""
* Assignment: Protocol Property Getter
* Filename: protocol_property_getter.py
* Complexity: easy
* Lines of code: 9 lines
* Estimated time: 5 min

English:
    1. Define class `Point` with `x`, `y`, `z` attributes
    2. Define property `position` in class `Point`
    3. Accessing `position` returns `(x, y, z)`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zdefiniuj property `position` w klasie `Point`
    3. Dostęp do `position` zwraca `(x, y, z)`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position
    (1, 2, 3)
"""


# Solution
class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.getter
    def position(self):
        return self.x, self.y, self.z
