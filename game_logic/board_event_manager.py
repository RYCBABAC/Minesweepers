from typing import List

from entities.cell import Cell
from entities.cell_value import CellValue
from entities.game_state import GameState
from entities.update_type import CellUpdateType
from game_logic.board import Board
from game_logic.cell_updater import CellUpdater
from game_logic.game_state_manager import GameStateManager
from user_interface.display import Display


class BoardEventManager:
    def __init__(self, board: Board, display: Display, game_state_manager: GameStateManager):
        self.board = board
        self.display = display
        self.game_state_manager = game_state_manager

    def handle_cell_clicked_event(self, cell: Cell) -> None:
        if self.game_state_manager.game_state != GameState.ONGOING:
            return

        CellUpdater.update_cell(cell, CellUpdateType.REVEAL)
        cells_to_reveal = self.get_revealed_cells(cell)
        self.game_state_manager.game_state = self.get_new_game_state(cell)
        self.display.update_cells(cells_to_reveal)

    def handle_cell_flagged_event(self, cell: Cell) -> None:
        if self.game_state_manager.game_state != GameState.ONGOING or cell.is_revealed:
            return

        CellUpdater.update_cell(cell, CellUpdateType.FLAG)
        self.display.update_cells([cell])

    def get_revealed_cells(self, cell: Cell) -> List[Cell]:
        if self.did_user_lose(cell):
            return self.board.reveal_all()
        return [cell] + self.board.reveal(cell)

    def get_new_game_state(self, cell: Cell) -> GameState:
        if self.did_user_lose(cell):
            return GameState.USER_LOST
        elif self.board.did_user_win():
            return GameState.USER_WON
        else:
            return GameState.ONGOING

    @staticmethod
    def did_user_lose(cell: Cell) -> bool:
        return cell.value == CellValue.MINE
