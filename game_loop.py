from game_state import GameState
from game_state_manager import GameStateManager


class GameLoop:
    def __init__(self, game_state_manager: GameStateManager):
        self.game_state_manager = game_state_manager

    def run_game(self) -> None:
        is_game_finished = False
        while not is_game_finished:
            game_current_states = self.game_state_manager.get_game_state()
            is_game_finished = GameState.QUIT in game_current_states
