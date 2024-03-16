from abc import ABC, abstractmethod


class IBoardCounter(ABC):
    @abstractmethod
    def get_board_size(self) -> int:
        raise NotImplementedError
