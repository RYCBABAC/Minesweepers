from dataclasses import dataclass

from backend.entities.grid_type import GridType
from entities.board_element import BoardElement


@dataclass
class Grid(BoardElement):
    type: GridType = GridType.EMPTY
    is_revealed: bool = False
