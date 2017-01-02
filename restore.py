# coding: utf-8
# TODO-me remove external library
import random
import math
import matplotlib.pyplot as plt
import sys


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    @staticmethod
    def make_vector(a, b):
        return Point(b.x - a.x, b.y - a.y)


def angle(a, b):
    return math.fabs(math.atan2(a.x * b.y - a.y * b.x, (a.x * b.x + a.y * b.y)))


def dist(A, B):
    return math.hypot(A.x - B.x, A.y - B.y)


def checkTriangle(points):
    a = points[0]
    b = points[1]
    c = points[2]
    vector_a = Point.make_vector(a, b)
    vector_b = Point.make_vector(a, c)
    vector_c = Point.make_vector(c, b)
    if dist(a, b) < DIST or dist(a, c) < DIST or dist(b, c) < DIST:
        return False
    if angle(vector_a, vector_b) < ANGLE_rad or angle(vector_a, vector_c) < ANGLE_rad or angle(vector_c,
                                                                                               vector_b) < ANGLE_rad:
        return False
    return True


# Инициализация всех параметров.
# TODO-me включить release
DEBUG = 123
RELEASE = 124
filename = 'image.pgm'
N = 50
M = 50
MODE = DEBUG
DIST = 10
ANGLE_deg = 30
ANGLE_rad = math.radians(ANGLE_deg)
STD_P = 0.1
pic = []
for x in range(N):
    pic.append([0] * M)


# Чтение картинки.
try:
    filename = sys.argv[1]
except IndexError:
    P = STD_P

# Рисование треугольника, отладка.
# plt.imshow(pic)
# plt.show()










