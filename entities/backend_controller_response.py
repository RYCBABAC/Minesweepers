from dataclasses import dataclass, field
from typing import List

from entities.game_state import GameState


@dataclass
class BackendControllerResponse:
    game_state: GameState = GameState.ONGOING
    revealed_grids: List[int] = field(default_factory=list)
    error_message: str = ""
