from abc import ABC, abstractmethod
from typing import List

from backend.entities.grid import Grid


class INeighborsAccessor(ABC):
    @abstractmethod
    def get_neighbors(self, grid: Grid) -> List[Grid]:
        raise NotImplementedError
