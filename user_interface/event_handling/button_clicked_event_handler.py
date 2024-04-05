from typing import Tuple, Callable, List

from pygame.event import Event

from pipelines.ui_logic_accessor import UILogicAccessor
from user_interface.drawers.display import Display
from user_interface.entities.grid import Grid
from user_interface.entities.ui_game_state import UIGameState
from user_interface.event_handling.ievent_handler import IEventHandler
from user_interface.on_screen_objects.table import Table

GetChangedGridsMethodType = Callable[[Grid], Tuple[List[Grid], UIGameState]],


class ButtonClickedEventHandler(IEventHandler):
    def __init__(self, table: Table, ui_to_logic_pipeline: UILogicAccessor, display: Display):
        self.table = table
        self.game_logic = ui_to_logic_pipeline
        self.display = display

    def handle_event(self, event: Event) -> UIGameState:
        match event.button:
            case 1:  # Left click
                return self.handle_left_click(event.pos)
            case 3:  # Right click
                return self.handle_right_click(event.pos)
            case _:
                return UIGameState.ONGOING

    def handle_left_click(self, clicked_position: Tuple[int, int]) -> UIGameState:
        grid = self.table.get_grid_from_position(clicked_position)
        if grid is not None:
            return self.handle_table_click(self.game_logic.click_grid, grid)

    def handle_right_click(self, clicked_position: Tuple[int, int]) -> UIGameState:
        grid = self.table.get_grid_from_position(clicked_position)
        if grid is not None:
            return self.handle_table_click(self.game_logic.flag_grid, grid)

    def handle_table_click(self, get_changed_grids: GetChangedGridsMethodType, clicked_grid: Grid) -> UIGameState:
        changed_grids, next_game_state = get_changed_grids(clicked_grid)
        self.display.update_grids(changed_grids)
        return next_game_state
