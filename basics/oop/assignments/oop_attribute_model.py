"""
* Assignment: OOP Attribute Model
* Filename: oop_attribute_model.py
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Model the data using classes
    3. How many classes are there?
    4. How many instances are there?
    5. Create instances filling it with data
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zamodeluj dane za pomocą klas
    3. Ile jest klas?
    4. Ile jest instancji?
    5. Stwórz instancje wypełniając je danymi
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Mark Watney' in watney.__dict__.values()
    >>> assert 'USA' in watney.__dict__.values()
    >>> assert '1969-07-21' in watney.__dict__.values()
    >>> assert 'National Aeronautics and Space Administration' in nasa.__dict__.values()
    >>> assert 'USA' in nasa.__dict__.values()
    >>> assert '1958-07-29' in nasa.__dict__.values()
"""

# Given
"""
Mark Watney, USA, 1969-07-21
National Aeronautics and Space Administration, USA, 1958-07-29
"""

# Solution
class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
watney.name = 'Mark Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa = SpaceAgency()
nasa.name = 'National Aeronautics and Space Administration'
nasa.country = 'USA'
nasa.date = '1958-07-29'
