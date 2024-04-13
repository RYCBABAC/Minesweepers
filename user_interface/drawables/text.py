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

    @property
    def surface(self) -> Surface:
        surface = Surface(self.rect.size)
        surface.fill(Display.BACKGROUND_COLOR)
        text = pygame.font.SysFont(self.font, self.size).render(self.content, self.anti_alias, self.color)
        surface.blit(text, dest=(0, 0))
        self.rect.size = text.get_size()
        return surface

