from typing import List

from entities.cell import Cell
from entities.cell_value import CellValue
from entities.game_state import GameState


class GameStateFinder:
    @staticmethod
    def get_game_state(clicked_cell: Cell, board: List[Cell]) -> GameState:
        if GameStateFinder.did_user_lose(clicked_cell):
            return GameState.USER_LOST
        elif GameStateFinder.did_user_win(board):
            return GameState.USER_WON
        else:
            return GameState.ONGOING

    @staticmethod
    def did_user_lose(clicked_cell: Cell) -> bool:
        return clicked_cell.value == CellValue.MINE

    @staticmethod
    def did_user_win(board: List[Cell]) -> bool:
        return not any(cell.is_revealed for cell in board)
