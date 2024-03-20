from typing import Tuple, Optional, List

import pygame
from pygame import Surface

from entities.cell import Cell
from user_interface.cell_image_mapper import CellImageMapper


class Display:
    def __init__(self, size: Tuple[int, int], cell_image_mapper: CellImageMapper):
        self.size = size
        self.cell_image_mapper = cell_image_mapper
        self._display: Optional[Surface] = None

    @property
    def display(self) -> Surface:
        return self._display

    def __enter__(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.size)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()

    def set_background_color(self, background_color: Tuple[int, int]):
        self.display.fill(background_color)
        pygame.display.update()

    def update_cells(self, cells: List[Cell]) -> None:
        for cell in cells:
            image = self.cell_image_mapper[cell.image]
            self.display.blit(image, cell.rect)
        pygame.display.update()
