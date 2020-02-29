import pickle


class Astronaut:
    def __init__(self, name, missions=()):
        self.name = name
        self.missions = missions

    def __repr__(self):
        return f'\n\nAstronaut(name="{self.name}", missions={self.missions})'


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\tMission(year={self.year}, name="{self.name}")'


CREW = [
    Astronaut('Jan Twardowski', missions=(
        Mission(1969, 'Apollo 18'),
        Mission(2024, 'Artemis 3'))),

    Astronaut('Mark Watney', missions=(
        Mission(2035, 'Ares 3'))),

    Astronaut('Melissa Lewis'),
]

with open(r'/tmp/astronauts.pkl', mode='wb') as file:
    pickle.dump(CREW, file)


with open(r'/tmp/astronauts.pkl', mode='rb') as file:
    output = pickle.load(file)


print(output)
# [
#
# Astronaut(name="Jan Twardowski", missions=(
# 	Mission(year=1969, name="Apollo 18"),
# 	Mission(year=2024, name="Artemis 3"))),
#
# Astronaut(name="Mark Watney", missions=
# 	Mission(year=2035, name="Ares 3")),
#
# Astronaut(name="Melissa Lewis", missions=())]
