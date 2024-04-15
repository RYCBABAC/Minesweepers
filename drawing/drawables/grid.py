from dataclasses import dataclass

from pygame import Surface

from user_interface.drawables.drawable import Drawable
from user_interface.entities.grid_image import GridImage
from user_interface.resource_managers.grid_image_getter import get_grid_image


@dataclass
class Grid(Drawable):
    image: GridImage

    @property
    def surface(self) -> Surface:
        return get_grid_image(self.image)
