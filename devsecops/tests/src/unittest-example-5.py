import unittest
from typing import Union


class Rectangle:
    def __init__(self, bok_a: Union[float, int], bok_b: [float, int]) -> None:
        if not isinstance(bok_a, (float, int)) or bok_a <= 0:
            raise ValueError('Side A cannot be negative')

        if not isinstance(bok_b, (float, int)) or bok_b <= 0:
            raise ValueError('Side B cannot be negative')

        self.side_a = float(bok_a)
        self.side_b = float(bok_b)

    def area(self) -> float:
        return self.side_a * self.side_b

    def circumference(self) -> float:
        return 2 * (self.side_a + self.side_b)

    def __str__(self) -> str:
        return f'Rectangle(a={self.side_a}, b={self.side_b})'


class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(bok_a=10, bok_b=20)

    def test_create_rectangle(self):
        Rectangle(bok_a=5, bok_b=10)

    def test_create_rectangle_with_invalid_side(self):
        with self.assertRaises(ValueError):
            Rectangle(bok_a='a', bok_b=20)

        with self.assertRaises(ValueError):
            Rectangle(bok_a=20, bok_b='b')

        with self.assertRaises(ValueError):
            Rectangle(bok_a='b', bok_b='b')

    def test_create_rectangle_side_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(bok_a=0, bok_b=20)

        with self.assertRaises(ValueError):
            Rectangle(bok_a=20, bok_b=0)

        with self.assertRaises(ValueError):
            Rectangle(bok_a=0, bok_b=0)

    def test_create_rectangle_side_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(bok_a=-3, bok_b=20)

        with self.assertRaises(ValueError):
            Rectangle(bok_a=20, bok_b=-3)

        with self.assertRaises(ValueError):
            Rectangle(bok_a=-1, bok_b=-3)

    def test_create_rectangle_with_one_side(self):
        with self.assertRaises(TypeError):
            Rectangle(bok_a=0)

        with self.assertRaises(TypeError):
            Rectangle(bok_b=0)

    def test_create_rectangle_and_store_values(self):
        p = Rectangle(bok_a=5, bok_b=10)
        self.assertEqual(p.side_a, 5)
        self.assertEqual(p.side_b, 10)

    def test_create_rectangle_valid(self):
        self.assertEqual(self.rectangle.side_a, 10)
        self.assertEqual(self.rectangle.side_b, 20)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 200.0)

    def test_circumference(self):
        self.assertEqual(self.rectangle.circumference(), 60)

    def test_stringify_rectangle(self):
        self.assertEqual(str(self.rectangle), 'Rectangle(a=10.0, b=20.0)')


if __name__ == '__main__':
    unittest.main()
