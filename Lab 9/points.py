# point1 = [1.0, 2.0]
# print(point1)
# point1.append(3.0)
# print(point1)
# point1.pop(0)
# print(point1)
# point1.pop()
# print(point1)
# point1 = (1.0, 2.0)
# print(point1)
# print(type(point1))
# x = point1[0]
# y = point1[1]
# print(x)
# print(y)
# point2 = (4.0, 6.0)
# x, y = point2
# print(x)
# print(y)
import math


def distance(pt1, pt2):
    """
    >>> point1 = (1.0, 2.0)
    >>> point2 = (4.0, 6.0)
    >>> distance(point1, point2)
    5.0

    :param pt1:
    :param pt2:
    :return distance:
    """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)