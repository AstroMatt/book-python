"""
>>> from random import seed; seed(0)
>>> wawelski = Dragon(name='Wawelski', x=50, y=120)
>>> wawelski.place(x=10, y=20)
>>> wawelski.move(left=10, down=20)
>>> wawelski.move(left=10, right=15)
>>> wawelski.move(right=15, up=5)
>>> wawelski.move(down=5)
>>> assert wawelski.attack() in range(5, 20)
>>> wawelski.hit(10)
>>> wawelski.hit(5)
>>> wawelski.hit(3)
>>> wawelski.hit(2)
>>> wawelski.hit(15)
>>> wawelski.hit(25)
>>> wawelski.hit(75)
Wawelski is dead
Gold 6
Position x=20 y=40
"""

from random import randint


class Dragon:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.health = randint(50, 100)
        self.texture = 'img/dragon/alive.png'
        self.x = x
        self.y = y

    def place(self, x, y):
        self.x = x
        self.y = y

    def move(self, left=0, down=0, right=0, up=0):
        self.x += right - left
        self.y += down - up

    def attack(self):
        return randint(5, 20)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = 'dead'
            self.texture = 'img/dragon/dead.png'
            print(f'{self.name} is dead')
            print(f'Gold {randint(1, 100)}')
            print(f'Position x={self.x} y={self.y}')
