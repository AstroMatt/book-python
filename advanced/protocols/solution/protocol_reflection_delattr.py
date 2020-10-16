"""
>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)

>>> del pt.x
Traceback (most recent call last):
    ...
PermissionError: Cannot delete attributes

>>> del pt.notexisting
Traceback (most recent call last):
    ...
PermissionError: Cannot delete attributes
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError('Cannot delete attributes')
