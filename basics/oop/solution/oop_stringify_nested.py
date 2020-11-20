"""
>>> melissa = Astronaut('Melissa Lewis')
>>> print(f'Commander: \\n{melissa}\\n')  # doctest: +NORMALIZE_WHITESPACE
Commander:
Melissa Lewis

>>> mark = Astronaut('Mark Watney', experience=[
...    Mission(2035, 'Ares 3')])
>>> print(f'Space Pirate: \\n{mark}\\n')  # doctest: +NORMALIZE_WHITESPACE
Space Pirate:
Mark Watney veteran of [
      2035: Ares 3]

>>> crew = Crew([
...     Astronaut('Jan Twardowski', experience=[
...         Mission(1969, 'Apollo 11'),
...         Mission(2024, 'Artemis 3'),
...     ]),
...     Astronaut('José Jiménez'),
...     Astronaut('Mark Watney', experience=[
...         Mission(2035, 'Ares 3'),
...     ]),
... ])

>>> print(f'Crew: \\n{crew}')  # doctest: +NORMALIZE_WHITESPACE
Crew:
Jan Twardowski veteran of [
      1969: Apollo 11,
      2024: Artemis 3]
José Jiménez
Mark Watney veteran of [
      2035: Ares 3]
"""


class Crew:
    def __init__(self, members=()):
        self.members = list(members)

    def __str__(self):
        return '\n'.join(str(x) for x in self.members)


class Astronaut:
    def __init__(self, name, experience=()):
        self.name = name
        self.experience = list(experience)

    def __str__(self):
        if not self.experience:
            return f'{self.name}'
        return f'{self.name} veteran of {self.experience}'

    def __repr__(self):
        return self.__str__()


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\t{self.year}: {self.name}'
