"""
>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)

>>> pt.notexisting = 10
Traceback (most recent call last):
    ...
PermissionError: Cannot set other attributes than x,y,z

>>> pt.x = 10
Traceback (most recent call last):
    ...
PermissionError: Cannot modify existing attributes
>>> pt.y = 20
Traceback (most recent call last):
    ...
PermissionError: Cannot modify existing attributes
>>> pt.z = 30
Traceback (most recent call last):
    ...
PermissionError: Cannot modify existing attributes
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x,y,z')
        if hasattr(self, name):
            raise PermissionError('Cannot modify existing attributes')
        return super().__setattr__(name, value)
