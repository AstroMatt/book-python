"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski', 'missions': '1969,Apollo 11;2024,Artemis 3'},
 {'firstname': 'Mark', 'lastname': 'Watney', 'missions': '2035,Ares 3'},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'missions': ''}]
"""

import csv

FILE = r'/tmp/oop-relations.csv'


class Astronaut:
    def __init__(self, firstname, lastname, missions=()):
        self.firstname = firstname
        self.lastname = lastname
        self.missions = list(missions)


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


DATA = [
    Astronaut('Jan', 'Twardowski', missions=[
        Mission('1969', 'Apollo 11'),
        Mission('2024', 'Artemis 3')]),

    Astronaut('Mark', 'Watney', missions=[
        Mission('2035', 'Ares 3')]),

    Astronaut('Melissa', 'Lewis'),
]


result = []
for astronaut in DATA:
    astronaut.missions = [','.join(x.__dict__.values()) for x in astronaut.missions]
    astronaut.missions = ';'.join(astronaut.missions)
    result.append(astronaut.__dict__)


with open(FILE, mode='w') as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=sorted(result[0].keys()),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')
    writer.writeheader()
    writer.writerows(result)
