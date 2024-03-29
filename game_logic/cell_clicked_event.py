from typing import List

from entities.cell import Cell
from entities.cell_value import CellValue
from entities.game_state import GameState
from entities.update_type import CellUpdateType
from game_logic.auto_revealer import AutoRevealer
from game_logic.cell_updater import CellUpdater
from game_logic.game_state_manager import GameStateManager
from user_interface.display import Display


class CellClickedEvent:
    def __init__(self, board: List[Cell], display: Display, auto_revealer: AutoRevealer,
                 game_state_manager: GameStateManager):
        self.board = board
        self.display = display
        self.auto_revealer = auto_revealer
        self.game_state_manager = game_state_manager

    def handle_cell_clicked_event(self, cell: Cell) -> None:
        if self.game_state_manager.game_state != GameState.ONGOING:
            return

        cells_to_reveal = self.get_revealed_cells(cell)
        self.set_game_state()
        self.display.update_cells(cells_to_reveal)

    def get_revealed_cells(self, cell: Cell) -> List[Cell]:
        if cell.value == CellValue.MINE:
            self.game_lost_reveal()
            self.game_state_manager.game_state = GameState.USER_LOST
            return self.board

        CellUpdater.update_cell(cell, CellUpdateType.REVEAL)
        return [cell] + self.auto_revealer.reveal(cell, self.board)

    def game_lost_reveal(self) -> None:
        for cell in self.board:
            CellUpdater.update_cell(cell, CellUpdateType.LOST_REVEAL)

    def set_game_state(self) -> None:
        did_user_win = not any(not cell.is_revealed for cell in self.board if cell.value != CellValue.MINE)
        self.game_state_manager.game_state = GameState.USER_WON if did_user_win else GameState.ONGOING
