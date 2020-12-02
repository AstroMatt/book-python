from dataclasses import dataclass, FrozenInstanceError
from typing import NoReturn, Optional
from unittest import TestCase, skip
from datetime import timezone, datetime


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if not isinstance(self.x, int):
            raise TypeError

        if not isinstance(self.y, int):
            raise TypeError


class PointTest(TestCase):
    def test_create(self):
        p = Point()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

    def test_change(self):
        with self.assertRaises(FrozenInstanceError):
            p = Point()
            p.x = 10

        with self.assertRaises(FrozenInstanceError):
            p = Point()
            p.y = 10


class Movable:
    def set_position(self, position: Point) -> Optional[NoReturn]:
        if not isinstance(position, Point):
            raise TypeError

        self._position = position

    def get_position(self) -> Point:
        return self._position


class Dragon(Movable):
    def __init__(self, name, position: Point = Point()):
        self.name = name
        self.created_date = datetime.now(tz=timezone.utc)
        self.set_position(position)


class DragonTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon(name="Wawelski")

    def test_dragon_create(self):
        dragon = Dragon(name="Wawelski")
        self.assertEqual(dragon.name, "Wawelski")

    def test_initial_position(self):
        dragon = Dragon(name="Wawelski", position=Point(x=50, y=120))
        x, y = dragon.get_position()
        self.assertEqual(x, 50)
        self.assertEqual(y, 120)

    def test_get_position_type(self):
        position = self.dragon.get_position()
        self.assertIsInstance(position, Point)

    def test_get_position_values(self):
        x, y = self.dragon.get_position()
        self.assertIsInstance(x, int)
        self.assertIsInstance(y, int)

    def test_bad_initial_position(self):
        with self.assertRaises(TypeError):
            Dragon(name="Wawelski", position=Point(x=0, y="a"))

        with self.assertRaises(TypeError):
            Dragon(name="Wawelski", position=Point(x="a", y=0))

    def test_set_position(self):
        self.dragon.set_position(Point(x=100, y=200))
        position = self.dragon.get_position()
        self.assertEqual(position.x, 100)
        self.assertEqual(position.y, 200)

    def test_bad_position_x(self):
        with self.assertRaises(TypeError):
            p = Point(x=50.5, y=0)
            self.dragon.set_position(p)

    def test_bad_position_y(self):
        with self.assertRaises(TypeError):
            p = Point(x=0, y="a")
            self.dragon.set_position(p)

    def test_created_date_in_utc(self):
        self.assertEqual(self.dragon.created_date.tzinfo, timezone.utc)
