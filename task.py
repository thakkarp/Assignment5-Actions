import math


def getArea(radius):
    pi = math.pi
    area = pi * radius * radius
    return area


def getFirstAndLast(list):
    length = len(list)
    return [list[0], list[length - 1]]


def getNumDays(date1, date2):
    d1 = 0
    d2 = 0
    diff = 0
    if date1 == "Monday":
        d1 = 1
    if date1 == "Tuesday":
        d1 = 2
    if date2 == "Monday":
        d2 = 1
    if date2 == "Tuesday":
        d2 = 2
    if d1 > d2:
        diff = (d1 - d2)
    else:
        diff = (d2 - d1)
    return diff
