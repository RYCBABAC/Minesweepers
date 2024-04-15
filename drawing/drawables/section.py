from dataclasses import dataclass
from typing import List

from pygame import Surface

from user_interface.drawables.drawable import Drawable


@dataclass
class Section(Drawable):
    BACKGROUND_COLOR = (192, 192, 192)

    items: List[Drawable] = None

    @property
    def surface(self) -> Surface:
        surface = Surface(self.rect.size)
        surface.fill(self.BACKGROUND_COLOR)
        self.__add_items_to_surface(surface)
        return surface

    def __add_items_to_surface(self, surface: Surface) -> None:
        if self.items is None:
            return

        for item in self.items:
            item.draw(surface)
