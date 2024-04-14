from dataclasses import dataclass
from typing import List

from pygame import Surface

from user_interface.drawables.drawable import Drawable
from user_interface.drawables.grid import Grid


@dataclass
class Row(Drawable):
    grids: List[Grid]

    @property
    def surface(self) -> Surface:
        surface = Surface(self.rect.size)
        for grid in self.grids:
            grid.draw(surface)
        return surface
