"""
>>> pt = Point(x=1, y=2, z=3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)
>>> pt.position = (4, 5, 6)
Traceback (most recent call last):
    ...
PermissionError: Cannot modify values
"""


class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.setter
    def position(self, new_value):
        raise PermissionError('Cannot modify values')
