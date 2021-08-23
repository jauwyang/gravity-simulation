from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK, WHITE, RED, GREEN, BLUE, TURQUOISE
# **===== SINGLE ORBIT PRESET =====**

# ----- CONFIG -----
# BLACK_HOLE = False
# SCALE = 1000000


particles = [
    {
    "mass": 9e25,
    "colour": WHITE,
    "radius": 10,
    "staticMovement": True,
    "staticColour": True,
    "staticRadius": False,
    "position": {
        "xPos": WINDOW_WIDTH * SCALE / 2,
        "yPos": WINDOW_HEIGHT * SCALE / 2
    },
    "velocity": {
        "xVel": 0,
        "yVel": 0,
    }
    },
    {
    "mass": 9e25,
    "colour": TURQUOISE,
    "radius": 7,
    "staticMovement": False,
    "staticColour": True,
    "staticRadius": False,
    "position": {
        "xPos": WINDOW_WIDTH * SCALE / 2,
        "yPos": WINDOW_HEIGHT * SCALE /2 + 100000000
    },
    "velocity": {
        "xVel": 7700,
        "yVel": 0,
    }
    }
]