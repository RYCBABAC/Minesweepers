from abc import ABC, abstractmethod

from backend.entities.grid import Grid


class IBoardGetter(ABC):
    @abstractmethod
    def get_from_board(self, index: int) -> Grid:
        raise NotImplementedError
