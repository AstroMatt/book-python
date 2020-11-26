"""
* Assignment: OOP Inheritance Simple
* Filename: oop_inheritance_simple.py
* Complexity: easy
* Lines of code to write: 4 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Woman` which inherits from `Venus`
    3. Create class `Man` which inherits from `Mars`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Woman`, która dziedziczy po `Venus`
    3. Stwórz klasę `Man`, która dziedziczy po `Mars`

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Venus)
    >>> assert isclass(Woman)
    >>> assert isclass(Mars)
    >>> assert isclass(Man)
    >>> assert issubclass(Woman, Venus)
    >>> assert issubclass(Man, Mars)
"""


# Given
class Venus:
    pass


class Mars:
    pass


# Solution
class Woman(Venus):
    pass


class Man(Mars):
    pass
