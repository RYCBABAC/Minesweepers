from typing import Optional, List

import pygame
from pygame import Surface

from game_logic.board import Board
from user_interface.entities.grid import Grid
from user_interface.entities.text import Text
from user_interface.resource_managers.grid_image_mapper import GridImageMapper


class Display:
    BACKGROUND_COLOR = (192, 192, 192)
    HORIZONTAL_BORDER_SIZE = (16, 16)
    VERTICAL_BORDER_SIZE = (100, 16)
    DISPLAY_SIZE = (Board.BOARD_SIZE[0] * Grid.CELL_SIZE[0] + HORIZONTAL_BORDER_SIZE[0] + HORIZONTAL_BORDER_SIZE[1],
                    Board.BOARD_SIZE[1] * Grid.CELL_SIZE[1] + VERTICAL_BORDER_SIZE[0] + VERTICAL_BORDER_SIZE[1])

    def __init__(self, grid_image_mapper: GridImageMapper):
        self.grid_image_mapper = grid_image_mapper
        self._display: Optional[Surface] = None

    @property
    def display(self) -> Surface:
        return self._display

    def __enter__(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.DISPLAY_SIZE)
        self.display.fill(self.BACKGROUND_COLOR)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()

    def update_grids(self, grids: List[Grid]) -> None:
        for grid in grids:
            image = self.grid_image_mapper[grid.image]
            self.display.blit(image, grid.rect)

    def update_text(self, text: Text) -> None:
        text_content_surface = (pygame.font.SysFont(text.font, text.size)
                                .render(text.content, text.anti_alias, text.color))
        text_surface = Surface(text_content_surface.get_size())
        text_surface.fill(self.BACKGROUND_COLOR)
        text_surface.blit(text_content_surface, (0, 0))
        self.display.blit(text_surface, text.position)

    @staticmethod
    def update_frame() -> None:
        pygame.display.update()
