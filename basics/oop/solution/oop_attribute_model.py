"""
>>> assert isinstance(watney, Astronaut)
>>> assert isinstance(nasa, SpaceAgency)
>>> assert 'Mark Watney' in watney.__dict__.values()
>>> assert 'USA' in watney.__dict__.values()
>>> assert '1969-07-21' in watney.__dict__.values()
>>> assert 'National Aeronautics and Space Administration' in nasa.__dict__.values()
>>> assert 'USA' in nasa.__dict__.values()
>>> assert '1958-07-29' in nasa.__dict__.values()
"""


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
