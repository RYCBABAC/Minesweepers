from dataclasses import dataclass

from pygame.rect import RectType

from entities.cell_image import CellImage
from entities.cell_value import CellValue


@dataclass
class Cell:
    index: int
    value: CellValue
    image: CellImage
    is_revealed: bool
    is_flagged: bool
    rect: RectType
