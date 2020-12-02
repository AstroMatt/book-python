"""
* Assignment: OOP Composition Decompose
* Filename: oop_composition_decompose.py
* Complexity: easy
* Lines of code: 30 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Refactor class `Hero` to use composition
    3. Name mixin classes: `HasHealth` and `HasPosition`
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zrefaktoruj klasę `Hero` aby użyć kompozycji
    3. Nazwij klasy domieszkowe: `HasHealth` i `HasPosition`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from random import seed; seed(0)
    >>> from inspect import isclass
    >>> assert isclass(Hero)
    >>> assert isclass(HasHealth)
    >>> assert isclass(HasPosition)
    >>> assert issubclass(Hero, HasHealth)
    >>> assert issubclass(Hero, HasPosition)
    >>> assert hasattr(HasHealth, 'HEALTH_MIN')
    >>> assert hasattr(HasHealth, 'HEALTH_MAX')
    >>> assert hasattr(HasHealth, '_health')
    >>> assert hasattr(HasHealth, 'is_alive')
    >>> assert hasattr(HasHealth, 'is_dead')
    >>> assert hasattr(HasPosition, '_position_x')
    >>> assert hasattr(HasPosition, 'position_set')
    >>> assert hasattr(HasPosition, 'position_change')
    >>> assert hasattr(HasPosition, 'position_get')
    >>> assert hasattr(Hero, 'HEALTH_MIN')
    >>> assert hasattr(Hero, 'HEALTH_MAX')
    >>> assert hasattr(Hero, '_health')
    >>> assert hasattr(Hero, '_position_x')
    >>> assert hasattr(Hero, 'is_alive')
    >>> assert hasattr(Hero, 'is_dead')
    >>> assert hasattr(Hero, 'position_set')
    >>> assert hasattr(Hero, 'position_change')
    >>> assert hasattr(Hero, 'position_get')
    >>> watney = Hero()
    >>> watney.is_alive()
    True
    >>> watney.position_set(x=1, y=2)
    >>> watney.position_change(left=1, up=2)
    >>> watney.position_get()
    (0, 0)
    >>> watney.position_change(right=1, down=2)
    >>> watney.position_get()
    (1, 2)
"""

# Given
from dataclasses import dataclass
from random import randint


@dataclass
class Hero:
    HEALTH_MIN: int = 10
    HEALTH_MAX: int = 20
    _health: int = 0
    _position_x: int = 0
    _position_y: int = 0

    def __post_init__(self) -> None:
        self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def is_alive(self) -> bool:
        return self._health > 0

    def is_dead(self) -> bool:
        return self._health <= 0

    def position_set(self, x: int, y: int) -> None:
        self._position_x = x
        self._position_y = y

    def position_change(self, right=0, left=0, down=0, up=0):
        x = self._position_x + right - left
        y = self._position_y + down - up
        self.position_set(x, y)

    def position_get(self) -> tuple[int, int]:
        return self._position_x, self._position_y


# Solution
@dataclass
class HasHealth:
    HEALTH_MIN: int = 10
    HEALTH_MAX: int = 20
    _health: int = 0

    def __post_init__(self) -> None:
        self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def is_alive(self) -> bool:
        return self._health > 0

    def is_dead(self) -> bool:
        return self._health <= 0


@dataclass
class HasPosition:
    _position_x: int = 0
    _position_y: int = 0

    def position_set(self, x: int, y: int) -> None:
        self._position_x = x
        self._position_y = y

    def position_change(self, right=0, left=0, down=0, up=0):
        x = self._position_x + right - left
        y = self._position_y + down - up
        self.position_set(x, y)

    def position_get(self) -> tuple[int, int]:
        return self._position_x, self._position_y


class Hero(HasHealth, HasPosition):
    pass
