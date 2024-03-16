from abc import ABC, abstractmethod

from backend.entities.grid import Grid


class IBoardUpdater(ABC):
    @abstractmethod
    def update_board(self, grid:Grid) -> None:
        raise NotImplementedError
