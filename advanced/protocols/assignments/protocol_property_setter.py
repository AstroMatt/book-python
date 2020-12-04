"""
* Assignment: Protocol Property Setter
* Filename: protocol_property_setter.py
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Point` with `x`, `y`, `z` attributes
    3. Define property `position` in class `Point`
    4. Setting `position`:
        a. If argument is not list, tuple, set raise Type Error
        b. If argument has length other than 3, raise Value
        b. Else sets `x`, `y`, `z` attributes from sequence
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zdefiniuj property `position` w klasie `Point`
    4. Ustawianie `position`:
        a. Jeżeli argument nie jest list, tuple, set podnieś TypeError
        b. Jeżeli argument nie ma długości 3, podnieś ValueError
        b. W przeciwnym wypadku ustaw kolejne atrybuty `x`, `y`, `z` z sekwencji
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position = 4, 5, 6
    >>> pt.x, pt.y, pt.z
    (4, 5, 6)
    >>> pt.position = [7, 8, 9]
    >>> pt.x, pt.y, pt.z
    (7, 8, 9)
    >>> pt.position = 1, 2
    Traceback (most recent call last):
    ValueError
    >>> pt.position = {'a':1, 'b':2}
    Traceback (most recent call last):
    TypeError
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

    @position.setter
    def position(self, new_value):
        if type(new_value) not in (list, tuple, set):
            raise TypeError
        elif len(new_value) != 3:
            raise ValueError
        else:
            self.x, self.y, self.z = new_value
