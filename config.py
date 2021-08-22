# ======== IMPORT MODULES ========
import pygame
import matplotlib.cm

# ======== GLOBAL VARIABLES ========
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
FPS = 60
TIME_INTERVAL = 200
G = 6.67E-11
COLOUR_MAP = matplotlib.cm.get_cmap('plasma')
BLACK = (0, 0, 0)
GREY = (45, 45, 48)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# ======== CUSTOMIZABLE VARIABLES ========
SCALE = 1000000 # 100,000 km
RADIUS = 4
BARRIER = True
BLACK_HOLE = False
CENTER_OF_MASS = False
ACCELERATION_VECTOR = False
VELOCITY_VECTOR = False
