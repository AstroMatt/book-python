from dataclasses import dataclass
from typing import Tuple
from unittest import TestCase


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        if not isinstance(self.x, int):
            raise TypeError

        if not isinstance(self.y, int):
            raise TypeError

    def as_tuple(self):
        return self.x, self.y


@dataclass
class Movable:
    x: int = 0
    y: int = 0
    point: Point = None

    def __post_init__(self) -> None:
        self.set_position(self.x, self.y)
        del self.x
        del self.y

    def get_position(self) -> Tuple[int, int]:
        return self.point.as_tuple()

    def set_position(self, x: int, y: int) -> None:
        self.point = Point(x, y)


@dataclass
class Dragon(Movable):
    name: str = None


class DragonTest(TestCase):
    def test_tworzenia_smoka(self):
        dragon = Dragon(name="Wawelski")
        self.assertEqual(dragon.name, "Wawelski")

    def test_tworzenia_smoka_z_pozycja(self):
        dragon = Dragon(name="Wawelski", x=1, y=2)
        x, y = dragon.get_position()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_wyswietlania_pozycji(self):
        dragon = Dragon(name="Wawelski", x=1, y=2)
        x, y = dragon.get_position()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_ustawiania_pozycji(self):
        dragon = Dragon(name="Wawelski")
        dragon.set_position(x=1, y=2)
        x, y = dragon.get_position()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_niepoprawnej_pozycji(self):
        dragon = Dragon(name="Wawelski")

        with self.assertRaises(TypeError):
            dragon.set_position(x=1, y="two")

        with self.assertRaises(TypeError):
            dragon.set_position(x="one", y=2)

        with self.assertRaises(TypeError):
            dragon.set_position(x="one", y="two")

    def test_nieprawidlowej_pozycji_przy_inicjacji(self):
        with self.assertRaises(TypeError):
            Dragon(name="Wawelski", x="one", y="two")
