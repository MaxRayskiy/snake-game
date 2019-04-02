import pygame
from setting import PIXEL_SIZE

class FakeFood:
    def __init__(self, color):
        self.color = color
        self.position = []
        self.size_x = PIXEL_SIZE
        self.size_y = PIXEL_SIZE

    def draw(self, play_surface):
        for ff_position in self.position:
            pygame.draw.rect(play_surface, self.color, pygame.Rect(
                ff_position[0], ff_position[1],
                self.size_x, self.size_y))
