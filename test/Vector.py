from math import hypot


class Vector(object):
    """一个简单的二维向量"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。"""
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __str__(self):
        return 'Vector({},{})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
