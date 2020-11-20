"""
>>> from inspect import isclass
>>> assert isclass(Astronaut)
>>> assert isclass(SpaceAgency)
>>> assert isinstance(watney, Astronaut)
>>> assert isinstance(nasa, SpaceAgency)
"""


class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
nasa = SpaceAgency()
