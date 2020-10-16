"""
>>> t = Temperature()
>>> t.kelvin = 1
>>> t.kelvin
1
>>> t.kelvin = -1
Traceback (most recent call last):
    ...
ValueError: Negative temperature
"""


class Kelvin:
    def __get__(self, parent, parent_type):
        return parent._value

    def __set__(self, parent, new_value):
        if new_value < 0:
            raise ValueError('Negative temperature')
        else:
            parent._value = new_value


class Temperature:
    kelvin = Kelvin()
