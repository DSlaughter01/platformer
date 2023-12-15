import pygame
from plat_variables import *
from plat_class import *

def get_background():

    # Background image
    background_img = pygame.image.load(join('my_tiles', 'tilemap-backgrounds_packed.png')).subsurface(0, 0, 96, 72)
    background_img = pygame.transform.scale_by(background_img, HEIGHT / background_img.get_height())

    # Tilemap
    tiles = {1: 'left_floor', 2: 'mid_floor', 3: 'right_floor', 4: 'alone_floor'}
    tilemap = []

    # Read tile coordinates from tilemap.txt into tilemap list
    with open('tilemap.txt', 'r') as f:
        y = 0
        for row in f:
            x = 0
            for tile in row:
                if tile != '.' and tile != '\n':
                    tilemap.append(Block(tiles[int(tile)], x, y, BLOCK_SIZE, BLOCK_SIZE))
                x += BLOCK_SIZE
            y += BLOCK_SIZE

    return background_img, tilemap

# x offset when moving more than 100 pixels aways from left or right border
def get_offset(player, x_offset):

    if player.rect.x > WIDTH - 200 + x_offset and player.x_vel > 0: x_offset += X_VEL
    elif player.rect.x < 200 + x_offset and player.x_vel < 0: x_offset -= X_VEL
    
    return x_offset


def vertical_coll(player, objects):
    
    obj_list = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            obj_list.append(obj)
            
    if len(obj_list) == 0: player.fall()

    for obj in obj_list:
        if player.y_vel > 0: 
            player.rect.bottom = obj.rect.top
            player.land()
        elif player.y_vel < 0:
            player.rect.top = obj.rect.bottom
            player.hit_head()
    
    return obj_list


def horizontal_coll(player, dx, objects):

    hor_collision = None

    # Move in x direction to test for collisions (don't draw this)
    player.move(dx, 0)
    player.update()
    
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if player.x_vel > 0: player.rect.right = obj.rect.left
            elif player.x_vel < 0: player.rect.left = obj.rect.right
            break
    
    player.move(-dx, 0)
    player.update()

    return hor_collision


def movement(player, objects):

    left = horizontal_coll(player, -X_VEL, objects)
    right = horizontal_coll(player, X_VEL, objects)
    vert = vertical_coll(player, objects)

    return left, right, vert


def draw(bg_img, tilemap, player, x_offset = 0):

    for i in range(4): WIN.blit(bg_img, (i*bg_img.get_width() - x_offset, 0))
    for tile in tilemap: tile.draw_obj(WIN, x_offset)
    player.draw_sprite(WIN)

    pygame.display.update()