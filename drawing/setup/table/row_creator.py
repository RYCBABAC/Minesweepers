from pygame import Rect

from drawing.configurations.size_manager import GRID_HEIGHT, TABLE_WIDTH, COLS
from drawing.drawables.section import Section
from drawing.setup.table.grid_creator import create_grid


def __create_row_rect(row) -> Rect:
    top_left_x_position = 0
    top_left_y_position = GRID_HEIGHT * row
    width = TABLE_WIDTH
    height = GRID_HEIGHT
    return Rect(top_left_x_position, top_left_y_position, width, height)


def create_row(row) -> Section:
    rect = __create_row_rect(row)
    grids = [create_grid(col_index) for col_index in range(0, COLS)]
    return Section(rect, grids)
