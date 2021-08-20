# ========= IMPORT MODULES =========
import math
import matplotlib.cm
from math_tools import Point, Vector2D, distance
import random

# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BARRIER, RADIUS, FPS, BLACK, WHITE, TIME_INTERVAL, G, COLOUR_MAP




class Particle:
    # TODO: make the radius depend on the density of the particle (which will depend on the scale of the map)
    def __init__(self, mass, xPos, yPos, xVel, yVel, staticMovement = False, staticColour = False, staticRadius = False, density = None, radius = None, colour = None):
        self.mass = mass
        self.Pos = Point(xPos, yPos)
        self.Vel = Vector2D(xVel, yVel)
        self.Accel = Vector2D(0, 0)
        self.staticMovement = staticMovement
        self.staticColour = staticColour
        self.staticRadius = staticRadius
        self.collided = False
        self.colour = colour
        self.density = None # TBD when radius implementation is added
        if (radius == None):
            self.radius # TBD how to calculate in future
        else:
            self.radius = radius
    
    def updatePosition(self):
        if self.staticMovement:
            return

        self.Pos.x = self.Pos.x + self.Vel.x*TIME_INTERVAL + 0.5*self.Accel.x*(TIME_INTERVAL**2)
        self.Pos.y = self.Pos.y + self.Vel.y*TIME_INTERVAL + 0.5*self.Accel.y*(TIME_INTERVAL**2)
        
        # Barrier limit
        if BARRIER:
            if (self.Pos.x / SCALE) > WINDOW_WIDTH or (self.Pos.x / SCALE) < 0:
                self.Vel.x *= -1
            if (self.Pos.y / SCALE) > WINDOW_HEIGHT or (self.Pos.y / SCALE) < 0:
                self.Vel.y *= -1

    def updateVelocity(self):
        if self.staticMovement:
            return
        self.Vel.x = self.Vel.x + self.Accel.x*TIME_INTERVAL
        self.Vel.y = self.Vel.y + self.Accel.y*TIME_INTERVAL

    def updateAcceleration(self, space):
        if self.staticMovement:
            return

        self.Accel.x = 0
        self.Accel.y = 0

        # for particle in space.particles:
        #     if self.Pos.x == particle.Pos.x and self.Pos.y == particle.Pos.y:
        #         pass
        #     else:
        #         deltaX = abs(self.Pos.x - particle.Pos.x)
        #         deltaY = abs(self.Pos.y - particle.Pos.y)

        #         radius = math.sqrt((deltaX)**2 + (deltaY)**2)
        #         acceleration = G*particle.mass / (radius**2)
                
        #         xAcceleration = acceleration * deltaX / radius # similar triangles
        #         yAcceleration = acceleration * deltaY / radius

        #         if particle.Pos.x < self.Pos.x:
        #             xAcceleration *= -1
        #         if particle.Pos.y < self.Pos.y:
        #             yAcceleration *= -1

        #         self.Accel.x += xAcceleration
        #         self.Accel.y += yAcceleration


    def intersects(self, otherP):
        d = distance(self.Pos.x, self.Pos.y, otherP.Pos.x, otherP.Pos.y)
        return (d <= self.radius + otherP.radius)


    def changeColour(self, colour = None):
        if not colour:
            colourTuple = COLOUR_MAP(math.log(self.mass, 10) / 25)
            self.colour = tuple(255 * value for value in colourTuple)
        else:
            self.colour = colour



class Map:
    def __init__(self, randomStatus, numberOfPlanets, blackHole):
        self.randomStatus = randomStatus #true or false
        self.numberOfPlanets = numberOfPlanets
        self.blackHole = blackHole
        self.particles = []
        self.xCenterMass = 0
        self.yCenterMass = 0
        self.totalMass = 0

    def updateTotalMass(self):
        self.totalMass = 0
        for particle in self.particles:
            self.totalMass += particle.mass

    def updateCenterMass(self):
        self.xCenterMass = 0
        self.yCenterMass = 0
        for particle in self.particles:
            self.xCenterMass += particle.mass*particle.Pos.x
            self.yCenterMass += particle.mass*particle.Pos.y