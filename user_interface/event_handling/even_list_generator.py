from typing import List, Optional, Tuple

import pygame
from pygame.event import Event

from user_interface.entities.event_type import EventType
from user_interface.on_screen_objects.table import Table


def get_event_list() -> List[Tuple[EventType, Event]]:
    for event in pygame.event.get():
        event_type = identify_event(event)
        if event_type is not None:
            yield event_type, event
    yield EventType.TIME_EVENT, None


def identify_event(event: Event) -> Optional[EventType]:
    if event.type == pygame.QUIT:
        return EventType.QUIT
    elif event.type == pygame.MOUSEBUTTONUP and Table.is_in_table(event.pos):
        if event.button == 1:
            return EventType.GRID_CLICKED
        elif event.button == 3:
            return EventType.GRID_FLAGGED
    return None



