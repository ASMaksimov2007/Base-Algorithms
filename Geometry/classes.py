import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def radius(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def angle(self, precision=9):
        return round(math.degrees(math.acos(self.y / self.radius())), precision)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def dist(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __rmul__(self, other):
        return Vector(self.x * k, self.y * k)

    def normalize(self):
        return Vector(x / self.length(), y / self.length())


def vector_by_points(point1, point2):
    return Vector(point2.x - point1.x, point2.y - point1.y)


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def contains(self, point):
        return self.a * point.x + self.b * point.y + self.c == 0

    def get_equation_result(self, x, y):
        return self.a * x + self.b * y + self.c

    def sign(self, x, y):
        if self.get_equation_result(self, x, y) > 0:
            return 1
        elif self.get_equation_result(self, x, y) < 0:
            return -1
        return 0

    def perpendicular(self, point):
        return Line(-self.b, self.a, -self.a * point.y + self.b * point.x)

    def intersection(self, other):
        def det(a, b, c, d):
            return a * d - b * c

        zn = det(self.a, self.b, other.a, other.b)

        if zn == 0:
            return (None, None)

        result = Point(0, 0)
        print(zn)

        result.x = -det(self.c, self.b, other.c, other.b) / zn
        result.y = -det(self.a, self.c, other.a, other.c) / zn

        return result

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"


def points_to_normal_line(point1, point2):
    a = point2.y - point1.y
    b = point1.x - point2.x
    c = -a * point1.x - b * point1.y
    return Line(a, b, c)


class Segment:
    def __init__(self, point1, point2):
        self.start = point1
        self.finish = point2


def intersect(segm1, segm2):
    pass
