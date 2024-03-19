from pygame.event import Event

from game_state import GameState
from ievent_handler import IEventHandler


class GameQuitEventHandler(IEventHandler):
    def handle_event(self, event: Event) -> GameState:
        return GameState.QUIT
