from dataclasses import dataclass

from pygame import Surface, Rect

from user_interface.drawables.drawable import Drawable
from user_interface.entities.grid_image import GridImage
from user_interface.resource_managers.grid_image_mapper import GridImageMapper


@dataclass
class Grid(Drawable):
    GRID_SIZE = (32, 32) # (x, y)

    index: int
    image: GridImage
    rect: Rect
    grid_image_mapper: GridImageMapper

    def draw(self, surface: Surface) -> None:
        surface_image = self.grid_image_mapper[self.image]
        surface.blit(surface_image, self.rect)

