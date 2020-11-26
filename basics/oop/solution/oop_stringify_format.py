"""
* Assignment: OOP Stringify Format
* Filename: oop_stringify_format.py
* Complexity: easy
* Lines of code to write: 8 lines
* Estimated time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Overload `__format__()` to convert length units
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Przeciąż `__format__()` aby konwertował jednostki długości
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 km = 1000 m
    * 1 m = 100 cm

Tests:
    >>> result = Distance(meters=1337)
    >>> format(result, 'km')
    '1.337'
    >>> format(result, 'cm')
    '133700'
    >>> format(result, 'm')
    '1337'
"""

# Given
class Distance:
    def __init__(self, meters):
        self.meters = meters


# Solution
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        if unit in ('cm', 'centimeter', 'centimeters'):
            result = self.meters * 100
        elif unit in ('m', 'meter', 'meters'):
            result = self.meters
        elif unit in ('km', 'kilometer', 'kilometers'):
            result = self.meters / 1000
        return str(result)
