import pygame

from drawing.drawer.drawer import Drawer
from drawing.setup.display.create_display import create_display


def game_loop():
    stop = False
    while not stop:
        events = pygame.event.get()
        stop = pygame.QUIT in [event.type for event in events]


def main():
    with Drawer() as drawer:
        display = create_display()
        drawer.draw(display)
        drawer.update_frame()
        game_loop()


if __name__ == '__main__':
    main()
