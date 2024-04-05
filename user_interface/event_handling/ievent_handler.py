from abc import ABC, abstractmethod

from pygame.event import Event

from user_interface.entities.ui_game_state import UIGameState


class IEventHandler(ABC):
    @abstractmethod
    def handle_event(self, event: Event) -> UIGameState:
        raise NotImplementedError
