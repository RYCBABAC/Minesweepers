from typing import List, Callable

from game_logic.board import Board
from game_logic.entities.cell import Cell
from game_logic.entities.cell_value import CellValue
from game_logic.entities.game_state import GameState
from user_interface.drawables.grid import Grid
from user_interface.entities.grid_image import GridImage
from user_interface.on_screen_objects.table import Table


def get_empty_and_valued_grid_image(cell: Cell) -> GridImage:
    return GridImage.EMPTY if cell.value == CellValue.EMPTY else GridImage(f"grid{cell.value.value}")


def get_hidden_grid_image(cell: Cell) -> GridImage:
    return get_unflagged_hidden_grid_image(cell) if not cell.is_flagged else get_clicked_flagged_grid_image(cell)


def get_unflagged_hidden_grid_image(cell: Cell) -> GridImage:
    return GridImage.MINE if cell.value == CellValue.MINE else get_empty_and_valued_grid_image(cell)


def get_revealed_grid_image(cell: Cell) -> GridImage:
    return GridImage.MINE_CLICKED if cell.value == CellValue.MINE else get_empty_and_valued_grid_image(cell)


def get_clicked_flagged_grid_image(cell: Cell) -> GridImage:
    return GridImage.MINE if cell.value == CellValue.MINE else GridImage.MINE_FALSE


def get_clicked_grid_image(cell: Cell) -> GridImage:
    return get_revealed_grid_image(cell) if cell.is_revealed else get_hidden_grid_image(cell)


def get_flagged_grid_image(cell: Cell) -> GridImage:
    return GridImage.FLAG if cell.is_flagged else GridImage.CELL


TableClickApiType = Callable[[Cell], List[Cell]]
ImageGetterType = Callable[[Cell], GridImage]


class LogicApi:
    def __init__(self, board: Board, table: Table):
        self.board = board
        self.table = table

    def click_grid(self, clicked_grid: Grid) -> List[Grid]:
        return self.__table_click_api(clicked_grid, self.board.click_cell, get_clicked_grid_image)

    def flag_grid(self, flagged_grid: Grid) -> List[Grid]:
        return self.__table_click_api(flagged_grid, self.board.flag_cell, get_flagged_grid_image)

    def is_game_locked(self) -> bool:
        return self.board.get_game_state() != GameState.ONGOING

    def __table_click_api(self, grid: Grid, api_action: TableClickApiType, image_getter: ImageGetterType) -> List[Grid]:
        clicked_cell = self.board.board[grid.index]
        revealed_cells = api_action(clicked_cell)
        return [self.__get_grid(cell, image_getter) for cell in revealed_cells]

    def __get_grid(self, cell: Cell, image_getter: ImageGetterType) -> Grid:
        grid = self.table.table[cell.index]
        grid.image = image_getter(cell)
        return grid
