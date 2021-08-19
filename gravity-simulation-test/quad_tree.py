from math_tools import Rectangle, Point
import pygame
import random
from config import SCALE

# https://www.youtube.com/watch?v=OJxEcs0w_kE

class QuadTree:
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        ne = Rectangle(x + (w / 2), y - (h / 2), w/2, h/2)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - (w / 2), y - (h / 2), w/2, h/2)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + (w / 2), y + (h / 2), w/2, h/2)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - (w / 2), y + (h / 2), w/2, h/2)
        self.southwest = QuadTree(sw, self.capacity)
        self.divided = True

    def insert(self, point):
        # point.Pos is to accomodate the Particle class
        if (not self.boundary.contains(point.Pos)):
            return False

        if ((len(self.points) < self.capacity) and not self.divided):
            self.points.append(point)
            return True
        else:
            if (not self.divided):
                self.subdivide()
                while self.points:
                    part = self.points.pop()
                    self.insert(part)

            if (self.northeast.insert(point)):
                return True
            elif (self.northwest.insert(point)):
                return True
            elif (self.southeast.insert(point)):
                return True
            elif (self.southwest.insert(point)):
                return True
    
    def query(self, range, found = None):
        if (not found):
            found = []
        if (not range.intersects(self.boundary)):
            # empty array
            return found
        else:
            for p in self.points:
                if (range.contains(p.Pos)):
                    found.append(p)
                    
            if (self.divided):
                self.northeast.query(range, found)
                self.northwest.query(range, found)
                self.southeast.query(range, found)
                self.southwest.query(range, found)
        return found

    def draw(self, window):

        pygame.draw.rect(window, (0, 255, 0), (self.boundary.x - self.boundary.w, self.boundary.y - self.boundary.h, (self.boundary.w * 2)  / SCALE, (self.boundary.h * 2)/ SCALE), width = 1)
        # print(len(self.points))
        # pygame.draw.rect(window, (0, 255, 0), (self.boundary.x, self.boundary.y, (self.boundary.x + self.boundary.w) / SCALE, (self.boundary.y + self.boundary.h) / SCALE), width = 2)
        if (self.divided):
            self.northeast.draw(window)
            self.northwest.draw(window)
            self.southeast.draw(window)
            self.southwest.draw(window)

    def height(self):
        if (self.divided):
            neDepth = self.northeast.height()
            nwDepth = self.northwest.height()
            seDepth = self.southeast.height()
            swDepth = self.southwest.height()
            biggestDepth = 0
            if neDepth > biggestDepth:
                biggestDepth = neDepth
            if nwDepth > biggestDepth:
                biggestDepth = nwDepth
            if seDepth > biggestDepth:
                biggestDepth = seDepth
            if swDepth > biggestDepth:
                biggestDepth = swDepth
            return biggestDepth + 1
        else:
            return 0