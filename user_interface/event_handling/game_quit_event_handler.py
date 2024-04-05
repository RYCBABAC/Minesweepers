from pygame.event import Event

from user_interface.entities.ui_game_state import UIGameState
from user_interface.event_handling.ievent_handler import IEventHandler


class GameQuitEventHandler(IEventHandler):
    def handle_event(self, event: Event) -> UIGameState:
        return UIGameState.QUIT
