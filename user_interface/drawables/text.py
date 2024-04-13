from dataclasses import dataclass
from typing import Tuple

import pygame
from pygame import Surface, Rect

from user_interface.drawables.drawable import Drawable
from user_interface.drawers.display import Display


@dataclass
class Text(Drawable):
    font: str
    size: int
    content: str
    anti_alias: bool
    color: Tuple[int, int, int]
    position: Tuple[int, int]

    def draw(self, surface: Surface) -> None:
        text_surface = self.create_text_surface()
        text_surface = self.add_background_to_text_surface(text_surface)
        surface.blit(text_surface, Rect(self.position,text_surface.get_size()))

    def create_text_surface(self) -> Surface:
        return pygame.font.SysFont(self.font, self.size).render(self.content, self.anti_alias, self.color)

    @staticmethod
    def add_background_to_text_surface(text_surface: Surface) -> Surface:
        text_surface_with_background = Surface(text_surface.get_size())
        text_surface_with_background.fill(Display.BACKGROUND_COLOR)
        text_surface_with_background.blit(text_surface, (0, 0))
        return text_surface_with_background
