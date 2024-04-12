from enum import Enum


class EventType(Enum):
    GRID_CLICKED = "grid_clicked"
    GRID_FLAGGED = "grid_flagged"
    QUIT = "quit"
    TIME_EVENT = "time_event"
