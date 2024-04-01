from typing import Tuple

from pygame.event import Event

from event_handling.ievent_handler import IEventHandler
from game_logic.board import Board
from game_logic.board_event_manager import BoardEventManager


class ButtonClickedEventHandler(IEventHandler):
    def __init__(self, board: Board, board_event_manager: BoardEventManager):
        self.board = board
        self.board_event_manager = board_event_manager

    def handle_event(self, event: Event) -> None:
        match event.button:
            case 1:  # Left click
                self.handle_left_click(event.pos)
            case 3:  # Right click
                self.handle_right_click(event.pos)

    def handle_left_click(self, clicked_position: Tuple[int, int]) -> None:
        cell = self.board.get_cell_from_position(clicked_position)
        if cell is not None:
            self.board_event_manager.handle_cell_clicked_event(cell)

    def handle_right_click(self, clicked_position: Tuple[int, int]) -> None:
        cell = self.board.get_cell_from_position(clicked_position)
        if cell is not None:
            self.board_event_manager.handle_cell_flagged_event(cell)
