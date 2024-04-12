from typing import Dict

from user_interface.entities.event_type import EventType
from user_interface.event_handling.even_list_generator import get_event_list
from user_interface.event_handling.event_handler import EventHandler


class EventManager:
    def __init__(self):
        self.event_handlers: Dict[EventType, EventHandler] = {}

    def subscribe_event(self, event_type: EventType, event_handler: EventHandler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = event_handler

    def handle_events(self) -> None:
        for event_type, event in get_event_list():
            if event_type in self.event_handlers:
                self.event_handlers[event_type].handle_event(event)
