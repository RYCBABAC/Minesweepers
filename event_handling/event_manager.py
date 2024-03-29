import pygame

from event_handling.button_clicked_event_handler import ButtonClickedEventHandler
from event_handling.game_quit_event_handler import GameQuitEventHandler


class EventManager:
    def __init__(self, game_quit_event_handler: GameQuitEventHandler,
                 cell_clicked_event_handler: ButtonClickedEventHandler):
        self.event_handlers = {
            pygame.QUIT: game_quit_event_handler,
            pygame.MOUSEBUTTONUP: cell_clicked_event_handler
        }

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type].handle_event(event)
