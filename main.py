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

    while run:
        
        clock.tick(FPS)
        # left, right, vert = movement(player, tilemap)
        coll = vertical_coll(player, tilemap)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        x_offset = get_offset(player, x_offset)
        player.loop()
        draw(bg_img, tilemap, player, x_offset)

if __name__ == main():
    main()