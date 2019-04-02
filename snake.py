import pygame
import random
from setting import *


class Snake:
    def __init__(self, color, play_surface):
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        # coordinates from head <-----------  to tail
        self.direction = RIGHT
        self.color = color
        self.play_surface = play_surface

    def change_dir(self, turn):
        if turn == RIGHT and not self.direction == LEFT:
            self.direction = turn
        elif turn == LEFT and not self.direction == RIGHT:
            self.direction = turn
        elif turn == UP and not self.direction == DOWN:
            self.direction = turn
        elif turn == DOWN and not self.direction == UP:
            self.direction = turn

    def move(self):
        dx = 10
        dy = 0
        if self.direction == RIGHT:
            dx = 10
            dy = 0
        elif self.direction == LEFT:
            dx = -10
            dy = 0
        elif self.direction == UP:
            dx = 0
            dy = -10
        elif self.direction == DOWN:
            dx = 0
            dy = 10

        self.snake_body.pop()
        self.snake_body.insert(0, [self.snake_body[0][0] + dx, self.snake_body[0][1] + dy])

    def grow(self):
        size = len(self.snake_body)
        tail_dir1 = self.snake_body[size - 2][0] - self.snake_body[size - 1][0]
        tail_dir2 = self.snake_body[size - 2][1] - self.snake_body[size - 1][1]
        self.snake_body.insert(size, [self.snake_body[size - 1][0] - tail_dir1,
                                      self.snake_body[size - 1][1] - tail_dir2])

    def draw(self, play_surface, surface_color):
        self.play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.color,
                             pygame.Rect(pos[0], pos[1], 10, 10))

    def collisions(self, food, fake_food, game):
        if self.snake_body[0] == food.position:
            self.grow()
            game.score += 1
            food.add(fake_food, self)
            while food.position in self.snake_body:
                food.position = [random.randrange(WIN_WIDTH / PIXEL_SIZE) * PIXEL_SIZE,
                                 random.randrange(WIN_HEIGHT / PIXEL_SIZE) * PIXEL_SIZE]

        if not (0 <= self.snake_body[0][0] < WIN_WIDTH):
                    return game.game_over()

        if not (0 <= self.snake_body[0][1] < WIN_HEIGHT):
                    return game.game_over()

        for i in range(1, len(self.snake_body)):
            if self.snake_body[0] == self.snake_body[i]:
                return game.game_over()

        # generate fake_food:
        wellnes = random.randrange(0, 100)
        if ((FAKE_FOOD_MIN_DIST < abs(self.snake_body[0][0] - food.position[0]) < FAKE_FOOD_MAX_DIST) and
                (FAKE_FOOD_MIN_DIST < abs(self.snake_body[0][1] - food.position[1]) < FAKE_FOOD_MAX_DIST) and
                wellnes == 1 and game.score > 3):
            fake_food.position.append(food.position)
            food.add(fake_food, self)
            print(fake_food.position)

        for i in range(len(fake_food.position)):
            if self.snake_body[0] == fake_food.position[i]:
                return game.game_over()

        return True
