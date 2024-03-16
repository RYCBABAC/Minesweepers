from abc import ABC, abstractmethod
from typing import List

from backend.entities.grid import Grid


class IMinesCreator(ABC):
    @abstractmethod
    def create_mines(self, num_of_mines: int) -> List[Grid]:
        raise NotImplementedError
