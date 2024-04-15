from typing import Optional, List

import pygame
from pygame import Surface

from drawing.configurations.size_manager import TOTAL_HEIGHT, TOTAL_WIDTH
from user_interface.drawables.drawable import Drawable


class Drawer:
    def __init__(self):
        self.screen: Optional[Surface] = None

    def __enter__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.screen = None
        pygame.quit()

    def draw(self, drawable: Drawable):
        drawable.draw(self.screen)

    @staticmethod
    def update_frame():
        pygame.display.update()
