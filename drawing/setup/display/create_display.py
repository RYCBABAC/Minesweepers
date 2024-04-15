from typing import List

from pygame import Rect

from drawing.configurations.size_manager import TOTAL_HEIGHT, TOTAL_WIDTH
from drawing.drawables.drawable import Drawable
from drawing.drawables.section import Section
from drawing.setup.borders.bottom_border_creator import create_bottom_border
from drawing.setup.borders.left_border_creator import create_left_border
from drawing.setup.borders.right_border_creator import create_right_border
from drawing.setup.table.table_creator import create_table
from drawing.setup.borders.top_border_creator import create_top_border


def __create_display_rect() -> Rect:
    top_left_x_position = 0
    top_left_y_position = 0
    width = TOTAL_WIDTH
    height = TOTAL_HEIGHT
    return Rect(top_left_x_position, top_left_y_position, width, height)


def __create_borders() -> List[Drawable]:
    return [
        create_top_border(),
        create_bottom_border(),
        create_left_border(),
        create_right_border()
    ]


def __create_display_items_list() -> List[Drawable]:
    return __create_borders() + [create_table()]


def create_display() -> Section:
    rect = __create_display_rect()
    items = __create_display_items_list()
    return Section(rect, items)
