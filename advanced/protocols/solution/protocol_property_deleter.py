"""
>>> pt = Point(x=1, y=2, z=3)
>>> pt.x. pt,y, pt.z
(1, 2, 3)
>>> del pt.position
>>> pt.x. pt,y, pt.z
(0, 0, 0)
"""


class Point:
    position = property()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @position.deleter
    def position(self):
        self.x = 0
        self.y = 0
        self.z = 0
