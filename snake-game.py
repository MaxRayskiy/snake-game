import pygame
import sys
import random
import time


WIN_WIDTH = 400
WIN_HEIGHT = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 00)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)


class Menu:
    def __init__(self, screen):
        pygame.font.init()
        self.screen = screen
        self.buttons = [(WIN_WIDTH / 3, WIN_HEIGHT / 3 - 40, 'Play', (11, 0, 77), (0, 255, 0), 0),
                        (WIN_WIDTH / 3, WIN_HEIGHT / 3, 'Settings', (11, 0, 77), (0,255,0), 1),
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
        start_game = False
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        button = 0
        while not start_game:
            self.screen.fill((255, 255, 255))
            pygame.Surface((800, 30)).fill((100, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.buttons:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    button = i[5]
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
                            start_game = True
                        if button == 1:
                            pass
                        if button == 2:
                            exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button == 0:
                        start_game = True
                    elif button == 2:
                        pygame.quit()
                        sys.exit()
            self.screen.blit(pygame.Surface((800, 30)), (0, 1000))
            self.screen.blit(self.screen, (0, 30))
            pygame.display.flip()


class Game:
    def __init__(self, speed, play_surface):
        self.score = 0
        self.fps_controller = pygame.time.Clock()
        self.speed = speed
        self.play_surface = play_surface

    def change_dir(self, turn):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("pause")
                    pause = True
                    while pause:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                exit()
                            elif e.type == pygame.KEYDOWN:
                                if e.key == pygame.K_SPACE:
                                    print("continue")
                                    pause = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    turn = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    turn = "RIGHT"
                elif event.key == pygame.K_UP:
                    turn = "UP"
                elif event.key == pygame.K_DOWN:
                    turn = "DOWN"
        return turn

    def refresh(self):
        pygame.display.update()
        self.fps_controller.tick(self.speed)

    def show_score(self):
        s_font = pygame.font.SysFont('freesans', 24)
        s_surf = s_font.render('Score: {0}'.format(self.score), True, BLACK)
        s_rect = s_surf.get_rect()
        s_rect.midtop = (80, 10)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, RED)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.play_surface.blit(go_surf, go_rect)
        pygame.display.flip()
        time.sleep(2)
        return False


class Snake:
    def __init__(self, color, play_surface):
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        # coordinates from head <-----------  to tail
        self.direction = "RIGHT"
        self.color = color
        self.play_surface = play_surface

    def change_dir(self, turn):
        if turn == "RIGHT" and not self.direction == "LEFT":
            self.direction = turn
        elif turn == "LEFT" and not self.direction == "RIGHT":
            self.direction = turn
        elif turn == "UP" and not self.direction == "DOWN":
            self.direction = turn
        elif turn == "DOWN" and not self.direction == "UP":
            self.direction = turn

    def move(self):
        dx = 10
        dy = 0
        if self.direction == "RIGHT":
            dx = 10
            dy = 0
        elif self.direction == "LEFT":
            dx = -10
            dy = 0
        elif self.direction == "UP":
            dx = 0
            dy = -10
        elif self.direction == "DOWN":
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
                food.position = [random.randrange(WIN_WIDTH / 10) * 10,
                                 random.randrange(WIN_HEIGHT / 10) * 10]

        if not (0 <= self.snake_body[0][0] < WIN_WIDTH):
            return game.game_over()

        if not (0 <= self.snake_body[0][1] < WIN_HEIGHT):
            return game.game_over()

        for i in range(1, len(self.snake_body)):
            if self.snake_body[0] == self.snake_body[i]:
                return game.game_over()

        # generate fake_food:
        wellnes = random.randrange(0, 100)
        if ((-80 < self.snake_body[0][0] - food.position[0] < 80) and
            (-80 < self.snake_body[0][1] - food.position[1] < 80) and
            not (-20 < self.snake_body[0][0] - food.position[0] < 20) and
            not (-20 < self.snake_body[0][1] - food.position[1] < 20) and
                wellnes == 1 and game.score > 3):
            fake_food.position.append(food.position)
            food.add(fake_food, self)
            print(fake_food.position)

        for i in range(len(fake_food.position)):
            if self.snake_body[0] == fake_food.position[i]:
                return game.game_over()

        return True


class Food:
    def __init__(self, food_color):
        self.color = food_color
        self.size_x = 10
        self.size_y = 10
        self.position = [random.randrange(WIN_WIDTH/10)*10,
                         random.randrange(WIN_HEIGHT/10)*10]

    def add(self, fake_food, snake):
        self.position = [random.randrange(WIN_WIDTH / 10) * 10,
                         random.randrange(WIN_HEIGHT / 10) * 10]
        first = True
        second = True
        while first or second:
            first = False
            for i in range(len(fake_food.position)):
                if fake_food.position[i] == self.position:
                    first = True
                    self.position = [random.randrange(WIN_WIDTH / 10) * 10,
                                     random.randrange(WIN_HEIGHT / 10) * 10]
                    break
            if not first:
                second = False
                for i in range(len(snake.snake_body)):
                    if snake.snake_body[i] == self.position:
                        second = True
                        self.position = [random.randrange(WIN_WIDTH / 10) * 10,
                                         random.randrange(WIN_HEIGHT / 10) * 10]
                        break

    def draw(self, play_surface):
        pygame.draw.rect(play_surface, self.color, pygame.Rect(
                self.position[0], self.position[1],
                self.size_x, self.size_y))


class FakeFood:
    def __init__(self, color):
        self.color = color
        self.position = []
        self.size_x = 10
        self.size_y = 10

    def draw(self, play_surface):
        for ff_position in self.position:
            pygame.draw.rect(play_surface, self.color, pygame.Rect(
                ff_position[0], ff_position[1],
                self.size_x, self.size_y))


def main():
    while True:
        pygame.init()
        play_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Snake Game')

        main = Menu(play_surface)
        speed = 10
        game = Game(speed, play_surface)
        snake = Snake(GREEN, play_surface)
        food = Food(RED)
        fake_food = FakeFood(BLACK)

        play = True
        while play:
            snake.change_dir(game.change_dir(snake.direction))
            snake.move()
            play = snake.collisions(food, fake_food, game)
            snake.draw(play_surface, WHITE)
            game.show_score()
            food.draw(play_surface)
            fake_food.draw(play_surface)

            game.refresh()


if __name__ == '__main__':
    main()
