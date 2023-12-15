import pygame
from plat_variables import *
from plat_class import *
from plat_func import *

pygame.init()
pygame.display.set_caption("Platformer")

def main():
    # Visual elements
    bg_img, tilemap = get_background()
    player = Sprite()
    x_offset = 0

    # Clock
    clock = pygame.time.Clock()
    run = True
