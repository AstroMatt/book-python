"""
* Assignment: Dragon (version alpha)
* Filename: dragon_alpha.py
* Complexity: medium
* Lines of code: 100 lines
* Time: 60 min, then 90 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

English:
    1. Dragon has (attributes):
        a. name
        b. position `x` on the screen
        c. position `y` on the screen
        d. texture file name, default `img/dragon/alive.png`
        e. health points, default random `int` in range from 50 to 100
    2. Dragon can (methods):
        a. have position set to any place on the screen
        b. make damage in range from 5 to 20
        c. take damage
        d. move in any direction by specified value
    3. Assume left-top screen corner as a initial coordinates position:
        a. going right add to `x`
        b. going left subtract from `x`
        c. going up subtract from `y`
        d. going down add to `y`
    4. When dragon receives damage:
        a. print name of the Dragon
        b. health points which left
    5. When health points drop to, and below zero:
        a. Dragon is dead
        b. Set object status to dead
        c. Print `XXX is dead`, where XXX is the name of the dragon
        d. Change texture file name to  `img/dragon/dead.png`
        e. Print position where dragon died
        f. Return gold dropped by Dragon (random in range from 1 to 100)
        g. Dragon cannot take any more damage
        h. Dragon cannot make any more damage
        i. Dragon cannot move or have position set
    6. Run the game:
        a. Create dragon at x=50, y=120 position and name it "Wawelski"
        b. Set new position to x=10, y=20
        c. Move dragon left by 10 and down by 20
        d. Move dragon left by 10 and right by 15
        e. Move dragon right by 15 and up by 5
        f. Move dragon down by 5
        g. Dragon makes damage
        h. Make 10 points damage to the dragon
        i. Make 5 points damage to the dragon
        j. Make 3 points damage to the dragon
        k. Make 2 points damage to the dragon
        l. Make 15 points damage to the dragon
        m. Make 25 points damage to the dragon
        n. Make 75 points damage to the dragon
    7. Non-functional requirements:
        a. This is a simulation of development process
        b. Trainer act as Product Owner with little technical knowledge
        c. You are the software engineer who need to decide and live with
        consequences of your choices
        d. Task is a narrative story telling to demonstrate OOP and good
        engineering practices
        e. Calculated last position of the game should be x=20, y=40
        f. You can introduce new fields, methods, functions, variables,
        constants, classes, objects, whatever you want
        g. Don't use modules form outside the Python Standard Library
        h. Task is business requirements specification, not a technical
        documentation, i.e. "what Dragon has to do, not how to do it"
        i. You don't have to keep order of business specification while
        writing code
        j. This is `alpha` version, so no new functionality like negative
        position checking etc.
        k. Do not read solution or any future iterations of this exercise.
        l. If you read future tasks, you will spoil fun and what is the most
        important: learning.

Polish:
    1. Smok ma (atrybuty):
        a. nazwę
        b. pozycję `x` na ekranie
        c. pozycję `y` na ekranie
        d. nazwę pliku tekstury, domyślnie `img/dragon/alive.png`
        e. punkty życia, domyślnie losowy `int` z zakresu od 50 do 100
    2. Smok może (metody):
        a. być ustawiony w dowolne miejsce ekranu
        b. zadawać komuś losowe obrażenia z przedziału od 5 do 20
        c. otrzymywać obrażenia
        d. być przesuwany o zadaną liczbę punktów w którymś z kierunków
    3. Przyjmij górny lewy róg ekranu za punkt początkowy:
        a. idąc w prawo dodajesz `x`
        b. idąc w lewo odejmujesz `x`
        c. idąc w górę odejmujesz `y`
        d. idąc w dół dodajesz `y`
    4. Gdy smok otrzymuje obrażenia:
        a. wypisz nazwę smoka,
        b. pozostałe punkty życia
    5. Kiedy punkty życia Smoka spadną do, lub poniżej zera:
        a. Smok jest martwy
        b. Ustaw status obiektu na dead
        c. Wypisz napis `XXX is dead` gdzie XXX to nazwa smoka
        d. Zmień nazwę pliku tekstury na `img/dragon/dead.png`
        e. Wypisz pozycję gdzie smok zginął
        f. Zwróć ile złota smok wyrzucił (losowa 1-100)
        g. Nie można zadawać mu obrażeń
        h. Smok nie może zadawać obrażeń
        i. Smok nie może się poruszać
    6. Przeprowadź grę:
        a. Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
        b. Ustaw nową pozycję na x=10, y=20
        c. Przesuń smoka w lewo o 10 i w dół o 20
        d. Przesuń smoka w lewo o 10 i w prawo o 15
        e. Przesuń smoka w prawo o 15 i w górę o 5
        f. Przesuń smoka w dół o 5
        g. Smok zadaje obrażenia
        h. Zadaj 10 obrażeń smokowi
        i. Zadaj 5 obrażeń smokowi
        j. Zadaj 3 obrażeń smokowi
        k. Zadaj 2 obrażeń smokowi
        l. Zadaj 15 obrażeń smokowi
        m. Zadaj 25 obrażeń smokowi
        n. Zadaj 75 obrażeń smokowi
    7. Wymagania niefunkcjonalne:
        a. Zadanie jest symulacją procesu developmentu
        b. Trener zachowuje się jak Product Owner z niewielką techniczną wiedzą
        c. Ty jesteś inżynierem oprogramowania, który musi podejmować
        decyzje i ponosić ich konsekwencje
        d. Zadanie jest tylko narracją do demonstracji OOP i dobrych praktyk
        programowania
        e. Wyliczona pozycja Smoka na końcu gry powinna być x=20, y=40
        f. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne,
        stały, klasy, obiekty, co tylko chcesz
        g. Nie korzystaj z modułów spoza standardowej biblioteki Pythona
        h. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją
        techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
        i. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
        j. Jest to wersja `alpha` więc bez dodatkowych funkcjonalności (np.
        sprawdzanie koordynatów, wychodzenia poza planszę itp.)
        k. Nie przeglądaj rozwiązań ani treści kolejnych (przyszłych) części
        zadania.
        l. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i co
        najważniejsze naukę.

Hints:
    * `from random import randint`
    * `randint` returns random integer between a and b (including both ends!)
    point

Tests:
    >>> from random import seed; seed(0)
    >>> dragon = Dragon(name='Wawelski', position_x=50, position_y=120)
    >>> dragon @ Point(x=10, y=20)
    >>> dragon >> Direction(left=10, down=20)
    >>> dragon >> Direction(left=10, right=15)
    >>> dragon >> Direction(right=15, up=5)
    >>> dragon >> Direction(down=5)
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

    TODO: dragon < Damage(...)
    TODO: dragon > Damage(...)
    TODO: dragon[...] -> items
    TODO: hero[gold] = dragon[gold]
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from random import randint
from typing import Callable, NoReturn, Optional, TypedDict, overload
from unittest import TestCase


def if_alive(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'HasHealth', *args, **kwargs) -> Optional[Callable]:
        if instance.is_alive():
            return method(instance, *args, **kwargs)
        else:
            raise instance.IsDead

    return wrapper


def if_dead(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(instance: 'HasHealth', *args, **kwargs) -> Optional[Callable]:
        if instance.is_dead():
            return method(instance, *args, **kwargs)

    return wrapper


@dataclass(frozen=True)
class Point(metaclass=ABCMeta):
    x: int = 0
    y: int = 0


@dataclass(frozen=True)
class Direction(metaclass=ABCMeta):
    left: int = 0
    right: int = 0
    up: int = 0
    down: int = 0


@dataclass
class CanMove(metaclass=ABCMeta):
    _position: Point = Point()

    @property
    def position(self) -> Point:
        return self._position

    @if_alive
    def __matmul__(self, point: Point) -> None:
        """dragon @ Position(x,y)"""
        self._position = point

    @if_alive
    def __rshift__(self, direction: Direction) -> None:
        """dragon >> Direction(left, right, up, down)"""
        new_x: int = self._position.x + direction.right - direction.left
        new_y: int = self._position.y + direction.down - direction.up
        return self @ Point(new_x, new_y)


class Status(Enum):
    ALIVE: str = 'alive'
    DEAD: str = 'dead'


class HasHealth(metaclass=ABCMeta):
    HEALTH_MIN: int
    HEALTH_MAX: int
    _health: int = 0
    _status: str

    class IsDead(Exception):
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._health = randint(cls.HEALTH_MIN, cls.HEALTH_MAX)
        cls._update_status(cls)

    def _update_status(self) -> None:
        if self._health > 0:
            self._status = Status.ALIVE
        else:
            self._status = Status.DEAD

    def is_dead(self) -> bool:
        return self._status is Status.DEAD

    def is_alive(self) -> bool:
        return self._status is not Status.DEAD

    @if_alive
    def take_damage(self, damage) -> Optional[NoReturn]:
        self._health -= damage
        self._update_status()
        if self.is_dead():
            self._make_dead()
            raise self.IsDead

    def _make_dead(self):
        self._health = 0
        self._update_status()
        self._on_dead()

    @abstractmethod
    def _on_dead(self):
        raise NotImplementedError


class Drop(TypedDict):
    gold: int
    position: Point


class CanAttack(metaclass=ABCMeta):
    DAMAGE_MIN: int
    DAMAGE_MAX: int

    @if_alive
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


class HasItems(metaclass=ABCMeta):
    GOLD_MIN: int
    GOLD_MAX: int
    _gold: int = 0

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._gold = randint(cls.GOLD_MIN, cls.GOLD_MAX)

    @if_dead
    def get_drop(self) -> Drop:
        gold, self._gold = self._gold, 0
        return Drop(gold=gold, position=self.position)


class Critter:
    _name: str = None
    _texture: str = None

    def __init__(self, name, position_x: int = 0, position_y: int = 0):
        self._name = name
        self._texture = self.TEXTURE_ALIVE
        self @ Point(position_x, position_y)

    def __str__(self) -> str:
        return self._name

    def __format__(self, name: str) -> str:
        if name == 'name':
            return str(self._name)
        elif name == 'position':
            return str(self._position)
        elif name == 'health':
            return str(self._health)
        else:
            return str(self._name)

    def _on_dead(self) -> None:
        self._texture = self.TEXTURE_DEAD



class Dragon(Critter, HasHealth, CanMove, CanAttack, HasItems):
    TEXTURE_DEAD: str = 'img/dragon/dead.png'
    TEXTURE_ALIVE: str = 'img/dragon/alive.png'
    DAMAGE_MIN: int = 5
    DAMAGE_MAX: int = 20
    HEALTH_MIN: int = 50
    HEALTH_MAX: int = 100
    GOLD_MIN: int = 1
    GOLD_MAX: int = 100


class CanMoveTest(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_position_default(self):
        self.assertEqual(self.alive.position, Point(x=0, y=0))

    def test_position_init(self):
        dragon = Dragon('Alive', position_x=1, position_y=2)
        self.assertEqual(dragon.position, Point(x=1, y=2))

    def test_position(self):
        self.assertEqual(self.alive.position, Point(x=0, y=0))

    def test_position_set(self):
        self.alive @ Point(x=1, y=2)
        self.assertEqual(self.alive.position, Point(x=1, y=2))
        with self.assertRaises(self.dead.IsDead):
            self.dead @ Point(x=1, y=2)

    def test_position_change_right(self):
        self.alive >> Direction(right=1)
        self.assertEqual(self.alive.position, Point(x=1, y=0))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(right=1)

    def test_position_change_left(self):
        self.alive >> Direction(left=1)
        self.assertEqual(self.alive.position, Point(x=-1, y=0))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(left=1)

    def test_position_change_down(self):
        self.alive >> Direction(down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=1))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(down=1)

    def test_position_change_up(self):
        self.alive >> Direction(up=1)
        self.assertEqual(self.alive.position, Point(x=0, y=-1))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(up=1)

    def test_position_change_horizontal(self):
        self.alive >> Direction(right=1, left=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(right=1, left=1)

    def test_position_change_vertical(self):
        self.alive >> Direction(up=1, down=1)
        self.assertEqual(self.alive.position, Point(x=0, y=0))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(up=1, down=1)

    def test_position_matmul(self):
        self.alive @ Point(x=1, y=2)
        self.assertEqual(self.alive.position, Point(x=1, y=2))
        with self.assertRaises(self.dead.IsDead):
            self.dead @ Point(x=1, y=2)

    def test_position_rshift(self):
        self.alive >> Direction(right=1, down=2)
        self.assertEqual(self.alive.position, Point(x=1, y=2))
        with self.assertRaises(self.dead.IsDead):
            self.dead >> Direction(right=1, down=2)


class CanDieTest(TestCase):
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
            self.alive._health = 1
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
        self.alive._health = 1
        self.assertEqual(f'{self.alive:name}', 'Alive')
        self.assertEqual(f'{self.alive:position}', 'Point(x=0, y=0)')
        self.assertEqual(f'{self.alive:health}', '1')

    def test_texture(self):
        self.assertEqual(self.alive._texture, Dragon.TEXTURE_ALIVE)
        self.assertEqual(self.dead._texture, Dragon.TEXTURE_DEAD)

    def test_gold(self):
        self.assertIn(self.alive._gold, range(Dragon.GOLD_MIN, Dragon.GOLD_MAX + 1))

    def test_get_drop(self):
        drop = self.dead.get_drop()
        expected_position = Point(x=0, y=0)
        expected_gold = range(Dragon.GOLD_MIN, Dragon.GOLD_MAX + 1)
        self.assertEqual(drop['position'], expected_position)
        self.assertIn(drop['gold'], expected_gold)
        self.assertEqual(self.dead._gold, 0)

    def test_make_dead(self):
        dragon = self.alive
        dragon._make_dead()
        self.assertTrue(dragon.is_dead())
        self.assertEqual(dragon._texture, Dragon.TEXTURE_DEAD)
        self.assertEqual(dragon._status, Status.DEAD)
        self.assertEqual(dragon._health, 0)

    def test_take_damage(self):
        self.alive._health = 2
        self.alive.take_damage(1)
        self.assertEqual(self.alive._health, 1)
        with self.assertRaises(self.dead.IsDead):
            self.dead.take_damage(1)
        with self.assertRaises(self.dead.IsDead):
            self.alive._health = 1
            self.alive.take_damage(1)


class CanAttack(TestCase):
    def setUp(self):
        self.alive = Dragon('Alive')
        self.dead = Dragon('Dead')
        self.dead._make_dead()

    def test_make_damage(self):
        expected = range(Dragon.DAMAGE_MIN, Dragon.DAMAGE_MAX + 1)
        self.assertIn(self.alive.make_damage(), expected)
        with self.assertRaises(self.dead.IsDead):
            self.dead.make_damage()
