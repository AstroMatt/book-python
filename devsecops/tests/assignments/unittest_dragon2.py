from unittest import TestCase

BORDER_X_MAX = 1024
BORDER_X_MIN = 0
BORDER_Y_MAX = 768
BORDER_Y_MIN = 0


class Dragon:
    def __init__(self, name, x: int = 0, y: int = 0) -> None:
        self.name = name
        self.x = x
        self.y = y

    def set_position(self, x: int, y: int) -> None:
        if not isinstance(x, int):
            raise TypeError
        if not isinstance(y, int):
            raise TypeError

        if x > BORDER_X_MAX:
            x = BORDER_X_MAX

        if x < BORDER_X_MIN:
            x = BORDER_X_MIN

        y = min(max(y, BORDER_Y_MIN), BORDER_Y_MAX)

        self.x = x
        self.y = y

    def move(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None:
        x = self.x + right - left
        y = self.y + down - up
        self.set_position(x, y)


class DragonTest(TestCase):

    def setUp(self) -> None:
        self.dragon = Dragon(name='Wawelski', x=0, y=0)

    def test_create_dragon(self):
        dragon = Dragon(name='Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_create_dragon_at_position(self):
        dragon = Dragon(name='Wawelski', x=10, y=20)
        self.assertEqual(dragon.x, 10)
        self.assertEqual(dragon.y, 20)

    def test_set_position(self):
        self.dragon.set_position(x=10, y=20)
        self.assertEqual(self.dragon.x, 10)
        self.assertEqual(self.dragon.y, 20)

    def test_set_position_out_of_border(self):
        self.dragon.set_position(x=BORDER_X_MAX+1, y=0)
        self.assertEqual(self.dragon.x, BORDER_X_MAX)

        self.dragon.set_position(x=BORDER_X_MIN-1, y=0)
        self.assertEqual(self.dragon.x, BORDER_X_MIN)

        self.dragon.set_position(x=0, y=BORDER_Y_MAX+1)
        self.assertEqual(self.dragon.y, BORDER_Y_MAX)

        self.dragon.set_position(x=0, y=BORDER_Y_MIN-1)
        self.assertEqual(self.dragon.y, BORDER_Y_MIN)

    def test_move_sequential(self):
        self.dragon.move(left=10)
        self.assertEqual(self.dragon.x, 0)

        self.dragon.move(right=10)
        self.assertEqual(self.dragon.x, 10)

    def test_move_parallel(self):
        self.dragon.set_position(100, 100)

        self.dragon.move(left=10, right=20)
        self.assertEqual(self.dragon.x, 110)

        self.dragon.move(up=10, down=20)
        self.assertEqual(self.dragon.y, 110)

    def test_set_position_invalid_type(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position(x=1.5, y=0)
        with self.assertRaises(TypeError):
            self.dragon.set_position(x=0, y=1.5)
        with self.assertRaises(TypeError):
            self.dragon.set_position((1, 1), y=0)
        with self.assertRaises(TypeError):
            self.dragon.set_position(x=1, y=(1, 1))

