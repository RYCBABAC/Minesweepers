from user_interface.drawers.display import Display
from user_interface.entities.event_type import EventType
from user_interface.event_handling.event_handlers.game_quit_event import GameQuitEvent
from user_interface.event_handling.event_handlers.grid_clicked_event import GridClickedEvent
from user_interface.event_handling.event_handlers.grid_flagged_event import GridFlaggedEvent
from user_interface.event_handling.event_handlers.time_event import TimeEvent
from user_interface.event_handling.event_manager import EventManager
from user_interface.on_screen_objects.table import Table


class EventManagerBuilder:
    @staticmethod
    def build_event_manager(table: Table, display: Display, logic_api) -> EventManager:
        event_manager = EventManager()
        event_manager.subscribe_event(EventType.QUIT, GameQuitEvent(display))
        event_manager.subscribe_event(EventType.GRID_CLICKED, GridClickedEvent(display, table, logic_api))
        event_manager.subscribe_event(EventType.GRID_FLAGGED, GridFlaggedEvent(display, table, logic_api))
        event_manager.subscribe_event(EventType.TIME_EVENT, TimeEvent(display, logic_api))
        return event_manager
