"""
* Assignment: Protocol Iterator Implementation
* Filename: protocol_iterator_implementation.py
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Modify classes to implement iterator protocol
    3. Iterator should return instances of `Mission`
    4. All tests must pass
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zmodyfikuj klasy aby zaimplementować protokół iterator
    3. Iterator powinien zwracać instancje `Mission`
    4. Wszystkie testy muszą przejść
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass, ismethod
    >>> assert isclass(Astronaut)

    >>> astro = Astronaut('Mark', 'Watney')
    >>> assert hasattr(astro, 'firstname')
    >>> assert hasattr(astro, 'lastname')
    >>> assert hasattr(astro, 'missions')
    >>> assert hasattr(astro, '__iter__')
    >>> assert hasattr(astro, '__next__')
    >>> assert ismethod(astro.__iter__)
    >>> assert ismethod(astro.__next__)

    >>> astro = Astronaut('Jan', 'Twardowski', missions=(
    ...     Mission(1969, 'Apollo 11'),
    ...     Mission(2024, 'Artemis 3'),
    ...     Mission(2035, 'Ares 3'),
    ... ))

    >>> for mission in astro:
    ...     print(mission)
    Mission(year=1969, name='Apollo 11')
    Mission(year=2024, name='Artemis 3')
    Mission(year=2035, name='Ares 3')
"""
# Given
from dataclasses import dataclass


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()


@dataclass
class Mission:
    year: int
    name: str


# Solution
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.missions):
            raise StopIteration

        result = self.missions[self._iter_index]
        self._iter_index += 1
        return result
