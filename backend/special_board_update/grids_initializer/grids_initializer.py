from typing import List

from backend.board_access.updater.iboard_updater import IBoardUpdater
from backend.entities.grid import Grid
from backend.entities.grid_type import GridType
from backend.special_board_access.neighbors_accesser.ineighbors_accesser import INeighborsAccessor
from backend.special_board_update.grids_initializer.igrids_initializer import IGridsInitializer


class GridsInitializer(IGridsInitializer):
    def __init__(self, board_updater: IBoardUpdater, neighbors_accessor: INeighborsAccessor):
        self.board_updater = board_updater
        self.neighbors_accessor = neighbors_accessor

    def initialize_grids(self, mines: List[Grid]) -> None:
        for mine in mines:
            mines_neighbors = self.neighbors_accessor.get_neighbors(mine)
            self.update_mine_neighbors(mines_neighbors)

    def update_mine_neighbors(self, mines_neighbors: List[Grid]) -> None:
        for grid in mines_neighbors:
            grid.type = self.get_grid_type(grid)
            self.board_updater.update_board(grid)

    def get_grid_type(self, grid: Grid) -> GridType:
        if grid.type != GridType.EMPTY:
            return GridType.EMPTY
        grid_value = sum(neighbor.type == GridType.MINE for neighbor in self.neighbors_accessor.get_neighbors(grid))
        return GridType(grid_value)
