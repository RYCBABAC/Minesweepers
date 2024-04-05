from dataclasses import dataclass

from game_logic.entities.cell_value import CellValue


@dataclass
class Cell:
    index: int
    value: CellValue
    is_revealed: bool
    is_flagged: bool
