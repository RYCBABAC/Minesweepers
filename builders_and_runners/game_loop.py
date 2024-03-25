from entities.game_state import GameState
from event_handling.event_manager import EventManager
from game_logic.game_state_manager import GameStateManager


class GameLoop:
    def __init__(self, event_manager: EventManager, game_state_manager: GameStateManager):
        self.event_manager = event_manager
        self.game_state_manager = game_state_manager

    def run_game(self) -> None:
        while self.game_state_manager.game_state != GameState.QUIT:
            self.event_manager.get_game_state()
