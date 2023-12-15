import pygame
from os.path import join

pygame.init()

# Screen display
WIDTH, HEIGHT = 1366, 708
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
#TOP_FONT = pygame.font.SysFont('Comic Sans', 40)
#GAME_OVER_FONT = pygame.font.SysFont('ComicSans', 100)

# Blocks and background
BLOCK_SIZE = 64
SPRITE_SIZE = 48

# Movement
X_VEL = 5
MAX_Y_VEL = 10
GRAVITY = 1
