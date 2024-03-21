from typing import List

from entities.cell import Cell
from entities.cell_value import CellValue
from entities.update_type import CellUpdateType
from game_logic.cell_updater import CellUpdater
from game_logic.neighbors_accessor import NeighborsAccessor


class AutoRevealer:
    def __init__(self, neighbors_accessor: NeighborsAccessor):
        self.neighbors_accessor = neighbors_accessor

    def reveal(self, clicked_cell: Cell, board: List[Cell]) -> List[Cell]:
        revealed_cells = self.get_neighbors_to_reveal(clicked_cell, board)
        for cell in revealed_cells:
            CellUpdater.update_cell(cell, CellUpdateType.REVEAL)
            revealed_cells += self.reveal(cell, board)
        return revealed_cells
    def get_neighbors_to_reveal(self, clicked_cell: Cell, board: List[Cell]) -> List[Cell]:
        if clicked_cell.value != CellValue.EMPTY:
            return []
        neighbors = self.neighbors_accessor.get_neighbors(clicked_cell, board)
        return [neighbor for neighbor in neighbors
                if neighbor.value != CellValue.MINE and not neighbor.is_flagged and not neighbor.is_revealed]