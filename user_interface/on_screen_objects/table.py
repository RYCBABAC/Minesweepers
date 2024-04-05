from typing import List, Tuple, Optional

from user_interface.entities.grid import Grid


class Table:
    TABLE_SIZE = (10, 10)
    def __init__(self, table: List[Grid]):
        self.table = table

    def get_grid_from_position(self, position: Tuple[int, int]) -> Optional[Grid]:
        for grid in self.table:
            if grid.rect.collidepoint(position):
                return grid
        return None
