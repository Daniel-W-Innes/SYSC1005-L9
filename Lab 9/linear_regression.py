"""
SYSC 1005 Fall 2017 Lab 9, Parts 2 and 3
"""

def get_points():
    """

    :return:
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}


def read_points(filename):
    """
    >>> read_points("data.txt")

    :param filename:
    :return:
    """
    infile = open(filename, 'r')
    output = set()
    for line in infile:
        x, y = tuple(line.split())
        output.add((float(x), float(y)))
    infile.close()
    return output


def fit_line_to_points(points):
    """
    #>>> m, b = fit_line_to_points(fit_line_to_points(read_points(input(""))))
    >>> m, b = fit_line_to_points(read_points("data.txt"))
    >>> print("The best-fit line is y = " + str(m) + "x + " + str(b))

    :param points:
    :return line:
    """
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    for point in points:
        print(point)
        sumx = sumx + point[0]
        sumy = sumy + point[1]
        sumxx = sumxx + point[0] ** 2
        sumxy = sumxy + point[0] * point[1]
    return ((sumx * sumy - len(points) * sumxy) / (sumx * sumx - len(points) * sumxx),
            (sumx * sumxy - sumxx * sumy) / (sumx * sumx - len(points) * sumxx))


def read_and_print_lines():
    infile = open('data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()


if __name__ == "__main__":
    m, b = fit_line_to_points(get_points())
    print("The best-fit line is y = " + str(m) + "x + " + str(b))
