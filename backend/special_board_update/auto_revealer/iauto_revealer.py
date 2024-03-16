from abc import ABC, abstractmethod
from typing import List

from backend.entities.grid import Grid


class IAutoRevealer(ABC):
    @abstractmethod
    def reveal(self, clicked_grid: Grid) -> List[Grid]:
        raise NotImplementedError
