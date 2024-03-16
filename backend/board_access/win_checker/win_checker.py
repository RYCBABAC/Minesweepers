from backend.board_access.board.board import Board
from backend.board_access.win_checker.iwin_checker import IWinChecker
from backend.entities.grid import Grid
from backend.entities.grid_type import GridType


class WinChecker(IWinChecker):
    def __init__(self, board: Board):
        self.board = board

    def did_user_win(self) -> bool:
        return not any(grid for grid in self.board.grids.values() if self.is_invalid_in_winning(grid))

    @staticmethod
    def is_invalid_in_winning(grid: Grid) -> bool:
        return not grid.is_revealed and grid.type != GridType.MINE
