"""
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
