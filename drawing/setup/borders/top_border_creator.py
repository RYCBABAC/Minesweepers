from pygame import Rect

from drawing.drawables.section import Section
from drawing.configurations.size_manager import TOTAL_WIDTH, TOP_BORDER_HEIGHT


def create_top_border():
    top_left_x_position = 0
    top_left_y_position = 0
    width = TOTAL_WIDTH
    height = TOP_BORDER_HEIGHT
    rect = Rect(top_left_x_position, top_left_y_position, width, height)
    return Section(rect)

