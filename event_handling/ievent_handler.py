from abc import ABC, abstractmethod

from pygame.event import Event


class IEventHandler(ABC):
    @abstractmethod
    def handle_event(self, event: Event) -> None:
        raise NotImplementedError
