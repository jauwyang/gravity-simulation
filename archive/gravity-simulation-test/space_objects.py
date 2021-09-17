# ========= IMPORT MODULES =========
import math
from math_tools import Point, Vector2D, distance
import random

# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BARRIER, RADIUS, FPS, BLACK, WHITE, TIME_INTERVAL, G, COLOUR_MAP


MASS_VAL = 10

class Particle:
    # TODO: make the radius depend on the density of the particle (which will depend on the scale of the map)
    def __init__(self, xPos, yPos, xVel, yVel, radius = None):
        self.mass = MASS_VAL
        self.Pos = Point(xPos, yPos)
        self.Vel = Vector2D(xVel, yVel)
        self.density = None # TBD when radius implementation is added
        self.colour = WHITE
        if (radius == None):
            self.radius # TBD how to calculate in future
        else:
            self.radius = radius
    
    def updatePosition(self):
        self.Pos.x = self.Pos.x + self.Vel.x*TIME_INTERVAL
        self.Pos.y = self.Pos.y + self.Vel.y*TIME_INTERVAL
        
        # Barrier limit
        if BARRIER:
            if (self.Pos.x / SCALE) > WINDOW_WIDTH or (self.Pos.x / SCALE) < 0:
                self.Vel.x *= -1
            if (self.Pos.y / SCALE) > WINDOW_HEIGHT or (self.Pos.y / SCALE) < 0:
                self.Vel.y *= -1


    def intersects(self, otherP):
        d = distance(self.Pos.x, self.Pos.y, otherP.Pos.x, otherP.Pos.y)
        return (d <= self.radius + otherP.radius)
