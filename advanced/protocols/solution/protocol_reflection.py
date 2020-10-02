"""
>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)

>>> del pt.x
Traceback (most recent call last):
    ...
PermissionError: Cannot delete attibutes

>>> del pt.notexisting
Traceback (most recent call last):
    ...
PermissionError: Cannot delete attibutes

>>> pt.x = 10
Traceback (most recent call last):
    ...
PermissionError: Cannot modify existing attributes

>>> pt.notexisting = 10
Traceback (most recent call last):
    ...
PermissionError: Cannot set other attributes than x,y,z
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError('Cannot delete attibutes')

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x,y,z')
        if hasattr(self, name):
            raise PermissionError('Cannot modify existing attributes')
        return super().__setattr__(name, value)
