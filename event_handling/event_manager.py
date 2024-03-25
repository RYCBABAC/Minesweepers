from typing import List

import pygame

from entities.cell import Cell
from entities.game_state import GameState
from event_handling.button_clicked_event_handler import ButtonClickedEventHandler
from event_handling.game_quit_event_handler import GameQuitEventHandler
from user_interface.display import Display


class EventManager:
    def __init__(self, game_quit_event_handler: GameQuitEventHandler,
                 cell_clicked_event_handler: ButtonClickedEventHandler):
        self.event_handlers = {
            pygame.QUIT: game_quit_event_handler,
            pygame.MOUSEBUTTONUP: cell_clicked_event_handler
        }

    def get_game_state(self) -> None:
        for event in pygame.event.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type].handle_event(event)
