from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK, WHITE

particles = [
    {
    "mass": 9e10,
    "colour": WHITE,
    "radius": 10 * SCALE,
    "staticMovement": False,
    "staticColour": False,
    "position": {
        "xPos": WINDOW_WIDTH / 4 * SCALE,
        "yPos": WINDOW_HEIGHT * SCALE * 1/4
    },
    "velocity": {
        "xVel": 10000,
        "yVel": 0,
    }
    },
    {
    "mass": 9e10,
    "colour": (0,255,0),
    "radius": 10 * SCALE,
    "staticMovement": False,
    "staticColour": False,
    "position": {
        "xPos": WINDOW_WIDTH * SCALE* 3/4,
        "yPos": WINDOW_HEIGHT * SCALE * 3/4
    },
    "velocity": {
        "xVel": -10000,
        "yVel": 0,
    }
    }
]