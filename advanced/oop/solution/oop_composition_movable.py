"""
* Assignment: OOP Composition Movable
* Filename: oop_composition_movable.py
* Complexity: medium
* Lines of code: 20 lines
* Estimated time: 13 min

English:
    1. Define class `Point`
    2. Class `Point` has attributes `x: int = 0` and `y: int = 0`
    3. When `x` or `y` has negative value raise en exception `ValueError('Coordinate cannot be negative')`
    4. Define class `Movable`
    5. In `Movable` define method `get_position(self) -> Point`
    6. In `Movable` define method `set_position(self, x: int, y: int) -> None`
    7. In `Movable` define method `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
    8. Assume left-top screen corner as a initial coordinates position:
        a. going right add to `x`
        b. going left subtract from `x`
        c. going up subtract from `y`
        d. going down add to `y`
    9. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Point`
    2. Klasa `Point` ma atrybuty `x: int = 0` oraz `y: int = 0`
    3. Gdy `x` lub `y` mają wartość ujemną podnieś wyjątek `ValueError('Coordinate cannot be negative')`
    4. Zdefiniuj klasę `Movable`
    5. W `Movable` zdefiniuj metodę `get_position(self) -> Point`
    6. W `Movable` zdefiniuj metodę `set_position(self, x: int, y: int) -> None`
    7. W `Movable` zdefiniuj metodę `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
    8. Przyjmij górny lewy róg ekranu za punkt początkowy:
        a. idąc w prawo dodajesz `x`
        b. idąc w lewo odejmujesz `x`
        c. idąc w górę odejmujesz `y`
        d. idąc w dół dodajesz `y`
    9. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
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
    ValueError: Coordinate cannot be negative

    >>> astro.set_position(x=1, y=1)
    >>> astro.change_position(up=2)
    Traceback (most recent call last):
    ValueError: Coordinate cannot be negative
"""

from dataclasses import dataclass


# Solution
@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError('Coordinate cannot be negative')

## Solution 2
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
