from pygame.event import Event

from entities.game_state import GameState
from event_handling.ievent_handler import IEventHandler


class GameQuitEventHandler(IEventHandler):
    def handle_event(self, event: Event) -> GameState:
        return GameState.QUIT
