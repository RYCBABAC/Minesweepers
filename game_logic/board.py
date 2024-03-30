from typing import List

from entities.cell import Cell
from entities.cell_value import CellValue
from entities.update_type import CellUpdateType
from game_logic.cell_updater import CellUpdater


class Board:
    BOARD_SIZE = (10, 10)
    NUM_OF_MINES = 9

    def __init__(self, board: List[Cell]):
        self.board = board

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        index = cell.index
        neighbors_indices = self.get_neighbors_indices(index)
        return [self.board[neighbor_index] for neighbor_index in neighbors_indices]

    def get_neighbors_indices(self, index: int):
        cols = self.BOARD_SIZE[0]
        rows = self.BOARD_SIZE[1]
        r = index // cols
        c = index % cols
        return [(r - i) * cols + c - j for i in range(-1, 2) for j in range(-1, 2)
                if 0 <= r - i < rows and 0 <= c - j < cols and (r - i) * cols + c - j != 0]

    def reveal(self, clicked_cell: Cell) -> List[Cell]:
        revealed_cells = self.get_neighbors_to_reveal(clicked_cell)
        for cell in revealed_cells:
            CellUpdater.update_cell(cell, CellUpdateType.REVEAL)
            revealed_cells += self.reveal(cell)
        return revealed_cells

    def get_neighbors_to_reveal(self, clicked_cell: Cell) -> List[Cell]:
        if clicked_cell.value != CellValue.EMPTY:
            return []
        neighbors = self.get_neighbors(clicked_cell)
        return [neighbor for neighbor in neighbors
                if neighbor.value != CellValue.MINE and not neighbor.is_flagged and not neighbor.is_revealed]
