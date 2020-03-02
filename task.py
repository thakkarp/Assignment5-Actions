import math


def getArea(radius):
    pi = math.pi
    area = pi * radius * radius
    return area


def getFirstAndLast(list):
    length = len(list)
    return [list[0], list[length - 1]]
