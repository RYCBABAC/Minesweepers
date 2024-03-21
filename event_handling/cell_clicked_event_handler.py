from typing import List, Tuple, Optional

from pygame.event import Event

from entities.cell import Cell
from entities.game_state import GameState
from entities.update_type import CellUpdateType
from game_logic.cell_updater import CellUpdater
from event_handling.ievent_handler import IEventHandler
from user_interface.display import Display


class CellClickedEventHandler(IEventHandler):
    def __init__(self, board: List[Cell], display: Display):
        self.board = board
        self.display = display

    def handle_event(self, event: Event) -> GameState:
        clicked_pos = event.pos
        cell = self.get_clicked_cell(clicked_pos)
        if cell is None:
            return GameState.ONGOING

        update_type = CellUpdateType(event.button)
        CellUpdater.update_cell(cell, update_type)
        self.display.update_cells([cell])
        return GameState.ONGOING

    def get_clicked_cell(self, clicked_pos: Tuple[int, int]) -> Optional[Cell]:
        for cell in self.board:
            if cell.rect.collidepoint(clicked_pos):
                return cell
        return None

