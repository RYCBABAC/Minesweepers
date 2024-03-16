from abc import ABC, abstractmethod

from entities.backend_controller_response import BackendControllerResponse


class IBackendController(ABC):
    @abstractmethod
    def initialize_game(self) -> BackendControllerResponse:
        raise NotImplementedError

    @abstractmethod
    def grid_clicked_event(self, grid_index: int) -> BackendControllerResponse:
        raise NotImplementedError
