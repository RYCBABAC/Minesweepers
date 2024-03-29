from typing import Tuple, Optional, List

import pygame
from pygame import Surface

from entities.cell import Cell
from entities.text import Text
from user_interface.cell_image_mapper import CellImageMapper


class Display:
    def __init__(self, size: Tuple[int, int], cell_image_mapper: CellImageMapper, background_color: Tuple[int, int]):
        self.size = size
        self.cell_image_mapper = cell_image_mapper
        self._display: Optional[Surface] = None
        self.background_color = background_color

    @property
    def display(self) -> Surface:
        return self._display

    def __enter__(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.size)
        self.display.fill(self.background_color)
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
        text_surface.fill(self.background_color)
        text_surface.blit(text_content_surface, (0, 0))
        self.display.blit(text_surface, text.position)

    @staticmethod
    def update_frame() -> None:
        pygame.display.update()
