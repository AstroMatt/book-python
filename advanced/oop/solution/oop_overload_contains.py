"""
* Assignment: OOP Overload Contains
* Filename: oop_overload_contains.py
* Complexity: easy
* Lines of code to write: 10 lines
* Estimated time: 13 min

English:
    1. Use code from "Input" section (see below)
    2. Override operators for code to work correctly
    3. Do not use `dataclasses`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Nadpisz operatory aby poniższy kod zadziałał poprawnie
    3. Nie używaj `dataclasses`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> astro = Astronaut('Jan Twardowski', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ...     Mission(2024, 'Artemis 3'),
    ...     Mission(2035, 'Ares 3'),
    ... ])

    >>> if Mission(2024, 'Artemis 3') in astro:
    ...    print(True)
    ... else:
    ...   print(False)
    True
"""

# Given
class Astronaut:
    def __init__(self, name, missions):
        self.name = name
        self.missions = missions


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


# Solution
class Astronaut:
    def __init__(self, name, missions):
        self.name = name
        self.missions = missions

    def __contains__(self, other):
        for mission in self.missions:
            if mission == other:
                return True
        return False


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False
