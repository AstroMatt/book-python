"""
* Assignment: OOP Inheritance Multiple
* Filename: oop_inheritance_multiple.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 2 min

English:
    1. Use data from "Given" section (see below)
    2. Create class ``Astronaut`` which inherits from all of those classes
    3. Compare result with "Tests" section (see below)

Polish:
    1. Use data from "Given" section (see below)
    2. Stwórz klasę ``Astronaut``, która dziedziczy po tych wszystkich klasach
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Scientist)
    >>> assert isclass(Engineer)
    >>> assert isclass(Pilot)
    >>> assert isclass(MedicalDoctor)
    >>> assert isclass(Astronaut)
    >>> assert issubclass(Astronaut, Scientist)
    >>> assert issubclass(Astronaut, Engineer)
    >>> assert issubclass(Astronaut, Pilot)
    >>> assert issubclass(Astronaut, MedicalDoctor)
"""


# Given
class Scientist:
    pass


class Engineer:
    pass


class Pilot:
    pass


class MedicalDoctor:
    pass


# Solution
class Astronaut(Scientist, Engineer, Pilot, MedicalDoctor):
    pass
