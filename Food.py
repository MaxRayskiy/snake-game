import pygame
import random
from setting import WIN_WIDTH, WIN_HEIGHT, PIXEL_SIZE


class Food:
    def __init__(self, food_color):
        self.color = food_color
        self.size_x = PIXEL_SIZE
        self.size_y = PIXEL_SIZE
        self.position = [random.randrange(WIN_WIDTH / PIXEL_SIZE) * PIXEL_SIZE,
                         random.randrange(WIN_HEIGHT / PIXEL_SIZE) * PIXEL_SIZE]

    def add(self, fake_food, snake):
        self.position = [random.randrange(WIN_WIDTH / PIXEL_SIZE) * PIXEL_SIZE,
                         random.randrange(WIN_HEIGHT / PIXEL_SIZE) * PIXEL_SIZE]
        first = True
        second = True
        while first or second:
            first = False
            for i in range(len(fake_food.position)):
                if fake_food.position[i] == self.position:
                    first = True
                    self.position = [random.randrange(WIN_WIDTH / PIXEL_SIZE) * PIXEL_SIZE,
                                     random.randrange(WIN_HEIGHT / PIXEL_SIZE) * PIXEL_SIZE]
                    break
            if not first:
                second = False
                for i in range(len(snake.snake_body)):
                    if snake.snake_body[i] == self.position:
                        second = True
                        self.position = [random.randrange(WIN_WIDTH / PIXEL_SIZE) * PIXEL_SIZE,
                                         random.randrange(WIN_HEIGHT / PIXEL_SIZE) * PIXEL_SIZE]
                        break

    def draw(self, play_surface):
        pygame.draw.rect(play_surface, self.color, pygame.Rect(
                self.position[0], self.position[1],
                self.size_x, self.size_y))

