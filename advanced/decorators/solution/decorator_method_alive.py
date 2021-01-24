def if_alive(method):
    def wrapper(hero, *args, **kwargs):
        if hero.current_health > 0:
            return method(hero, *args, **kwargs)
        else:
            print('Hero is dead and cannot make damage')
    return wrapper


class Hero:
    def __init__(self, name):
        self.name = name
        self.current_health = 100

    @if_alive
    def make_damage(self):
        return 10


hero = Hero('Jan Twardowski')
print(hero.make_damage())
# 10

hero.current_health = -10
print(hero.make_damage())
# Traceback (most recent call last):
#     ...
# RuntimeError: Hero is dead and cannot make damage
