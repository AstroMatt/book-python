"""
>>> from inspect import isclass, ismethod
>>> assert isclass(Point)
>>> assert isclass(Movable)
>>> assert hasattr(Point, 'x')
>>> assert hasattr(Point, 'y')
>>> assert hasattr(Movable, 'get_position')
>>> assert hasattr(Movable, 'set_position')
>>> assert hasattr(Movable, 'change_position')
>>> assert ismethod(Movable().get_position)
>>> assert ismethod(Movable().set_position)
>>> assert ismethod(Movable().change_position)

>>> class Astronaut(Movable):
...     pass

>>> astro = Astronaut()

>>> astro.set_position(x=1, y=2)
>>> astro.get_position()
Point(x=1, y=2)

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(right=1)
>>> astro.get_position()
Point(x=2, y=1)

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(left=1)
>>> astro.get_position()
Point(x=0, y=1)

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(down=1)
>>> astro.get_position()
Point(x=1, y=2)

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(up=1)
>>> astro.get_position()
Point(x=1, y=0)

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(left=2)
Traceback (most recent call last):
    ...
ValueError: Coordinate cannot be negative

>>> astro.set_position(x=1, y=1)
>>> astro.change_position(up=2)
Traceback (most recent call last):
    ...
ValueError: Coordinate cannot be negative
"""
from dataclasses import dataclass


# Solution 1
@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError('Coordinate cannot be negative')


# # Solution 2
# class Point:
#     x: int = 0
#     y: int = 0
#
#     def __init__(self, x, y):
#         if x < 0 or y < 0:
#             raise ValueError('Coordinate cannot be negative')
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Point(x={self.x}, y={self.y})'


class Movable:
    _position: Point

    def get_position(self) -> Point:
        return self._position

    def set_position(self, x: int, y: int) -> None:
        self._position = Point(x, y)

    def change_position(self,
                        left: int = 0,
                        right: int = 0,
                        up: int = 0,
                        down: int = 0
                        ) -> None:
        current = self.get_position()
        x = current.x + right - left
        y = current.y + down - up
        self.set_position(x, y)
