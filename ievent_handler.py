from abc import ABC, abstractmethod

from pygame.event import Event

from game_state import GameState


class IEventHandler(ABC):
    @abstractmethod
    def handle_event(self, event: Event) -> GameState:
        raise NotImplementedError
