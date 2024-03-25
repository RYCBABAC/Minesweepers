from entities.cell import Cell
from entities.game_state import GameState
from entities.update_type import CellUpdateType
from game_logic.cell_updater import CellUpdater
from game_logic.game_state_manager import GameStateManager
from user_interface.display import Display


class CellFlaggedEvent:
    def __init__(self, display: Display, game_state_manager: GameStateManager):
        self.display = display
        self.game_state_manager = game_state_manager

    def handle_cell_flagged_event(self, cell: Cell) -> None:
        if self.game_state_manager.game_state != GameState.ONGOING or cell.is_revealed:
            return

        CellUpdater.update_cell(cell, CellUpdateType.FLAG)
        self.display.update_cells([cell])

