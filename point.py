from numpy import matrix
from math import cos, sin

"""2D point geometry library"""


def column_vec(point):
    """return the column vector for a point"""
    (x, y) = point
    return matrix(([x], [y]))


def aspoint(column_vec):
    """convert a column vector to a point"""
    [[x], [y]] = column_vec.tolist()
    return x, y


def shear_x(point, factor):
    """
    shear a point parallel to the x axis
    https://en.wikipedia.org/wiki/Shear_matrix
    """
    shear = matrix(
        ([1, factor],
         [0, 1])
    )

    return aspoint(shear * column_vec(point))


def rotate(point, angle):
    """
    rotate a given point about the origin
    https://en.wikipedia.org/wiki/Rotation_matrix
    """
    rot = matrix(
        ([cos(angle), -sin(angle)],
         [sin(angle), cos(angle)])
    )

    return aspoint(rot * column_vec(point))


def translate(point, x, y):
    """move (translate) a point by x and y"""
    (point_x, point_y) = point

    return point_x + x, point_y + y


class _max:
    """helper class to represent a MAX value (greater than anything)"""
    def __lt__(self, other): return False
    def __gt__(self, other): return True


class _min:
    """helper class to represent a MIN value (less than anything)"""
    def __lt__(self, other): return True
    def __gt__(self, other): return False


MAX, MIN = _max(), _min()


def bbox(points):
    """find the bounding box of a set of points"""
    min_x = MAX
    min_y = MAX
    max_x = MIN
    max_y = MIN

    for point in points:
        (x, y) = point

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return min_x, min_y, max_x, max_y
