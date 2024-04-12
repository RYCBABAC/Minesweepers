from abc import ABC, abstractmethod
from typing import List

from pygame.event import Event

from user_interface.drawables.drawable import Drawable
from user_interface.drawers.display import Display


class EventHandler(ABC):
    def __init__(self, display: Display):
        self.display = display

    @abstractmethod
    def process_event(self, event: Event) -> List[Drawable]:
        raise NotImplementedError

    def handle_event(self, event: Event) -> None:
        changed_element = self.process_event(event)
        self.display.update_display(changed_element)
