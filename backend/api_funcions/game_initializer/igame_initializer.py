from abc import ABC, abstractmethod


class IGameInitializer(ABC):
    @abstractmethod
    def initialize_game(self, num_of_mines: int) -> None:
        raise NotImplementedError
