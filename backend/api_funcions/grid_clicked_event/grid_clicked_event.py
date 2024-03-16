from typing import List, Tuple

from backend.api_funcions.grid_clicked_event.igrid_clicked_event import IGridClickedEvent
from backend.board_access.win_checker.iwin_checker import IWinChecker
from backend.entities.grid import Grid
from backend.entities.grid_type import GridType
from backend.special_board_update.auto_revealer.iauto_revealer import IAutoRevealer
from entities.game_state import GameState


class GridClickedEvent(IGridClickedEvent):
    def __init__(self, win_checker: IWinChecker, auto_revealer: IAutoRevealer):
        self.win_checker = win_checker
        self.auto_revealer = auto_revealer

    def grid_clicked_event(self, grid: Grid) -> Tuple[GameState, List[Grid]]:
        game_state = self.get_game_state(grid)
        return game_state, self.reveal_grids(grid, game_state)

    def get_game_state(self, grid: Grid) -> GameState:
        if grid.type == GridType.MINE:
            return GameState.USER_LOST
        elif self.win_checker.did_user_win():
            return GameState.USER_WON
        return GameState.ONGOING

    def reveal_grids(self, grid: Grid, game_state: GameState) -> List[Grid]:
        return self.auto_revealer.reveal(grid) if game_state != GameState.ONGOING else [grid]
