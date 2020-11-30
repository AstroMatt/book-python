"""
* Assignment: OOP Relations Flatten
* Filename: oop_relations_flatten.py
* Complexity: hard
* Lines of code to write: 5 lines
* Estimated time: 21 min

English:
    1. Use code from "Input" section (see below)
    2. How to write relations to CSV file (contact has many addresses)?
    3. Convert `DATA` to `resul: list[dict[str,str]]`
    4. Non-functional requirements:
        a. Use `,` to separate fields
        b. Use `;` to separate columns
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    3. Przekonwertuj `DATA` do `resul: list[dict[str,str]]`
    4. Wymagania niefunkcjonalne:
        b. Użyj `,` do oddzielenia pól
        b. Użyj `;` do oddzielenia kolumn
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Jan', 'lastname': 'Twardowski', 'missions': '1967,Apollo 1;1970,Apollo 13;1973,Apollo 18'},
     {'firstname': 'Ivan', 'lastname': 'Ivanovic', 'missions': '2023,Artemis 2;2024,Artemis 3'},
     {'firstname': 'Mark', 'lastname': 'Watney', 'missions': '2035,Ares 3'},
     {'firstname': 'Melissa', 'lastname': 'Lewis', 'missions': ''}]
"""

# Given
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
        Mission('1967', 'Apollo 1'),
        Mission('1970', 'Apollo 13'),
        Mission('1973', 'Apollo 18')]),

    Astronaut('Ivan', 'Ivanovic', missions=[
        Mission('2023', 'Artemis 2'),
        Mission('2024', 'Artemis 3')]),

    Astronaut('Mark', 'Watney', missions=[
        Mission('2035', 'Ares 3')]),

    Astronaut('Melissa', 'Lewis')]


result: list = []


# Solution
result = []

for astronaut in DATA:
    astronaut.missions = [','.join(x.__dict__.values()) for x in astronaut.missions]
    astronaut.missions = ';'.join(astronaut.missions)
    result.append(astronaut.__dict__)
