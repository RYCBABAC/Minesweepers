from abc import ABC, abstractmethod


class IWinChecker(ABC):
    @abstractmethod
    def did_user_win(self) -> bool:
        raise NotImplementedError
