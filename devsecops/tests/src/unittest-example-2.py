from unittest import TestCase


class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        values = [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need argument')

        if len(values) > 1:
            raise ValueError('Only one argument')

        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'


class TemperatureTest(TestCase):
    def test_creating_temperature(self):
        with self.assertRaises(ValueError):
            Temperature()

    def test_setting_temperature(self):
        temp = Temperature(10)
        self.assertEqual(temp.kelvin, 10)

    def test_temp_from_celsius(self):
        temp = Temperature(celsius=1)
        self.assertEqual(temp.kelvin, 274.15)

    def test_temp_from_fahrenheit(self):
        temp = Temperature(fahrenheit=1)
        self.assertAlmostEqual(temp.kelvin, 255.928, places=3)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Temperature(celsius=1, kelvin=1)

    def test_negative_kelvins(self):
        with self.assertRaises(ValueError):
            Temperature(kelvin=-1)

        with self.assertRaises(ValueError):
            Temperature(celsius=-274)

        with self.assertRaises(ValueError):
            Temperature(fahrenheit=-1000)

    def test_to_string(self):
        temp = Temperature(kelvin=10)
        self.assertEqual(str(temp), 'Temperature = 10 Kelvins')

        temp = Temperature(celsius=10)
        self.assertEqual(str(temp), 'Temperature = 283.15 Kelvins')
