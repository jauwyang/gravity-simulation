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
        "yPos": WINDOW_HEIGHT * SCALE * 50/100
    },
    "velocity": {
        "xVel": 5,
        "yVel": 0,
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
        "yPos": WINDOW_HEIGHT * SCALE * 48/100
    },
    "velocity": {
        "xVel": -5,
        "yVel": 0,
    }
    }
]