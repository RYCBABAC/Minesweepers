from typing import List

from backend.board_access.updater.iboard_updater import IBoardUpdater
from backend.entities.grid import Grid
from backend.entities.grid_type import GridType
from backend.special_board_access.neighbors_accesser.ineighbors_accesser import INeighborsAccessor
from backend.special_board_update.auto_revealer.iauto_revealer import IAutoRevealer


class AutoRevealer(IAutoRevealer):
    def __init__(self, board_updater: IBoardUpdater, neighbors_accessor: INeighborsAccessor):
        self.board_updater = board_updater
        self.neighbors_accessor = neighbors_accessor

    def reveal(self, clicked_grid: Grid) -> List[Grid]:
        self.reveal_single_grid(clicked_grid)
        return self.reveal_neighbors(clicked_grid)

    def reveal_neighbors(self, grid: Grid) -> List[Grid]:
        neighbors = self.get_neighbors_to_reveal(grid)
        revealed_grids = neighbors + [grid]
        if not any(neighbors):
            return revealed_grids

        for neighbor in neighbors:
            revealed_grids += self.reveal_neighbors(neighbor)
        return neighbors

    def reveal_single_grid(self, grid: Grid) -> Grid:
        grid.is_revealed = True
        self.board_updater.update_board(grid)
        return grid

    def get_neighbors_to_reveal(self, grid: Grid) -> List[Grid]:
        neighbors = self.neighbors_accessor.get_neighbors(grid)
        neighbors_to_reveal = [self.reveal_single_grid(neighbor) for neighbor in neighbors if
                               self.should_reveal_neighbor(grid, neighbor)]
        return neighbors_to_reveal

    @staticmethod
    def should_reveal_neighbor(grid: Grid, neighbor: Grid) -> bool:
        if grid.type == GridType.EMPTY:
            return not neighbor.is_revealed and neighbor.type != GridType.MINE
        return not neighbor.is_revealed and neighbor.type == GridType.EMPTY
