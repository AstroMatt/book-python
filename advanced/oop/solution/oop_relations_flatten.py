import csv

FILE = r'/tmp/csv_relations.csv'


class Astronaut:
    def __init__(self, first_name, last_name, missions=None):
        self.first_name = first_name
        self.last_name = last_name
        self.missions = missions if missions else []


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


CREW = [
    Astronaut('Jan', 'Twardowski', missions=[
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3')]),

    Astronaut('Mark', 'Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa', 'Lewis'),
]


result = []

for astronaut in CREW:
    astro = astronaut.__dict__
    missions = [list(x.__dict__.values()) for x in astronaut.missions]
    astro['missions'] = ', '.join(map(str, missions))
    result.append(astro)


header = set(key for key in astro.keys()
                    for astro in result)


with open(FILE, mode='w') as file:

    writer = csv.DictWriter(
        f=file,
        fieldnames=sorted(header, reverse=True),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in result:
        writer.writerow(row)
