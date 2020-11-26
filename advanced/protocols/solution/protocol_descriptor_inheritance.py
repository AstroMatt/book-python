"""
* Assignment: Protocol Descriptor Inheritance
* Filename: protocol_descriptor_inheritance.py
* Complexity: medium
* Lines of code to write: 25 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `GeographicCoordinate`
    3. Use descriptors to check value boundaries
    4. All tests must pass
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `GeographicCoordinate`
    3. Użyj deskryptory do sprawdzania wartości brzegowych
    4. Wszystkie testy muszą przejść
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
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

# Given
class GeographicCoordinate:
    def __str__(self):
        return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()


"""
latitude - min: -90.0, max: 90.0
longitude - min: -180.0, max: 180.0
elevation - min: -10994.0, max: 8848.0
"""


# Solution
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
