import pygame
from pygame import Rect

from game_logic.board import Board
from user_interface.drawables.border import Border
from user_interface.drawables.grid import Grid

HORIZONTAL_BORDER_SIZE = (16, 16)  # (dist from start, dist from end)
VERTICAL_BORDER_SIZE = (100, 16)  # (dist from top, dist from bottom)
DISPLAY_SIZE = (Board.BOARD_SIZE[0] * Grid.GRID_SIZE[0] + HORIZONTAL_BORDER_SIZE[0] + HORIZONTAL_BORDER_SIZE[1],
                Board.BOARD_SIZE[1] * Grid.GRID_SIZE[1] + VERTICAL_BORDER_SIZE[0] + VERTICAL_BORDER_SIZE[1])


def main():
    top_border_height = 100
    left_border_width = 16
    right_border_width = 16
    bottom_border_height = 16
    rows = 10
    cols = 10
    grid_width = 32
    grid_height = 32
    total_width = left_border_width + right_border_width + cols * grid_width
    total_height = top_border_height + bottom_border_height + rows * grid_height
    side_borders_size_height = total_height - top_border_height - bottom_border_height
    borders_rects = [
        Rect(0, 0, total_width, top_border_height),
        Rect(0, top_border_height, left_border_width, side_borders_size_height),
        Rect(total_width - right_border_width, top_border_height, right_border_width, side_borders_size_height),
        Rect(0, total_height - bottom_border_height, total_width, bottom_border_height)
    ]
    borders = [Border(rect) for rect in borders_rects]
    pygame.init()
    display = pygame.display.set_mode((total_width, total_height))
    for border in borders:
        border.draw(display)
    pygame.display.update()

    stop = False
    while not stop:
        events = pygame.event.get()
        stop = pygame.QUIT in [event.type for event in events]


if __name__ == '__main__':
    main()
