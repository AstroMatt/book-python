"""
>>> dragon = Dragon(name='Wawelski', position_x=50, position_y=120)
>>> dragon.position_set(x=10, y=20)
>>> dragon.position_change(left=10, down=20)
>>> dragon.position_change(left=10, right=15)
>>> dragon.position_change(right=15, up=5)
>>> dragon.position_change(down=5)
>>> dragon.make_damage() in range(5, 21)
True
>>> try:
...     dragon.take_damage(10)
...     dragon.take_damage(5)
...     dragon.take_damage(3)
...     dragon.take_damage(2)
...     dragon.take_damage(15)
...     dragon.take_damage(25)
...     dragon.take_damage(75)
... except IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon:name} is dead at position {dragon:position}')
Wawelski is dead at position x=20, y=40
"""
import logging
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from random import randint
from typing import TypedDict, Optional, NoReturn, Callable
from unittest import TestCase


logging.basicConfig(
    # filename='/tmp/game.csv',
    level='DEBUG',
    datefmt='"%Y-%m-%d", "%H:%M:%S"',
    format='{asctime}, "{levelname}", "{message}"',
    style='{')


# TODO: dragon << Damage(...)
# TODO: dragon >> Damage(...)
# TODO: dragon @ Position(x,y)
# TODO: dragon > Position(x, y)
# TODO: dragon[...] -> items
# TODO: hero[gold] = dragon[gold]


class IsDead(Exception):
    pass

def if_alive(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'Destructable', *args, **kwargs) -> Optional[Callable]:
        if instance.is_alive():
            return method(instance, *args, **kwargs)
        else:
            raise IsDead
    return wrapper


def if_dead(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'Destructable', *args, **kwargs) -> Optional[Callable]:
        if instance.is_dead():
            return method(instance, *args, **kwargs)
    return wrapper


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    # def __post_init__(self) -> None:
    #     if self.x < 0:
    #         raise ValueError('"x" cannot be negative')
    #
    #     if self.y < 0:
    #         raise ValueError('"y" cannot be negative')

    def __str__(self) -> str:
        return f'x={self.x}, y={self.y}'


class Moveable:
    _position: Point = Point()

    @if_alive
    def position_set(self, x: int, y: int):
        self._position: Point = Point(x, y)

    @if_alive
    def position_change(self, right: int =0, left: int =0, down: int =0, up: int =0):
        position: Point = self.position_get()
        new_x: int = position.x + right - left
        new_y: int = position.y + down - up
        self.position_set(new_x, new_y)

    def position_get(self):
        return self._position


class Status(Enum):
    ALIVE: str = 'alive'
    DEAD: str = 'dead'


class Destructable:
    _current_health: int = 0
    _status: Status = Status.ALIVE

    def _set_initial_health(self) -> None:
        self._current_health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def _update_status(self) -> None:
        if self._current_health > 0:
            self._status = Status.ALIVE
        else:
            self._status = Status.DEAD

    def is_dead(self) -> bool:
        if self._status == Status.DEAD:
            return True
        else:
            return False

    def is_alive(self) -> bool:
        return not self.is_dead()


class Drop(TypedDict):
    gold: int
    position: Point


class Dragon(Moveable, Destructable):
    position = property()

    _name: str
    _texture: str
    _gold: int

    TEXTURE_DEAD = 'img/dragon/dead.png'
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    GOLD_MIN = 1
    GOLD_MAX = 100
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    HEALTH_MIN = 50
    HEALTH_MAX = 100

    def __init__(self, name: str = 'Wawelski', position_x: int = 0, position_y: int = 0) -> None:
        self._name = name
        self._texture = self.TEXTURE_ALIVE
        self._gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self._set_initial_health()
        self.position_set(position_x, position_y)

    def __str__(self) -> str:
        return self._name

    def __format__(self, name: str) -> str:
        if name == 'name':
            return str(self._name)
        elif name == 'position':
            return str(self._position)
        elif name == 'health':
            return str(self._current_health)
        else:
            return str(self._name)

    @position.getter
    def position(self) -> Point:
        return self._position

    @if_alive
    def take_damage(self, damage) -> Optional[NoReturn]:
        self._current_health -= damage
        self._update_status()
        logging.warning(self)

        if self.is_dead():
            self._make_dead()
            raise IsDead

    def _make_dead(self) -> None:
        self._current_health = 0
        self._texture = self.TEXTURE_DEAD
        self._status = Status.DEAD

    @if_dead
    def get_drop(self) -> Drop:
        gold, self._gold = self._gold, 0
        return Drop(gold=gold, position=self.position)

    @if_alive
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


class MovableTest(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_position_default(self):
        dragon = Dragon()
        self.assertEqual(dragon.position, Point(x=0, y=0))

    def test_position_init(self):
        dragon = Dragon(position_x=1, position_y=2)
        self.assertEqual(dragon.position, Point(x=1, y=2))

    def test_position_get(self):
        self.assertEqual(self.alive.position, Point(x=0, y=0))

    def test_position_set(self):
        self.alive.position_set(x=1, y=2)
        self.assertEqual(self.alive.position, Point(x=1, y=2))

        with self.assertRaises(IsDead):
            self.dead.position_set(x=1, y=2)

    def test_position_change_right(self):
        self.alive.position_change(right=1)
        self.assertEqual(self.alive.position, Point(x=1, y=0))

        with self.assertRaises(IsDead):
            self.dead.position_change(right=1)

    def test_position_change_left(self):
        self.alive.position_change(left=1)
        self.assertEqual(self.alive.position, Point(x=-1, y=0))

        with self.assertRaises(IsDead):
            self.dead.position_change(left=1)

    def test_position_change_down(self):
        self.alive.position_change(down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=1))

        with self.assertRaises(IsDead):
            self.dead.position_change(down=1)

    def test_position_change_up(self):
        self.alive.position_change(up=1)
        self.assertEqual(self.alive.position, Point(x=0, y=-1))

        with self.assertRaises(IsDead):
            self.dead.position_change(up=1)

    def test_position_change_horizontal(self):
        self.alive.position_change(right=1, left=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))

        with self.assertRaises(IsDead):
            self.dead.position_change(right=1, left=1)

    def test_position_change_vertical(self):
        self.alive.position_change(up=1, down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))

        with self.assertRaises(IsDead):
            self.dead.position_change(up=1, down=1)


class DestructableTest(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_alive(self):
        self.assertEqual(self.alive._status, Status.ALIVE)

    def test_dead(self):
        self.assertEqual(self.dead._status, Status.DEAD)

    def test_is_dead(self):
        self.assertEqual(self.dead.is_dead(), True)

    def test_is_alive(self):
        self.assertEqual(self.alive.is_alive(), True)

    def test_destroy_alive(self):
        with self.assertRaises(IsDead):
            self.alive._current_health = 1
            self.alive.take_damage(1)

        self.assertEqual(self.alive._status, Status.DEAD)
        self.assertEqual(self.alive.is_dead(), True)

    def test_destroy_dead(self):
        with self.assertRaises(IsDead):
            self.dead.take_damage(1)

        self.assertEqual(self.dead._status, Status.DEAD)
        self.assertEqual(self.dead.is_dead(), True)


class DragonTest(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_name(self):
        a = Dragon('Alive')
        b = Dragon(name='Alive')
        self.assertEqual(a._name, 'Alive')
        self.assertEqual(b._name, 'Alive')

    def test_str(self):
        self.assertEqual(str(self.alive), 'Alive')
        self.assertEqual(f'{self.alive}', 'Alive')

    def test_format(self):
        self.alive._current_health = 1
        self.assertEqual(f'{self.alive:name}', 'Alive')
        self.assertEqual(f'{self.alive:position}', 'x=0, y=0')
        self.assertEqual(f'{self.alive:health}', '1')

    def test_texture(self):
        self.assertEqual(self.alive._texture, Dragon.TEXTURE_ALIVE)
        self.assertEqual(self.dead._texture, Dragon.TEXTURE_DEAD)

    def test_gold(self):
        self.assertIn(self.alive._gold, range(Dragon.GOLD_MIN, Dragon.GOLD_MAX + 1))

    def test_get_drop(self):
        drop = self.dead.get_drop()
        expected_position = Point(x=0, y=0)
        expected_gold = range(Dragon.GOLD_MIN, Dragon.GOLD_MAX+1)
        self.assertEqual(drop['position'], expected_position)
        self.assertIn(drop['gold'], expected_gold)
        self.assertEqual(self.dead._gold, 0)

    def test_make_dead(self):
        dragon = self.alive
        dragon._make_dead()
        self.assertTrue(dragon.is_dead())
        self.assertEqual(dragon._texture, Dragon.TEXTURE_DEAD)
        self.assertEqual(dragon._status, Status.DEAD)
        self.assertEqual(dragon._current_health, 0)

    def test_take_damage(self):
        self.alive._current_health = 2
        self.alive.take_damage(1)
        self.assertEqual(self.alive._current_health, 1)

        with self.assertRaises(IsDead):
            self.dead.take_damage(1)

        with self.assertRaises(IsDead):
            self.alive._current_health = 1
            self.alive.take_damage(1)

    def test_make_damage(self):
        expected = range(Dragon.DAMAGE_MIN, Dragon.DAMAGE_MAX+1)
        self.assertIn(self.alive.make_damage(), expected)

        with self.assertRaises(IsDead):
            self.dead.make_damage()


# a1 = Dragon(texture='...', name='Wawelski', x=50, y=120)
# a2 = Dragon(name='Wawelski', texture='...', x=50, y=120)
# b1 = Dragon(name='Wawelski', posx=50, posy=120)
# b2 = Dragon(name='Wawelski', positionx=50, positiony=120)
#-> b3 = Dragon(name='Wawelski', position_x=50, position_y=120)
# c1 = Dragon(name='Wawelski', texture='...', xy=(50, 120))
# c2 = Dragon(name='Wawelski', pos=(50, 120))
# c3 = Dragon(name='Wawelski', position=(50, 120))
# c4 = Dragon(name='Wawelski', pos_xy=(50, 120))
# c5 = Dragon(name='Wawelski', posxy=(50, 120))
# from collections import namedtuple
# Position = namedtuple('Position', ['x', 'y'])
# Position = namedtuple('Position', 'x y')
# d1 = Dragon(name='Wawelski', position=Position(x=1, y=2))
# e1 = Dragon(name='Wawelski', position={'x': 50, 'y': 120})
# f1 = Dragon(name='Wawelski', position=Position(50, 120))
#-> f2 = Dragon(name='Wawelski', position=Position(x=50, y=120))
# f3 = Dragon(name='Wawelski', position=Position(posx=50, posy=120))
# f4 = Dragon(name='Wawelski', position=Position(position_x=50, position_y=120))

#-> dragon.set_position(x=10, y=20)
# dragon.teleport()
# dragon.fly()
# dragon.ustawaw_pozycje()
# dragon.x = 10
# dragon.y = 20
# dragon.position_x = 10
# dragon.position_y = 20
# dragon._position_x = 10
# dragon._position_y = 20

#-> dragon.move(left=10, down=20)
#-> dragon.change_position(left=10, down=20)
# dragon.move(x=dragon.x-10, y=dragon.y+20)

# x = dragon.x
# y = dragon.y
# dragon.move(x=x-10, y=y+20)

# x = dragon.x - 10
# y = dragon.y + 20
# dragon.move(x=x, y=y)

# dragon.x -= 10
# dragon.y += 20

# dragon.position_x -= 10
# dragon.position_y += 20

# dragon.move(x=-10, y=+20)
# dragon.move(dx=-10, dy=+20)
# dragon.move_left(10)
# dragon.move_down(20)
# dragon.move_left_down(10, 20)

# dragon.change_position(left=-10, down=20)
# dragon.change_position((-10, 20))
# dragon.move([
#     (-10, 20),
#     (-10, 20),
#     (-10, 20)])
# dragon.move([
#     {'dx': -10, 'dy': 20},
#     {'dx': -10, 'dy': 20},
#     {'dx': -10, 'dy': 20},])
# dragon.move([
#     {'left': -10, 'down': 20},
#     {'left': -10, 'right': 20},])
# dragon.move(direction='left', distance=20)
# dragon.move(direction='right', distance=5)

# LEFT = 61
# dragon.move(direction=LEFT, distance=20)

# dragon.move([
#     {'direction': 'left', 'distance': 20},
#     {'left': -10, 'right': 20},])


#-> dragon.take_damage()
#- dragon.receive_damage()
# dragon.__sub__()
# dragon.hit()
# dragon.wound()
# dragon.damage()
# dragon.attack()

# dragon.take_damage()
# dragon.make_damage()
# dragon.receive_damage()
# dragon.deal_damage()
