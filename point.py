from numpy import matrix
from math import cos, sin


def rotate(point, angle):
    rot = matrix(
        ([cos(angle), -sin(angle)],
         [sin(angle), cos(angle)])
    )

    (x, y) = point
    [[x], [y]] = (rot * matrix(([x], [y]))).tolist()

    return x, y


def translate(point, x, y):
    (point_x, point_y) = point

    return point_x + x, point_y + y


class _max:
    def __lt__(self, other): return False

    def __gt__(self, other): return True


class _min:
    def __lt__(self, other): return True

    def __gt__(self, other): return False


MAX, MIN = _max(), _min()


def bbox(points):
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
