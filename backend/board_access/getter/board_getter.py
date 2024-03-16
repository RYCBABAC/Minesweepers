from backend.board_access.board.board import Board
from backend.board_access.getter.iboard_getter import IBoardGetter
from backend.entities.grid import Grid


class BoardGetter(IBoardGetter):
    def __init__(self, board: Board):
        self.board = board

    def get_from_board(self, index: int) -> Grid:
        if index not in self.board.grids:
            raise KeyError("This index is outside of the board")
        return self.board.grids[index]
    