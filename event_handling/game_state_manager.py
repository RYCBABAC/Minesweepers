from typing import List

import pygame

from entities.cell import Cell
from entities.game_state import GameState
from event_handling.cell_clicked_event_handler import CellClickedEventHandler
from event_handling.game_quit_event_handler import GameQuitEventHandler
from user_interface.display import Display


class GameStateManager:
    def __init__(self, board: List[Cell], display: Display):
        self.board = board
        self.display = display
        self.event_handlers = {
            pygame.QUIT: GameQuitEventHandler(),
            pygame.MOUSEBUTTONUP: CellClickedEventHandler(self.board, self.display)
        }

    def get_game_state(self) -> List[GameState]:
        return [self.event_handlers[event.type].handle_event(event) for event in pygame.event.get() if
                event.type in self.event_handlers]
