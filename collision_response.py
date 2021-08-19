# ======== IMPORT MODULES ========
from quad_tree import QuadTree
from math_tools import Rectangle, Vector2D, Point, Ring

# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK
BOUNDARY = Rectangle(WINDOW_WIDTH * SCALE/2, WINDOW_HEIGHT * SCALE/2, WINDOW_WIDTH * SCALE / 2, WINDOW_HEIGHT * SCALE / 2)


def doElasticCollison(p1, p2):
    # Compute unit normal and unit tangent vectors
    normalVector = Vector2D(p2.Pos.x - p1.Pos.x, p2.Pos.y - p2.Pos.y)
    unitNormalVector = normalVector.unitVector()
    unitTangentVector = Vector2D(-unitNormalVector.y, unitNormalVector.x)

    normalVelocity1 = unitNormalVector.dot(p1.Vel)
    tangentVelocity1 = unitTangentVector.dot(p1.Vel)
    normalVelocity2 = unitNormalVector.dot(p2.Vel)
    tangentVelocity2 = unitTangentVector.dot(p2.Vel)

    normalVelocity1Prime = (normalVelocity1*(p1.mass - p2.mass) + 2*p2.mass*normalVelocity2) / (p1.mass + p2.mass)
    normalVelocity2Prime = (normalVelocity2*(p2.mass - p1.mass) + 2*p1.mass*normalVelocity1) / (p1.mass + p2.mass)

    vectorNormalVelocity1Prime = unitNormalVector.scalarMultiply(normalVelocity1Prime)
    vectorTangentVelocity1Prime = unitTangentVector.scalarMultiply(tangentVelocity1)
    vectorNormalVelocity2Prime = unitNormalVector.scalarMultiply(normalVelocity2Prime)
    vectorTangentVelocity2Prime = unitTangentVector.scalarMultiply(tangentVelocity2)

    p1.Vel.x = vectorNormalVelocity1Prime.x + vectorTangentVelocity1Prime.x
    p1.Vel.y = vectorNormalVelocity1Prime.y + vectorTangentVelocity1Prime.y
    p2.Vel.x = vectorNormalVelocity2Prime.x + vectorTangentVelocity2Prime.x
    p2.Vel.y = vectorNormalVelocity2Prime.y + vectorTangentVelocity2Prime.y


def doInelasticCollision(p1, p2, space):
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

    if p1.staticMovement or p2.staticMovement:
        p1.staticMovement = True
    combineCollisionColours(space, p1, p2)
    combineCollisionRadius(p1, p2)

    space.particles.remove(p2)
    space.numberOfPlanets -= 1


def doTypeOfCollision(space, p1, p2):


    # TODO: determine whether collision is inelastic vs elastic (bounce off or stick together)
    # doElasticCollison(p1, p2)
    doInelasticCollision(p1, p2, space)


def combineCollisionColours(space, p1, p2):
    if p1.staticColour and p2.staticColour:
        if p2.colour == BLACK or p1.colour == BLACK:
            p1.changeColour(BLACK)
        else:
            p1.changeColour((((p1.colour[0] + p2.colour[0]) / 2), ((p1.colour[1] + p2.colour[1]) / 2),) ((p1.colour[2] + p2.colour[2]) / 2))
    elif p2.staticColour:
        p1.changeColour(p2.colour)
        p1.staticColour = True
    elif p1.staticColour:
        pass
    else:
        p1.changeColour()


def combineCollisionRadius(p1, p2):
    if p1.staticRadius and p2.staticRadius and p1.radius != p2.radius:
        if (p2.colour == BLACK and p1.colour == BLACK) or (p2.colour != BLACK and p1.colour != BLACK):
            p1.radius = (p1.radius + p2.radius) / 2
        elif p2.colour == BLACK:
            p1.radius = p2.radius
        else:
            pass
    elif p2.staticRadius:
        p1.radius = p2.radius
        p1.staticRadius = True
    elif p1.staticRadius:
        pass
    else:
        p1.radius = (p1.radius + p2.radius) / 2



def checkCollision(space, window):
    # TODO: have to account for deleted particles in array
    # TODO: account for the "range" of a particle since it only works if ALL particles have the same radius
    qtree = QuadTree(BOUNDARY, 2)
    for particle in space.particles:
        qtree.insert(particle)

    qtree.draw(window)

    for mainParticle in space.particles:
        range = Ring(mainParticle.Pos.x, mainParticle.Pos.y, mainParticle.radius * 2.5)
        closeParticles = qtree.query(range)
        for otherParticle in closeParticles:
            if (mainParticle != otherParticle and mainParticle.intersects(otherParticle)):
                print("COLLISION")
                doTypeOfCollision(space, mainParticle, otherParticle)