from dataclasses import dataclass

from pygame import Surface, Rect

from user_interface.drawables.drawable import Drawable
from user_interface.entities.grid_image import GridImage
from user_interface.resource_managers.grid_image_getter import get_grid_image


@dataclass
class Grid(Drawable):
    GRID_SIZE = (32, 32)  # (x, y)

    index: int
    image: GridImage
    rect: Rect

    def draw(self, surface: Surface) -> None:
        surface_image = get_grid_image(self.image)
        surface.blit(surface_image, self.rect)
