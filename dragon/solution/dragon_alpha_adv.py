"""
>>> import random
>>> random.seed(0)
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
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon:name} is dead at position {dragon:position}')
...     print(f'Gold dropped {drop["gold"]}')
Wawelski is dead at position x=20, y=40
Gold dropped 50
"""
from dataclasses import dataclass
from functools import wraps
from random import randint
from typing import TypedDict, Optional, NoReturn, Callable
from unittest import TestCase


# TODO: dragon << Damage(...)
# TODO: dragon >> Damage(...)
# TODO: dragon @ Position(x,y)
# TODO: dragon > Position(x, y)
# TODO: dragon[...] -> items
# TODO: hero[gold] = dragon[gold]


def if_alive(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'Destructible', *args, **kwargs) -> Optional[Callable]:
        if instance.is_alive():
            return method(instance, *args, **kwargs)
        else:
            raise instance.IsDead
    return wrapper


def if_dead(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'Destructible', *args, **kwargs) -> Optional[Callable]:
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


@dataclass
class Movable:
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


class Status:
    ALIVE: str = 'alive'
    DEAD: str = 'dead'


@dataclass
class Destructible:
    _current_health: int = 0
    _status: Status = Status.ALIVE

    class IsDead(Exception):
        pass

    def __post_init__(self) -> None:
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


@dataclass(init=False)
class Dragon(Movable, Destructible):
    TEXTURE_DEAD: str = 'img/dragon/dead.png'
    TEXTURE_ALIVE: str = 'img/dragon/alive.png'
    GOLD_MIN: int = 1
    GOLD_MAX: int = 100
    DAMAGE_MIN: int = 5
    DAMAGE_MAX: int = 20
    HEALTH_MIN: int = 50
    HEALTH_MAX: int = 100

    _name: str = None
    _texture: str = None
    _gold: int = None

    position = property()

    def __init__(self, name, position_x: int = 0, position_y: int = 0):
        self._name = name
        self._texture = self.TEXTURE_ALIVE
        self._gold = randint(self.GOLD_MIN, self.GOLD_MAX)
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
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @if_alive
    def take_damage(self, damage) -> Optional[NoReturn]:
        self._current_health -= damage
        self._update_status()

        if self.is_dead():
            self._make_dead()
            raise self.IsDead

    def _make_dead(self) -> None:
        self._current_health = 0
        self._texture = self.TEXTURE_DEAD
        self._update_status()

    @if_dead
    def get_drop(self) -> Drop:
        gold, self._gold = self._gold, 0
        return Drop(gold=gold, position=self.position)


class MovableTest(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_position_default(self):
        self.assertEqual(self.alive.position, Point(x=0, y=0))

    def test_position_init(self):
        dragon = Dragon('Alive', position_x=1, position_y=2)
        self.assertEqual(dragon.position, Point(x=1, y=2))

    def test_position_get(self):
        self.assertEqual(self.alive.position, Point(x=0, y=0))

    def test_position_set(self):
        self.alive.position_set(x=1, y=2)
        self.assertEqual(self.alive.position, Point(x=1, y=2))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_set(x=1, y=2)

    def test_position_change_right(self):
        self.alive.position_change(right=1)
        self.assertEqual(self.alive.position, Point(x=1, y=0))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(right=1)

    def test_position_change_left(self):
        self.alive.position_change(left=1)
        self.assertEqual(self.alive.position, Point(x=-1, y=0))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(left=1)

    def test_position_change_down(self):
        self.alive.position_change(down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=1))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(down=1)

    def test_position_change_up(self):
        self.alive.position_change(up=1)
        self.assertEqual(self.alive.position, Point(x=0, y=-1))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(up=1)

    def test_position_change_horizontal(self):
        self.alive.position_change(right=1, left=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(right=1, left=1)

    def test_position_change_vertical(self):
        self.alive.position_change(up=1, down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))

        with self.assertRaises(self.dead.IsDead):
            self.dead.position_change(up=1, down=1)


class DestructibleTest(TestCase):
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
        with self.assertRaises(self.alive.IsDead):
            self.alive._current_health = 1
            self.alive.take_damage(1)

        self.assertEqual(self.alive._status, Status.DEAD)
        self.assertEqual(self.alive.is_dead(), True)

    def test_destroy_dead(self):
        with self.assertRaises(self.dead.IsDead):
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

        with self.assertRaises(self.dead.IsDead):
            self.dead.take_damage(1)

        with self.assertRaises(self.dead.IsDead):
            self.alive._current_health = 1
            self.alive.take_damage(1)

    def test_make_damage(self):
        expected = range(Dragon.DAMAGE_MIN, Dragon.DAMAGE_MAX+1)
        self.assertIn(self.alive.make_damage(), expected)

        with self.assertRaises(self.dead.IsDead):
            self.dead.make_damage()

# >>> from collections import NamedTuple
# >>> Position = NamedTuple('Position', ['x', 'y'])
# >>> pt = Position(x=50, y=120)
# >>> pt.x
# 50
# >>> pt.y
# 120

# >>> from typing import TypedDict
# >>> class Position(TypedDict):
# ...     x: int
# ...     y: int
# >>> pt1 = Position(x=50, y=120)
# >>> pt2: Position = {'x': 50, 'y': 120}


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
# dragon.ustaw_pozycje()
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

# class Direction(Enum):
#     LEFT = ...
#
# dragon.move(direction=Direction.LEFT, distance=5)

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
