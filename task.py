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
    dateDifference = 0
    if date1 == "Monday":
        d1 = 1
    if date1 == "Tuesday":
        d1 = 2
    if date1 == "Wednesday":
        d1 = 3
    if date1 == "Thursday":
        d1 = 4
    if date1 == "Friday":
        d1 = 5
    if date1 == "Saturday":
        d1 = 6
    if date1 == "Sunday":
        d1 = 7
    if date2 == "Monday":
        d2 = 1
    if date2 == "Tuesday":
        d2 = 2
    if date2 == "Wednesday":
        d2 = 3
    if date2 == "Thursday":
        d2 = 4
    if date2 == "Friday":
        d2 = 5
    if date2 == "Saturday":
        d2 = 6
    if date1 == "Sunday":
        d2 = 7
    if d1 > d2:
        dateDifference = d1 - d2
    else:
        dateDifference = d2 - d1
    return dateDifference
