"""
>>> pt = Point(x=1, y=2, z=3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)
>>> pt.position
(1, 2, 3)
"""


class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.getter
    def position(self):
        return self.x, self.y, self.z
