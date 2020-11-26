"""
* Assignment: OOP Class Instance
* Filename: oop_class_instance.py
* Complexity: easy
* Lines of code to write: 9 lines
* Estimated time: 5 min

English:
    1. Define class ``Astronaut``
    2. Define class ``SpaceAgency``
    3. Create instance ``watney`` of a class ``Astronaut``
    4. Create instance ``nasa`` of a class ``SpaceAgency``
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę ``Astronaut``
    2. Zdefiniuj klasę ``SpaceAgency``
    3. Stwórz instancję ``watney`` klasy ``Astronaut``
    4. Stwórz instancję ``nasa`` klasy ``SpaceAgency``
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Astronaut)
    >>> assert isclass(SpaceAgency)
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
"""


# Solution
class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
nasa = SpaceAgency()
