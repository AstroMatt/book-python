"""
* Assignment: OOP Overload IAdd
* Filename: oop_overload_iadd.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 5 min

English:
    1. Use code from "Input" section (see below)
    2. Override operator `+=` for code to work correctly
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Nadpisz operatory `+=` aby poniższy kod zadziałał poprawnie
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `obj.__iadd__(other) -> self`

Tests:
    >>> astro = Astronaut('Jan Twardowski', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ... ])
    >>> astro += Mission(2024, 'Artemis 3')
    >>> astro += Mission(2035, 'Ares 3')

    >>> print(astro)  # doctest: +NORMALIZE_WHITESPACE
    Astronaut(name='Jan Twardowski',
              missions=[Mission(year=1969, name='Apollo 11'),
                        Mission(year=2024, name='Artemis 3'),
                        Mission(year=2035, name='Ares 3')])
"""

# Given
from dataclasses import dataclass


@dataclass
class Astronaut:
    name: str
    missions: list


@dataclass
class Mission:
    year: int
    name: str


# Solution
@dataclass
class Astronaut:
    name: str
    missions: list

    def __iadd__(self, other):
        self.missions.append(other)
        return self


@dataclass
class Mission:
    year: int
    name: str
