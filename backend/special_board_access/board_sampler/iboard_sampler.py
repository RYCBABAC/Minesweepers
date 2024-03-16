from abc import ABC, abstractmethod
from typing import List

from backend.entities.grid import Grid


class IBoardSampler(ABC):
    @abstractmethod
    def sample_from_board(self, count: int) -> List[Grid]:
        raise NotImplementedError
