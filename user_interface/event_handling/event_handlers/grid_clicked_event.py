from typing import List

from pygame import Rect
from pygame.event import Event

from user_interface.drawables.drawable import Drawable
from user_interface.drawables.text import Text
from user_interface.drawers.display import Display
from user_interface.event_handling.event_handler import EventHandler
from user_interface.logic_api.logic_api import LogicApi
from user_interface.on_screen_objects.table import Table


class GridClickedEvent(EventHandler):
    def __init__(self, display: Display, table: Table, logic_api: LogicApi):
        super().__init__(display)
        self.table = table
        self.logic_api = logic_api
        self.game_state_text = Text(
            font="Calibri",
            size=25,
            content=self.logic_api.get_game_state_text(),
            anti_alias=True,
            color=(0, 0, 0),
            rect=Rect((0, 65), (0, 0)))

    def process_event(self, event: Event) -> List[Drawable]:
        clicked_position = event.pos
        clicked_grid = self.table.get_grid_from_position(clicked_position)
        revealed_grids = self.logic_api.click_grid(clicked_grid)
        self.game_state_text.content = self.logic_api.get_game_state_text()
        return revealed_grids + [self.game_state_text]
