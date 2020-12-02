from random import randint
from unittest import TestCase


class Config:
    RESOLUTION_X_MIN = 0
    RESOLUTION_X_MAX = 1024
    RESOLUTION_Y_MIN = 0
    RESOLUTION_Y_MAX = 768

class Status:
    ALIVE = 'alive'
    DEAD = 'dead'

class Dragon:
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20

    class IsDead(Exception):
        pass

    def __init__(self, name, x=0, y=0):
        self.status = Status.ALIVE
        self.name = name
        self.position_x = x
        self.position_y = y

    def get_position(self):
        return self.position_x, self.position_y

    def set_position(self, x, y):
        if x > Config.RESOLUTION_X_MAX:
            x = Config.RESOLUTION_X_MAX

        if x < Config.RESOLUTION_X_MIN:
            x = Config.RESOLUTION_X_MIN

        if y > Config.RESOLUTION_Y_MAX:
            y = Config.RESOLUTION_Y_MAX

        if y < Config.RESOLUTION_Y_MIN:
            y = Config.RESOLUTION_Y_MIN

        self.position_x = x
        self.position_y = y

    def move(self, down=0, left=0, up=0, right=0):
        x, y = self.get_position()
        x += right - left
        y += down - up
        self.set_position(x, y)

    def make_damage(self):
        if self.is_dead():
            raise Dragon.IsDead
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def is_dead(self):
        if self.status == Status.DEAD:
            return True
        else:
            return False


class DragonTest(TestCase):
    def setUp(self) -> None:
        self.wawelski = Dragon(name='Wawelski', x=0, y=0)

    def test_crate_dragon(self):
        wawelski = Dragon(name='Wawelski')
        self.assertEqual(wawelski.name, 'Wawelski')

    def test_initial_position(self):
        wawelski = Dragon(name='Wawelski', x=50, y=120)
        self.assertEqual(wawelski.position_x, 50)
        self.assertEqual(wawelski.position_y, 120)
        self.assertEqual(wawelski.get_position(), (50, 120))

    def test_set_position(self):
        self.wawelski.set_position(10, 20)
        self.assertEqual(self.wawelski.get_position(), (10, 20))

    def test_left(self):
        self.wawelski.move(left=1)
        self.assertEqual(self.wawelski.get_position(), (0, 0))

    def test_right(self):
        self.wawelski.move(right=1)
        self.assertEqual(self.wawelski.get_position(), (1, 0))

    def test_up(self):
        self.wawelski.move(up=1)
        self.assertEqual(self.wawelski.get_position(), (0, 0))

    def test_down(self):
        self.wawelski.move(down=1)
        self.assertEqual(self.wawelski.get_position(), (0, 1))

    def test_border_invalid(self):
        self.wawelski.set_position(-1, 0)
        self.assertEqual(self.wawelski.get_position(), (0, 0))

        self.wawelski.set_position(0, -1)
        self.assertEqual(self.wawelski.get_position(), (0, 0))

        self.wawelski.set_position(-1, -1)
        self.assertEqual(self.wawelski.get_position(), (0, 0))

    def test_make_damage(self):
        dmg = self.wawelski.make_damage()
        self.assertGreaterEqual(dmg, self.wawelski.DAMAGE_MIN)
        self.assertLessEqual(dmg, self.wawelski.DAMAGE_MAX)

    def test_exception_making_damage_when_dragon_is_dead(self):
        self.wawelski.status = Status.DEAD

        with self.assertRaises(Dragon.IsDead):
            self.wawelski.make_damage()
