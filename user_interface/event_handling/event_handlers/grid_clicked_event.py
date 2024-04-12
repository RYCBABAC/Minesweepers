from typing import List

from pygame.event import Event

from user_interface.drawables.drawable import Drawable
from user_interface.drawers.display import Display
from user_interface.event_handling.event_handler import EventHandler
from user_interface.logic_api.logic_api import LogicApi
from user_interface.on_screen_objects.table import Table


class GridClickedEvent(EventHandler):
    def __init__(self, display: Display, table: Table, logic_api: LogicApi):
        super().__init__(display)
        self.table = table
        self.logic_api = logic_api

    def process_event(self, event: Event) -> List[Drawable]:
        clicked_position = event.pos
        clicked_grid = self.table.get_grid_from_position(clicked_position)
        return self.logic_api.click_grid(clicked_grid)


