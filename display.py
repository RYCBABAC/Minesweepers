from typing import Tuple, Optional

import pygame
from pygame import Surface


class Display:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
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
