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
        self.end = point2

    def line(self):
        return points_to_normal_line(self.start, self.end)

    def contains(self, point):
        if self.line().contains(point):
            if any((max(self.start.y, self.end.y) < point.y,
                    min(self.start.y, self.end.y) > point.y,
                    max(self.start.x, self.end.x) < point.x,
                    min(self.start.x, self.end.x) > point.x,
                    )):
                return False
            else:
                return True
        else:
            return False

    def perpendicular(self, point):
        return self.line().perpendicular(point)

    def vector(self):
        return vector_by_points(self.start, self.end)

    def length(self):
        return dist(self.start, self.end)


def vector_to_ray(vector):
    return Ray(Point(0, 0), Point(vector.x, vector.y))


class Ray:
    def __init__(self, point1, point2):
        self.start = point1
        self.direction = point2

    def line(self):
        return points_to_normal_line(self.start, self.direction)

    def vector(self):
        return vector_by_points(self.start, self.direction)

    def perpendicular(self, point):
        return self.line().perpendicular(point)

    def contains(self, point):
        return all((
            self.line().contains(point),
            (point.x - self.start.x) * (self.direction.x - self.start.x) >= 0,
            (point.y - self.start.y) * (self.direction.y - self.start.y) >= 0,
        ))
