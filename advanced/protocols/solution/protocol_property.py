"""
>>> pt = Point(x=1, y=2, z=3)
>>> pt.position
(1, 2, 3)
>>> del pt.position
>>> pt.position
(0, 0, 0)
>>> pt.position = (4, 5, 6)
Traceback (most recent call last):
    ...
PermissionError: Cannot modify values
"""


class Point:
    position = property()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @position.getter
    def position(self):
        return self._x, self._y, self._z

    @position.setter
    def position(self, new_value):
        raise PermissionError('Cannot modify values')

    @position.deleter
    def position(self):
        self._x = 0
        self._y = 0
        self._z = 0

