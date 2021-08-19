# ======== IMPORT MODULES ========
import pygame
import matplotlib.cm

# ======== GLOBAL VARIABLES ========
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
FPS = 60
SCALE = 100000000 # 100,000 km
TIME_INTERVAL = 3.6*168
G = 6.67E-11
COLOUR_MAP = matplotlib.cm.get_cmap('plasma')
BLACK = (0, 0, 0)
GREY = (45, 45, 48)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# ======== CUSTOMIZABLE VARIABLES ========
RADIUS = 3
BARRIER = True
BLACK_HOLE = True
CENTER_OF_MASS = False
ACCELERATION_VECTOR = False
VELOCITY_VECTOR = False
