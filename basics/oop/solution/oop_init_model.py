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
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


watney = Astronaut('Mark Watney', 'USA', '1969-07-21')

nasa = SpaceAgency(
    name='National Aeronautics and Space Administration',
    country='USA',
    date='1958-07-29')
