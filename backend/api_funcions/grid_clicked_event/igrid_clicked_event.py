from abc import ABC, abstractmethod
from typing import Tuple, List

from backend.entities.grid import Grid
from entities.game_state import GameState


class IGridClickedEvent(ABC):
    @abstractmethod
    def grid_clicked_event(self, grid: Grid) -> Tuple[GameState, List[Grid]]:
        raise NotImplementedError
