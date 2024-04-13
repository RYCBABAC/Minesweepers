from typing import List

from pygame import Rect
from pygame.event import Event

from user_interface.drawables.drawable import Drawable
from user_interface.drawables.text import Text
from user_interface.drawers.display import Display
from user_interface.entities.grid_image import GridImage
from user_interface.event_handling.event_handler import EventHandler
from user_interface.logic_api.logic_api import LogicApi
from user_interface.on_screen_objects.table import Table


class GridFlaggedEvent(EventHandler):
    def __init__(self, display: Display, table: Table, logic_api: LogicApi):
        super().__init__(display)
        self.table = table
        self.logic_api = logic_api
        self.num_of_mines_text = Text(
            font="Calibri",
            size=50,
            content=str(logic_api.get_num_of_mines()),
            anti_alias=True,
            color=(0, 0, 0),
            rect=Rect(Display.DISPLAY_SIZE[0] - Display.HORIZONTAL_BORDER_SIZE[1] - 50, 0, 50, 50))

    def process_event(self, event: Event) -> List[Drawable]:
        flagged_position = event.pos
        flagged_grid = self.table.get_grid_from_position(flagged_position)
        num_of_mines = int(self.num_of_mines_text.content)
        flagged_grids = self.logic_api.flag_grid(flagged_grid)
        for grid in flagged_grids:
            if grid.image == GridImage.FLAG:
                num_of_mines -= 1
            else:
                num_of_mines += 1
        self.num_of_mines_text.content = str(num_of_mines)
        return flagged_grids + [self.num_of_mines_text]
