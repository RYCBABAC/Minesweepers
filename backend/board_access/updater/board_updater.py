from backend.board_access.board.board import Board
from backend.board_access.updater.iboard_updater import IBoardUpdater
from backend.entities.grid import Grid


class BoardUpdater(IBoardUpdater):
    def __init__(self, board: Board):
        self.board = board

    def update_board(self, grid: Grid) -> None:
        if grid.index not in self.board.grids:
            raise KeyError(f"Can't update the grid with index {grid.index} because it's outside of the board")
        self.board.grids[grid.index] = grid