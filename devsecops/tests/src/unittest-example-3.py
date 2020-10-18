from dataclasses import dataclass
from unittest import TestCase


@dataclass
class Longitude:
    value: float

    def __post_init__(self):
        if self.value > 180:
            raise ValueError
        if self.value < -180:
            raise ValueError


@dataclass
class Latitude:
    value: float

    def __post_init__(self):
        if self.value > 90:
            raise ValueError
        if self.value < -90:
            raise ValueError


@dataclass
class GEOCoordinates:
    lat: Latitude
    lon: Longitude


class LongitudeTest(TestCase):
    def test_init_latitude(self):
        l = Latitude(0)
        self.assertEqual(l.value, 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Latitude(-180.1)

        with self.assertRaises(ValueError):
            Latitude(180.1)


class LatitudeTest(TestCase):
    def test_init_latitude(self):
        l = Latitude(0)
        self.assertEqual(l.value, 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Latitude(-90.1)

        with self.assertRaises(ValueError):
            Latitude(90.1)


class GEOCoordinatesTest(TestCase):
    def test_set_longitude(self):
        lat = Latitude(-90)
        lon = Longitude(20)
        geo = GEOCoordinates(lat, lon)
