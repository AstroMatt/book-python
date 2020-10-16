"""
>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)

>>> pt.notexisting = 10
Traceback (most recent call last):
    ...
PermissionError: Cannot set other attributes than x,y,z

>>> pt.x = 10
>>> pt.y = 20
>>> pt.z = 30

>>> pt.x, pt.y, pt.z
(10, 20, 30)
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x,y,z')
        return super().__setattr__(name, value)
