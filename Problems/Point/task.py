from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, a):
        return sqrt((self.x - a.x) ** 2 + (self.y - a.y) ** 2)
