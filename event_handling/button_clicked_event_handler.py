from typing import List, Tuple, Optional

from pygame.event import Event

from entities.cell import Cell
from entities.game_state import GameState
from event_handling.ievent_handler import IEventHandler
from game_logic.board import Board
from game_logic.cell_clicked_event import CellClickedEvent
from game_logic.cell_flagged_event import CellFlaggedEvent


class ButtonClickedEventHandler(IEventHandler):
    def __init__(self, board: Board, cell_clicked_event: CellClickedEvent, cell_flagged_event: CellFlaggedEvent):
        self.board = board
        self.cell_clicked_event = cell_clicked_event
        self.cell_flagged_event = cell_flagged_event

    def handle_event(self, event: Event) -> GameState:
        cell = self.get_clicked_cell(event.pos)
        if cell is None:
            return GameState.ONGOING

        match event.button:
            case 1:  # Left click
                self.cell_clicked_event.handle_cell_clicked_event(cell)
            case 3:  # Right click
                self.cell_flagged_event.handle_cell_flagged_event(cell)

    def get_clicked_cell(self, clicked_pos: Tuple[int, int]) -> Optional[Cell]:
        for cell in self.board.board:
            if cell.rect.collidepoint(clicked_pos):
                return cell
        return None
