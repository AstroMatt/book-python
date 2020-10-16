"""
>>> place1 = GeographicCoordinate(50, 120, 8000)
>>> place1
Latitude: 50, Longitude: 120, Elevation: 8000

>>> place2 = GeographicCoordinate(22, 33, 44)
>>> place2
Latitude: 22, Longitude: 33, Elevation: 44

>>> place1.latitude = 1
>>> place1.longitude = 2
>>> place1
Latitude: 1, Longitude: 2, Elevation: 8000

>>> place2
Latitude: 22, Longitude: 33, Elevation: 44

>>> GeographicCoordinate(90, 0, 0)
Latitude: 90, Longitude: 0, Elevation: 0
>>> GeographicCoordinate(-90, 0, 0)
Latitude: -90, Longitude: 0, Elevation: 0
>>> GeographicCoordinate(0, +180, 0)
Latitude: 0, Longitude: 180, Elevation: 0
>>> GeographicCoordinate(0, -180, 0)
Latitude: 0, Longitude: -180, Elevation: 0
>>> GeographicCoordinate(0, 0, +8848)
Latitude: 0, Longitude: 0, Elevation: 8848
>>> GeographicCoordinate(0, 0, -10994)
Latitude: 0, Longitude: 0, Elevation: -10994

>>> GeographicCoordinate(-91, 0, 0)
Traceback (most recent call last):
  ...
ValueError: Out of bounds

>>> GeographicCoordinate(+91, 0, 0)
Traceback (most recent call last):
  ...
ValueError: Out of bounds

>>> GeographicCoordinate(0, -181, 0)
Traceback (most recent call last):
  ...
ValueError: Out of bounds

>>> GeographicCoordinate(0, +181, 0)
Traceback (most recent call last):
  ...
ValueError: Out of bounds

>>> GeographicCoordinate(0, 0, -10995)
Traceback (most recent call last):
  ...
ValueError: Out of bounds

>>> GeographicCoordinate(0, 0, +8849)
Traceback (most recent call last):
  ...
ValueError: Out of bounds
"""

class RangeValidator:
    MIN = None
    MAX = None

    @property
    def attrname(self):
        return '_' + self.__class__.__name__.lower()

    def __set__(self, parent, value):
        if self.MIN <= value <= self.MAX:
            setattr(parent, self.attrname, value)
        else:
            raise ValueError('Out of bounds')

    def __get__(self, parent, parent_type):
        return getattr(parent, self.attrname)


class Latitude(RangeValidator):
    MIN = -90
    MAX = +90


class Longitude(RangeValidator):
    MIN = -180
    MAX = +180


class Elevation(RangeValidator):
    MIN = -10994
    MAX = +8848


class GeographicCoordinate:
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()

    def __init__(self, latitude, longitude, elevation):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __repr__(self):
        return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'
