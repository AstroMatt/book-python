"""
>>> from inspect import isclass
>>> assert isclass(Scientist)
>>> assert isclass(Engineer)
>>> assert isclass(Pilot)
>>> assert isclass(MedicalDoctor)
>>> assert isclass(Astronaut)
>>> assert issubclass(Astronaut, Scientist)
>>> assert issubclass(Astronaut, Engineer)
>>> assert issubclass(Astronaut, Pilot)
>>> assert issubclass(Astronaut, MedicalDoctor)
"""

class Scientist:
    pass


class Engineer:
    pass


class Pilot:
    pass


class MedicalDoctor:
    pass


class Astronaut(Scientist, Engineer, Pilot, MedicalDoctor):
    pass
