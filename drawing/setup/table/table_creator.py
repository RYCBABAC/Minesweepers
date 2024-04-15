from pygame import Rect

from drawing.configurations.size_manager import TABLE_WIDTH, LEFT_BORDER_WIDTH, TOP_BORDER_HEIGHT, \
    TABLE_HEIGHT, ROWS
from drawing.drawables.section import Section
from drawing.setup.table.row_creator import create_row


def __create_table_rect() -> Rect:
    top_left_x_position = LEFT_BORDER_WIDTH
    top_left_y_position = TOP_BORDER_HEIGHT
    width = TABLE_WIDTH
    height = TABLE_HEIGHT
    return Rect(top_left_x_position, top_left_y_position, width, height)


def create_table() -> Section:
    rect = __create_table_rect()
    rows = [create_row(row_index) for row_index in range(0, ROWS)]
    return Section(rect, rows)
