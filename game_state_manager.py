from typing import Dict, List

import pygame

from cell import Cell
from cell_clicked_event_handler import CellClickedEventHandler
from display import Display
from game_quit_event_handler import GameQuitEventHandler
from game_state import GameState
from ievent_handler import IEventHandler


class GameStateManager:
    def __init__(self, board: List[Cell], display: Display):
        self.board = board
        self.display = display
        self.event_handlers: Dict[int, IEventHandler] = {}

    def __enter__(self):
        self.event_handlers = {
            pygame.QUIT: GameQuitEventHandler(),
            pygame.MOUSEBUTTONUP: CellClickedEventHandler(self.board, self.display)
        }
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.event_handlers = {}

    def get_game_state(self) -> List[GameState]:
        return [self.event_handlers[event.type].handle_event(event) for event in pygame.event.get() if
                event.type in self.event_handlers]
