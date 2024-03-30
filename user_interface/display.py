from typing import Optional, List

import pygame
from pygame import Surface

from entities.cell import Cell
from entities.text import Text
from game_logic.board import Board
from user_interface.cell_image_mapper import CellImageMapper


class Display:
    BACKGROUND_COLOR = (192, 192, 192)
    HORIZONTAL_BORDER_SIZE = (16, 16)
    VERTICAL_BORDER_SIZE = (100, 16)
    DISPLAY_SIZE = (Board.BOARD_SIZE[0] * Cell.CELL_SIZE[0] + HORIZONTAL_BORDER_SIZE[0] + HORIZONTAL_BORDER_SIZE[1],
                    Board.BOARD_SIZE[1] * Cell.CELL_SIZE[1] + VERTICAL_BORDER_SIZE[0] + VERTICAL_BORDER_SIZE[1])

    def __init__(self, cell_image_mapper: CellImageMapper):
        self.cell_image_mapper = cell_image_mapper
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

    def update_cells(self, cells: List[Cell]) -> None:
        for cell in cells:
            image = self.cell_image_mapper[cell.image]
            self.display.blit(image, cell.rect)

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
