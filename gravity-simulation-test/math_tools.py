import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return self.x**2 + self.y**2

    def unitVector(self):
        mag = self.magnitude()
        if (mag != 0):
            return Vector2D(self.x / mag, self.y / mag)
        else:
            return Vector2D()

    # operator functions
    def add(self, right):
        return Vector2D(self.x + right.x, self.y + right.y)
    
    def subtract(self, right):
        return Vector2D(self.x - right.x, self.y - right.y)
    
    def dot(self, right):
        return ((self.x * right.x) + (self.y + right.y))

    def scalarMultiply(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def contains(self, point):
        return (point.x >= self.x - self.w and
            point.x <= self.x + self.w and
            point.y >= self.y - self.h and
            point.y <= self.y + self.h)

    def intersects(self, range):
        return not (range.x - range.w > self.x + self.w or
            range.x + range.w < self.x - self.w or
            range.y - range.h > self.y + self.h or
            range.y + range.h < self.y - self.h)


class Ring:
    def __init__(self, x , y, r):
        self.x = x
        self.y = y
        self.r = r
        self.rSquared = r * r

    def intersects(self, range):
        xDist = abs(range.x - self.x)
        yDist = abs(range.y - self.y)

        w = range.w / 2
        h = range.h /2

        edges = math.pow((xDist - w), 2) + math.pow((yDist - h), 2)

        # No intersection
        if (xDist > (self.r + w) or yDist > (self.r + h)):
            return False
        
        # Intersection within the circle
        if (xDist <= w or yDist <= h):
            return True
        
        # Intersection on the edge of the circle
        return edges <= self.rSquared

    def contains(self, point):
        d = math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2)
        return d <= self.rSquared


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)