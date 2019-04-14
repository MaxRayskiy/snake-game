import sys
import time
from setting import *


class Game:
    def __init__(self, speed, play_surface):
        self.score = 0
        self.fps_controller = pygame.time.Clock()
        self.speed = speed
        self.play_surface = play_surface
        self.is_paused = False

    def change_dir(self, turn):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("pause")
                    self.is_paused = True
                    while self.is_paused:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                exit()
                            elif e.type == pygame.KEYDOWN:
                                if e.key == pygame.K_SPACE:
                                    print("continue")
                                    self.is_paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                try:
                    turn = turn_dict[event.key]
                except KeyError:
                    pass

        return turn

    def refresh(self):
        pygame.display.update()
        self.fps_controller.tick(self.speed)

    def show_score(self):
        s_font = pygame.font.SysFont(FREESANS, 24)
        s_surf = s_font.render('Score: {0}'.format(self.score), True, BLACK)
        s_rect = s_surf.get_rect()
        s_rect.midtop = (80, 10)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont(MONACO, 72)
        go_surf = go_font.render('Game over', True, RED)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.play_surface.blit(go_surf, go_rect)
        pygame.display.flip()
        time.sleep(2)
        return False
