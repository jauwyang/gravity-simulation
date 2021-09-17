# ======== IMPORT MODULES ========
from math_tools import distance
import pygame
import random
from space_objects import Particle
import math
import sys


# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK_HOLE, BARRIER, RADIUS, FPS, BLACK, WHITE, GREY, RED, GREEN, TIME_INTERVAL, ACCELERATION_VECTOR, VELOCITY_VECTOR, CENTER_OF_MASS

# ======== GLOBAL VARIABLES ========
CLOCK = pygame.time.Clock()
sys.setrecursionlimit(2500)
MASSES = []
PLANETS = 1500






# //////////////////
# ======== IMPORT MODULES ========
from quad_tree import QuadTree
from math_tools import Rectangle, Vector2D, Point, Ring

# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK
BOUNDARY = Rectangle(WINDOW_WIDTH * SCALE/2, WINDOW_HEIGHT * SCALE/2, WINDOW_WIDTH * SCALE / 2, WINDOW_HEIGHT * SCALE / 2)


# ///////////////////




def generateMasses():
     for i in range(PLANETS):
        xPos = random.randint(1, WINDOW_WIDTH * SCALE) 
        yPos = random.randint(1, WINDOW_HEIGHT * SCALE)
        xVel = random.randint(-1, 1)
        yVel = random.randint(-1, 1)

        r = RADIUS * SCALE # might change / based on how to calculate 

        if i != 0:
            j = 0
            while j < len(MASSES):
                if (distance(MASSES[j].Pos.x, MASSES[j].Pos.y, xPos, yPos) - (MASSES[j].radius + r) < 0):
                    xPos = random.randint(1, WINDOW_WIDTH * SCALE) 
                    yPos = random.randint(1, WINDOW_HEIGHT * SCALE)
                    j = -1
                j += 1
        MASSES.append(Particle(xPos, yPos, xVel, yVel, radius = r))


def redrawGameWindow(window):
    window.fill(GREY)
    # Run collision check
    checkCollision(window)
    for object in MASSES:
        xPos = round(object.Pos.x )
        yPos = round(object.Pos.y)
        pygame.draw.circle(window, object.colour, (xPos, yPos), object.radius / SCALE)
        # pygame.draw.circle(window, (255,0,255), (xPos, yPos), object.radius * 2.5, width = 1)
        object.colour = WHITE
        object.updatePosition()


    
    pygame.display.update()

def startup():

    generateMasses()
    # Initialize pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Main simulation loop
    run = True
    while run:
        # pygame.time.delay(10)
        CLOCK.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        redrawGameWindow(window)
    pygame.quit()






# ==================================

def doInelasticCollision(p1, p2):
    mass = p1.mass + p2.mass

    xPos = (p1.Pos.x + p2.Pos.x) / 2
    yPos = (p1.Pos.y + p2.Pos.y) / 2

    xVel = (p1.mass*p1.Vel.x + p2.mass*p2.Vel.x) / (p1.mass + p2.mass)
    yVel = (p1.mass*p1.Vel.y + p2.mass*p2.Vel.y) / (p1.mass + p2.mass)

    xAccel = (p1.Accel.x + p2.Accel.x) / 2
    yAccel = (p1.Accel.y + p2.Accel.y) / 2

    # Make 1st object the new object
    p1.mass = mass
    p1.Pos = Point(xPos, yPos)
    p1.Vel = Vector2D(xVel, yVel)
    p1.Accel = Vector2D(xAccel, yAccel)


    MASSES.remove(p2)


def doTypeOfCollision(p1, p2):


    # TODO: determine whether collision is inelastic vs elastic (bounce off or stick together)
    # doElasticCollison(p1, p2)
    p1.colour = (255,0,0)
    p2.colour = (255,0,0)
    # doInelasticCollision(p1, p2)



def checkCollision(window):
    # TODO: have to account for deleted particles in array
    # TODO: account for the "range" of a particle since it only works if ALL particles have the same radius
    qtree = QuadTree(BOUNDARY, 2)
    for particle in MASSES:
        qtree.insert(particle)
    qtree.draw(window)

    testRange = Rectangle(275, 275, 250, 250)
    pygame.draw.rect(window, (0,0,255), (testRange.x - testRange.w, testRange.y - testRange.h, (testRange.w * 2)  / SCALE, (testRange.h * 2)/ SCALE), width = 1)
    list = qtree.query(testRange)
    for part in list:
        part.colour = (0,0,255)

    for mainParticle in MASSES:
        range = Ring(mainParticle.Pos.x, mainParticle.Pos.y, mainParticle.radius * 3)
        testRange = Rectangle(mainParticle.Pos.x, mainParticle.Pos.y, mainParticle.radius, mainParticle.radius)
        closeParticles = qtree.query(testRange)
        for otherParticle in closeParticles:
            if (mainParticle != otherParticle and mainParticle.intersects(otherParticle)):
                doTypeOfCollision(mainParticle, otherParticle)










if __name__ == "__main__":
    startup()