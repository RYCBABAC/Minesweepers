from typing import List, Tuple

from entities.cell import Cell


class NeighborsAccessor:
    def __init__(self, game_size: Tuple[int, int]):
        self.game_size = game_size

    def get_neighbors(self, cell: Cell, board: List[Cell]) -> List[Cell]:
        index = cell.index
        neighbors_indices = self.get_neighbors_indices(index)
        return [board[neighbor_index] for neighbor_index in neighbors_indices]

    def get_neighbors_indices(self, index: int):
        cols = self.game_size[0]
        rows = self.game_size[1]
        r = index // cols
        c = index % cols
        return [(r - i) * cols + c - j for i in range(-1, 2) for j in range(-1, 2)
                if 0 <= r - i < rows and 0 <= c - j < cols and (r - i) * cols + c - j != 0]

