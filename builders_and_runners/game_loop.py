from entities.game_state import GameState
from event_handling.event_manager import EventManager
from game_logic.game_state_manager import GameStateManager
from user_interface.display import Display
from user_interface.time_manager import TimeManager


class GameLoop:
    def __init__(self, event_manager: EventManager, game_state_manager: GameStateManager, time_manager: TimeManager):
        self.event_manager = event_manager
        self.game_state_manager = game_state_manager
        self.time_manager = time_manager

    def run_game(self) -> None:
        while self.game_state_manager.game_state != GameState.QUIT:
            self.event_manager.handle_events()
            self.time_manager.update_time()
            Display.update_frame()
