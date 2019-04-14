import sys
from setting import *


class Menu:
    def __init__(self, screen):
        pygame.font.init()
        self.screen = screen
        self.buttons = [(WIN_WIDTH / 3, WIN_HEIGHT / 3 - 40, 'Play', (11, 0, 77), (0, 255, 0), 0),
                        (WIN_WIDTH / 3, WIN_HEIGHT / 3, 'Settings', (11, 0, 77), (0, 255, 0), 1),
                        (WIN_WIDTH / 3, WIN_HEIGHT / 3 + 40, 'Exit', (11, 0, 77), (0, 255, 0), 2)]
        #   coordinates (x, y)  , text,  (color1),     (color2), number
        self.menu()

    # button animation
    def render(self, screen, font, button_number):
        for i in self.buttons:
            if button_number == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        is_started = False
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        button = 0
        while not is_started:
            self.screen.fill(WHITE)
            pygame.Surface((800, 30)).fill((100, 100, 200))

            mouse_pos = pygame.mouse.get_pos()
            for parameter in self.buttons:
                # if (mouse_x_coord in button_x_coord)              and (mouse_y_coord in button_y_coord):
                if parameter[0] < mouse_pos[0] < parameter[0] + 155 and parameter[1] < mouse_pos[1] < parameter[1] + 50:
                    button = parameter[5]
            self.render(self.screen, font_menu, button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        if button > 0:
                            button -= 1
                    elif event.key == pygame.K_DOWN:
                        if button < len(self.buttons) - 1:
                            button += 1
                    elif event.key == pygame.K_RETURN:
                        if button == 0:
                            is_started = True
                        elif button == 1:
                            pass
                        elif button == 2:
                            exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button == 0:
                        is_started = True
                    elif button == 2:
                        pygame.quit()
                        sys.exit()
            self.screen.blit(pygame.Surface((800, 30)), (0, 1000))
            self.screen.blit(self.screen, (0, 30))
            pygame.display.flip()
