from abc import ABC, abstractmethod
from typing import List

from backend.entities.grid import Grid


class IGridsInitializer(ABC):
    @abstractmethod
    def initialize_grids(self, mines: List[Grid]) -> None:
        raise NotImplementedError
