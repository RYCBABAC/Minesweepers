from pygame.event import Event

from entities.game_state import GameState
from event_handling.ievent_handler import IEventHandler
from game_logic.game_state_manager import GameStateManager


class GameQuitEventHandler(IEventHandler):
    def __init__(self, game_state_manager: GameStateManager):
        self.game_state_manager = game_state_manager

    def handle_event(self, event: Event) -> None:
        self.game_state_manager.game_state = GameState.QUIT
