from menu import *
from game import *
from snake import *
from food import *
from fake_food import *


def main():

    while True:
        pygame.init()
        play_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Snake Game')

        Menu(play_surface)
        speed = GAME_SPEED
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
