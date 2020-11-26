"""
* Assignment: OOP Inheritance Super
* Filename: oop_inheritance_super.py
* Complexity: easy
* Lines of code to write: 8 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Astronaut` which inherits from `Person`
    3. Using positional arguments at the initialization set astronaut first name and last name
    4. All astronauts must have name inherited from `Person`
    5. Return first name, last name and mission name from `__str__()`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Astronaut` dziedziczącą po `Person`
    3. Używając parametrów pozycyjnych podanych przy inicjalizacji ustaw imię i nazwisko astronauty
    4. Każdy astronauta musi mieć imię i nazwisko odziedziczone z `Person`
    5. Zwróć imię, nazwisko i nazwę misji from `__str__()`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> mark = Astronaut('Mark Watney', 'Ares 3')
    >>> str(mark)
    'Mark Watney (Ares 3)'
    >>> melissa = Astronaut('Melissa Lewis', 'Ares 3')
    >>> str(melissa)
    'Melissa Lewis (Ares 3)'
"""


# Given
class Person:
    def __init__(self, name):
        self.name = name


# Solution
class Astronaut(Person):
    def __init__(self, name, mission):
        super().__init__(name)
        self.mission = mission

    def __str__(self):
        return f'{self.name} ({self.mission})'
