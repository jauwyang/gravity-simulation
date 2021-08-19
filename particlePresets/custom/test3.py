from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK, WHITE, RED, GREEN

particles = [
    {
    "mass": 9e30,
    "colour": None,
    "radius": 10 * SCALE,
    "staticMovement": False,
    "staticColour": False,
    "position": {
        "xPos": WINDOW_WIDTH / 4 * SCALE,
        "yPos": WINDOW_HEIGHT * SCALE * 47/100
    },
    "velocity": {
        "xVel": 100,
        "yVel": 0,
    },
    "acceleration": {
        "xAccel": 0,
        "yAccel": 0
    }
    },
    {
    "mass": 9e30,
    "colour": None,
    "radius": 10 * SCALE,
    "staticMovement": False,
    "staticColour": False,
    "position": {
        "xPos": WINDOW_WIDTH * SCALE* 3/4,
        "yPos": WINDOW_HEIGHT * SCALE * 50/100
    },
    "velocity": {
        "xVel": -100,
        "yVel": 0,
    },
    "acceleration": {
        "xAccel": 0,
        "yAccel": 0
    }
    }
]