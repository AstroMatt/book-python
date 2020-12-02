"""
* Assignment: Decorator Method Alive
* Filename: decorator_method_alive.py
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create `if_alive` method decorator
    3. Decorator will allow running `make_damage` method
       only if `current_health` is greater than 0
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator metody `if_alive`
    3. Dekorator pozwoli na wykonanie metody `make_damage`,
       tylko gdy `current_health` jest większe niż 0
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> class Hero:
    ...    def __init__(self, name):
    ...        self.name = name
    ...        self.current_health = 100
    ...
    ...    @if_alive
    ...    def make_damage(self):
    ...        return 10

    >>> hero = Hero('Jan Twardowski')
    >>> hero.make_damage()
    10
    >>> hero.current_health = -10
    >>> hero.make_damage()
    Traceback (most recent call last):
    RuntimeError: Hero is dead and cannot make damage
"""


# Given
def if_alive(method):
    def wrapper(hero, *args, **kwargs):
        return method(hero, *args, **kwargs)
    return wrapper


# Solution
def if_alive(method):
    def wrapper(self, *args, **kwargs):
        if self.current_health > 0:
            return method(self, *args, **kwargs)
        else:
            raise RuntimeError('Hero is dead and cannot make damage')
    return wrapper
