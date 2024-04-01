from typing import Dict

import pygame

from event_handling.ievent_handler import IEventHandler


class EventManager:
    def __init__(self):
        self.event_handlers: Dict[int, IEventHandler] = {}

    def subscribe_event(self, event_type: int, event_handler: IEventHandler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = event_handler

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type].handle_event(event)
