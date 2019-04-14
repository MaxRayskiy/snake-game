import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 300
PIXEL_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 00)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)

FREESANS = 'freesans'
MONACO ='monaco'

GAME_SPEED = 10

RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

turn_dict = {pygame.K_RIGHT: RIGHT,
             pygame.K_LEFT: LEFT,
             pygame.K_UP: UP,
             pygame.K_DOWN: DOWN,
             pygame.K_d: RIGHT,
             pygame.K_a: LEFT,
             pygame.K_w: UP,
             pygame.K_s: DOWN}

FAKE_FOOD_MAX_DIST = 80
FAKE_FOOD_MIN_DIST = 20
