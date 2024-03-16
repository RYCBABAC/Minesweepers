from backend.board_access.board.board import Board
from backend.board_access.counter.iboard_counter import IBoardCounter


class BoardCounter(IBoardCounter):
    def __init__(self, board: Board):
        self.board = board

    def get_board_size(self) -> int:
        return len(self.board)