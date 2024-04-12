from typing import Optional, List

import pygame
from pygame import Surface

from game_logic.board import Board
from user_interface.drawables.drawable import Drawable
from user_interface.drawables.grid import Grid
from user_interface.resource_managers.grid_image_mapper import GridImageMapper


class Display:
    BACKGROUND_COLOR = (192, 192, 192)  # (r, g, b)
    HORIZONTAL_BORDER_SIZE = (16, 16)  # (dist from start, dist from end)
    VERTICAL_BORDER_SIZE = (100, 16)  # (dist from top, dist from bottom)
    DISPLAY_SIZE = (Board.BOARD_SIZE[0] * Grid.GRID_SIZE[0] + HORIZONTAL_BORDER_SIZE[0] + HORIZONTAL_BORDER_SIZE[1],
                    Board.BOARD_SIZE[1] * Grid.GRID_SIZE[1] + VERTICAL_BORDER_SIZE[0] + VERTICAL_BORDER_SIZE[1])

    def __init__(self, grid_image_mapper: GridImageMapper):
        self.grid_image_mapper = grid_image_mapper
        self._display: Optional[Surface] = None
        self.is_game_running = False

    @property
    def display(self) -> Surface:
        return self._display

    def __enter__(self):
        pygame.init()
        self.is_game_running = True
        self._display = pygame.display.set_mode(self.DISPLAY_SIZE)
        self.display.fill(self.BACKGROUND_COLOR)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_game_running = False
        pygame.quit()

    def update_display(self, drawables: List[Drawable]):
        for drawable in drawables:
            drawable.draw(self.display)

    @staticmethod
    def update_frame():
        pygame.display.update()
