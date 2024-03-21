from typing import List, Tuple, Optional

from pygame.event import Event

from entities.cell import Cell
from entities.game_state import GameState
from entities.update_type import CellUpdateType
from game_logic.auto_revealer import AutoRevealer
from game_logic.cell_updater import CellUpdater
from event_handling.ievent_handler import IEventHandler
from user_interface.display import Display


class CellClickedEventHandler(IEventHandler):
    def __init__(self, board: List[Cell], display: Display, auto_revealer: AutoRevealer):
        self.board = board
        self.display = display
        self.auto_revealer = auto_revealer

    def handle_event(self, event: Event) -> GameState:
        clicked_pos = event.pos
        cell = self.get_clicked_cell(clicked_pos)
        if cell is None:
            return GameState.ONGOING

        update_type = CellUpdateType(event.button)
        CellUpdater.update_cell(cell, update_type)
        cells_to_reveal = [cell]
        if update_type == CellUpdateType.REVEAL:
            cells_to_reveal += self.auto_revealer.reveal(cell, self.board)
        self.display.update_cells(cells_to_reveal)
        return GameState.ONGOING

    def get_clicked_cell(self, clicked_pos: Tuple[int, int]) -> Optional[Cell]:
        for cell in self.board:
            if cell.rect.collidepoint(clicked_pos):
                return cell
        return None

