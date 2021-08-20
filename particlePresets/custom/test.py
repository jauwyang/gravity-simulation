from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, RADIUS, FPS, BLACK, WHITE

particles = [
    {
    "mass": 9e30,
    "colour": WHITE,
    "radius": 10 * SCALE,
    "static": False,
    "position": {
        "xPos": WINDOW_WIDTH / 4 * SCALE,
        "yPos": WINDOW_HEIGHT / 4 * SCALE
    },
    "velocity": {
        "xVel": 100000,
        "yVel": 0,
    }
    },
    {
    "mass": 9e30,
    "colour": (255,0,0),
    "radius": 10 * SCALE,
    "static": False,
    "position": {
        "xPos": WINDOW_WIDTH * SCALE,
        "yPos": WINDOW_HEIGHT * SCALE
    },
    "velocity": {
        "xVel": 0,
        "yVel": 0,
    }
    }
]