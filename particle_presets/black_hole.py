# ======== CONFIG VARIABLES ========
from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE, BLACK_HOLE, BARRIER, RADIUS, FPS, BLACK, WHITE, RED, GREEN, TIME_INTERVAL, ACCELERATION_VECTOR, VELOCITY_VECTOR, CENTER_OF_MASS


black_hole = {
    "mass": 2e30,
    "colour": BLACK,
    "radius": 10,
    "staticMovement": True,
    "staticColour": True,
    "staticRadius": True,
    "position": {
        "xPos": (WINDOW_WIDTH / 2) * SCALE,
        "yPos": (WINDOW_HEIGHT / 2) * SCALE
    },
    "velocity": {
        "xVel": 0,
        "yVel": 0,
    }
}