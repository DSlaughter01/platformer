# This class contains the classes needed for all of the interactive objects in the game
import pygame
from plat_variables import *

class Sprite(pygame.sprite.Sprite):

    LEFT_STILL = pygame.transform.scale_by(pygame.image.load(join('my_tiles', 'sprite_still.png')), SPRITE_SIZE / 24).convert_alpha()
    RIGHT_STILL = pygame.transform.flip(LEFT_STILL, flip_x = True, flip_y = False).convert_alpha()
    LEFT_WALK = pygame.transform.scale_by(pygame.image.load(join('my_tiles', 'sprite_walk.png')), SPRITE_SIZE / 24).convert_alpha()
    RIGHT_WALK = pygame.transform.flip(LEFT_WALK, flip_x = True, flip_y = False).convert_alpha()

    def __init__(self, 
                 x = BLOCK_SIZE, y = HEIGHT - BLOCK_SIZE - SPRITE_SIZE, 
                 width = SPRITE_SIZE, height = SPRITE_SIZE):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.img = self.RIGHT_STILL
        self.mask = pygame.mask.from_surface(self.img)
        self.direction = "right"
        self.has_landed = True
        self.x_vel = 0
        self.y_vel = 0

    # Update sprite velocity based on keydown movement
    def move_left(self):
        if self.direction != "left": self.direction = "left"
        self.x_vel = -X_VEL

    def move_right(self):
        if self.direction != "right": self.direction = "right"
        self.x_vel = X_VEL

    # Implement sprite movement
    def move(self, dx, dy):
        if self.y_vel <= MAX_Y_VEL and self.has_landed == False: self.y_vel += GRAVITY
        elif self.has_landed == True: self.y_vel = 0
        self.rect.x += dx
        self.rect.y += dy

    # Make the sprite jump
    def jump(self):
        self.y_vel = -18
        self.has_landed = False

    # Every so many frames, animate the sprite
    def choose_sprite(self):
        if self.direction == "right": self.img = self.RIGHT_STILL
        else: self.img = self.LEFT_STILL

    # Collisions
    def land(self):
        self.y_vel = 0
        self.has_landed = True
    
    def fall(self): 
        self.has_landed = False

    def hit_head(self): 
        self.y_vel = 3

    def update_pos():
        self.rect = self.img.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.img)

    def loop(self):
        # Stops the sprite moving infinitely after pressing an arrow key
        self.x_vel = 0

        # If no horizontal collisions, ok to move horizontally
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and left_coll == None: self.move_left()
        elif keys[pygame.K_RIGHT] and right_coll == None: self.move_right() 

        # self.choose_sprite()

        # Update the mask
        self.update()
        self.move(self.x_vel, self.y_vel)

    def draw_sprite(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Object(pygame.sprite.Sprite):

    def __init__(self, img_filename, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        # Not sure if it's bad practice to have 2 definitions of self.img in the __init__ function
        self.img = pygame.image.load(join('my_tiles', img_filename + '.png')).convert_alpha()
        self.img = pygame.transform.scale_by(self.img, height / self.img.get_height())
        self.mask = pygame.mask.from_surface(self.img) # Not sure what the next parameter threshold does
    
    def draw_obj(self, window, x_offset):
        window.blit(self.img, (self.rect.x - x_offset, self.rect.y))


class Block(Object):
    def __init__(self, img_filename, x, y, width, height):
        super().__init__(img_filename, x, y, width, height)