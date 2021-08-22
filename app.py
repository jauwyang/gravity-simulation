# ======== IMPORT MODULES ========
from math_tools import distance
from collision_response import checkCollision
import pygame
import random
from space_objects import Map, Particle
import math
import sys
# ========= IMPORT PRESET MODULES =========
from particle_presets.black_hole import black_hole

# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK_HOLE, BARRIER, RADIUS, FPS, BLACK, WHITE, GREY, RED, GREEN, TIME_INTERVAL, ACCELERATION_VECTOR, VELOCITY_VECTOR, CENTER_OF_MASS

# ======== GLOBAL VARIABLES ========
CLOCK = pygame.time.Clock()
sys.setrecursionlimit(1500)

# ========= The TODO list ==========
# FUTURE PLANS: Make radius different?
# TODO: finish collision algorithm
# TODO: determine GOOD mass generation
# TODO: determine GOOD density generation
# TODO: finish pygame repeat run
    # TODO: incorporate collision detection in for loop of "redraw game window"


def userCustomization():
    getRandomStatusUserInput = True
    while getRandomStatusUserInput:
        randomStatus = input("\nRandomly generated objects? (T/F) ")
        if (randomStatus.lower() =="t"):
            randomStatus = True
            getRandomStatusUserInput = False
        elif (randomStatus.lower() == "f"):
            randomStatus = False
            getRandomStatusUserInput = False
        else:
            print("\nIncorrect input.\n")
    if randomStatus:
        while True:
            try:
                numberOfPlanets = int(input("Number of objects: "))
                if numberOfPlanets > 0:
                    break
                else:
                    print("\nValue must be greater than 0.\n")
            except ValueError:
                print("\nIncorrect input.\n")
    else:
        numberOfPlanets = 0

    return randomStatus, numberOfPlanets


def redrawGameWindow(window, space):
    window.fill(GREY)
    for object in space.particles:
        xPos = round(object.Pos.x / SCALE)
        yPos = round(object.Pos.y / SCALE)
        if object.collided == True:
            colour = RED
            object.collided = False
        else:
            colour = object.colour

        pygame.draw.circle(window, colour, (xPos, yPos), object.radius / SCALE)

        if ACCELERATION_VECTOR:
            pygame.draw.line(window, RED, (object.Accel.x*3+xPos, object.Accel.y*3+yPos), (xPos, yPos), 3)
        if VELOCITY_VECTOR:
            pygame.draw.line(window, GREEN, (object.Vel.x/10000+xPos, object.Vel.y/10000+yPos), (xPos, yPos), 3)

        # update particle properties
        object.updatePosition()
        object.updateVelocity()
        object.updateAcceleration(space)

    # update space
    if CENTER_OF_MASS:
        space.updateCenterMass()
        x = space.xCenterMass / space.totalMass / SCALE
        y = space.yCenterMass / space.totalMass / SCALE
        pygame.draw.circle(window, BLACK, (x,y), 2)

    # Run collision check
    checkCollision(space, window)

    pygame.display.update()

def createMasses(space):

    if BLACK_HOLE:
        space.particles.append(Particle(
            black_hole["mass"], 
            black_hole["position"]["xPos"], 
            black_hole["position"]["yPos"], 
            black_hole["velocity"]["xVel"], 
            black_hole["velocity"]["yVel"], 
            staticMovement = black_hole["staticMovement"], 
            staticColour = black_hole["staticColour"],
            staticRadius = black_hole["staticRadius"],
            radius = black_hole["radius"]* SCALE, 
            colour = black_hole["colour"]
        ))


    if space.randomStatus:
        for i in range(space.numberOfPlanets):
            xPos = random.randint(1, WINDOW_WIDTH * SCALE) 
            yPos = random.randint(1, WINDOW_HEIGHT * SCALE)
            xVel = random.randint(-1000, 1000)
            yVel = random.randint(-1000, 1000)
            density = None #TBD

            # Calculates Mass
            a = random.randint(5, 9)
            power = random.randint(5, 25)
            mass = float(str(a) + 'e' + str(power)) #TBD

            r = RADIUS * SCALE # might change / based on how to calculate 

            # Makes sure particles spawn at different locations
            if i != 0:
                j = 0
                while j < len(space.particles):
                    if (distance(space.particles[j].Pos.x, space.particles[j].Pos.y, xPos, yPos) - (space.particles[j].radius + r) < 0):
                        xPos = random.randint(1, WINDOW_WIDTH * SCALE) 
                        yPos = random.randint(1, WINDOW_HEIGHT * SCALE)
                        j = -1
                    j += 1
            space.particles.append(Particle(mass, xPos, yPos, xVel, yVel, density = density, radius = r))

    else:
        from particle_presets.custom.preset import particles
        for particle in particles:
            space.particles.append(Particle(
                particle["mass"], 
                particle["position"]["xPos"], 
                particle["position"]["yPos"], 
                particle["velocity"]["xVel"], 
                particle["velocity"]["yVel"], 
                staticMovement = particle["staticMovement"],
                staticColour = particle["staticColour"],
                radius = particle["radius"], 
                colour = particle["colour"]
            ))


    space.updateTotalMass()

    for particle in space.particles:
        if particle.colour == None:
            particle.changeColour()


def initializeSim():
    # Initialize space map
    randomStatus, numberOfPlanets = userCustomization()
    space = Map(randomStatus, numberOfPlanets, BLACK_HOLE)

    # Create the masses from user customization
    createMasses(space)

    # Initialize pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Main simulation loop
    run = True
    while run:
        # pygame.time.delay(1)
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        redrawGameWindow(window, space)
    pygame.quit()


if __name__ == "__main__":
    initializeSim()