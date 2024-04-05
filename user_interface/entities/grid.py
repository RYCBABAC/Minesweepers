from dataclasses import dataclass

from pygame import Rect

from user_interface.entities.grid_image import GridImage


@dataclass
class Grid:
    CELL_SIZE = (32, 32)

    index: int
    rect: Rect
    image: GridImage
