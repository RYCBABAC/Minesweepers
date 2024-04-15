from pygame import Rect

from drawing.drawables.section import Section
from drawing.configurations.size_manager import TOTAL_HEIGHT, BOTTOM_BORDER_HEIGHT, TOTAL_WIDTH


def create_bottom_border():
    top_left_x_position = 0
    top_left_y_position = TOTAL_HEIGHT - BOTTOM_BORDER_HEIGHT
    width = TOTAL_WIDTH
    height = BOTTOM_BORDER_HEIGHT
    rect = Rect(top_left_x_position, top_left_y_position, width, height)
    return Section(rect)
