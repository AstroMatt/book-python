from enum import Enum
from .dragon_alpha_adv import Dragon, Status, Position, Movable


class Status(Status):
    FULL_HEALTH = 'Full Health'
    INJURED = 'Injured'
    BADLY_WOUNDED = 'Badly Wounded'
    NEAR_DEAD = 'Near Death'


class Config:
    BORDER_X_MAX = 1024
    BORDER_X_MIN = 0
    BORDER_Y_MAX = 768
    BORDER_Y_MIN = 0


class Character(Dragon):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items = []
        self._health_full = self._health_current

    def update_status(self):
        if not hasattr(self, '_health_full'):
            self._health_full = self._health_current

        percent = self._health_current / self._health_full * 100

        if percent == 100:
            self.status = Status.FULL_HEALTH
        elif 75 <= percent < 100:
            self.status = Status.INJURED
        elif 25 <= percent < 75:
            self.status = Status.BADLY_WOUNDED
        elif 0 < percent < 25:
            self.status = Status.NEAR_DEAD
        else:
            self.status = Status.DEAD

    def set_position(self, position: Position = Position()) -> None:
        """
        >>> dragon = Character(name='Red', position=Position(0, 0))
        >>> dragon.position_change(right=1)
        >>> dragon.position_get()
        Point(x=1, y=0)
        >>> dragon.position_change(down=1)
        >>> dragon.position_get()
        Point(x=1, y=1)
        >>> dragon.position_change(left=2)
        >>> dragon.position_get()
        Point(x=0, y=1)
        >>> dragon.position_change(up=2)
        >>> dragon.position_get()
        Point(x=1, y=1)
        """
        current_position = self.position_get()
        x = current_position.x
        y = current_position.y

        if x > Config.BORDER_X_MAX:
            x = Config.BORDER_X_MAX

        if x < Config.BORDER_X_MIN:
            x = Config.BORDER_X_MIN

        if y > Config.BORDER_Y_MAX:
            y = Config.BORDER_Y_MAX

        if y < Config.BORDER_Y_MIN:
            y = Config.BORDER_Y_MIN

        super().position_set(Position(x, y))


class CharacterClass(Enum):
    WARRIOR = 'Warrior'
    DRAGON = 'Dragon'


class Dragon(Character):
    HIT_POINTS_MIN = 100
    HIT_POINTS_MAX = 150
    CHARACTER_CLASS = CharacterClass.DRAGON


class Hero(Character):
    HIT_POINTS_MIN = 200
    HIT_POINTS_MAX = 250
    DAMAGE_MIN = 1
    DAMAGE_MAX = 15
    GOLD_MIN = 0
    GOLD_MAX = 0
    CHARACTER_CLASS = CharacterClass.WARRIOR


def run():
    dragon = Dragon(name='Wawelski')
    hero = Hero(name='Jan Twardowski')

    turn = 1

    while dragon.is_alive() and hero.is_alive():
        print(f'\nTurn: {turn}')

        dmg = dragon.make_damage()
        hero.take_damage(dmg)

        if hero.is_alive():
            dmg = hero.make_damage()
            dragon.take_damage(dmg)

        if dragon.is_dead():
            drop = dragon.get_drop()
            hero.gold += drop['gold']
            print(f'{hero.name} now has: {hero.gold} gold')

        turn += 1


if __name__ == '__main__':
    run()
