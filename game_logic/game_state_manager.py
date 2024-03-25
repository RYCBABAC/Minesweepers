from dataclasses import dataclass

from entities.game_state import GameState


@dataclass
class GameStateManager:
    game_state: GameState = GameState.ONGOING
