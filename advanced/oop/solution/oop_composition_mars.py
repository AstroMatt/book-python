"""
>>> from inspect import isclass
>>> assert isclass(Habitat)
>>> assert isclass(Astronaut)
>>> assert isclass(Rocket)
>>> assert isclass(MarsMission)
>>> assert issubclass(MarsMission, Habitat)
>>> assert issubclass(MarsMission, Astronaut)
>>> assert issubclass(MarsMission, Rocket)
"""


class Habitat:
    pass


class Astronaut:
    pass


class Rocket:
    pass


class MarsMission(Habitat, Astronaut, Rocket):
    pass
