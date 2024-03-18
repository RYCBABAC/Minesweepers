import pygame
from pygame import Surface

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

game_size = (10, 10)
numMine = 9
grid_size = (32, 32)
horizontal_border = (16, 16)
vertical_border = (100, 16)


def game_loop():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


def create_display() -> Surface:
    pygame.init()

    display_size = (grid_size[0] * game_size[0] + horizontal_border[0] + horizontal_border[1],
                    grid_size[1] * game_size[1] + vertical_border[0] + vertical_border[1])
    return pygame.display.set_mode(display_size)


def update_display_color(game_display: Surface):
    game_display.fill(bg_color)
    pygame.display.update()


def main():
    game_display = create_display()
    update_display_color(game_display)
    game_loop()


if __name__ == "__main__":
    main()
