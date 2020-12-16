import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
FPS_POSITION = (50, 50)
TILE = 100  # т.к. карта 12 на 8 блоков (каждый блок 100 на 100 точек)
START_POSITION = (TILE*1.5, TILE*1.5)  # игрок в верхнем левом положении

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3  # угол обзора
HALF_FOV = FOV / 2
NUM_RAYS = 150  # 120
MAX_DEPTH = 800  # глубина
DELTA_ANGLE = FOV / NUM_RAYS  # угол между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # дистанция до стены
PROJ_COEFF = DIST * TILE  # коэффициент проекции
SCALE = WIDTH // NUM_RAYS  #

# player settings
CENTER_POSITION = (HALF_WIDTH, HALF_HEIGHT)
PLAYER_START_ANGLE = 0
PLAYER_SPEED = 2

CIRCLE_RADIUS = 12
RAY_LENGTH = WIDTH
ROTATE_ANGLE = 0.03

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 220)
DARK_GRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
SKY_COLOR = (0, 191, 255)
GROUND_COLOR = (162, 101, 62)
