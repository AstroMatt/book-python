"""
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
from dataclasses import dataclass


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
