from pygame import Rect

from drawing.drawables.section import Section
from drawing.configurations.size_manager import RIGHT_BORDER_WIDTH, TOTAL_WIDTH, TOP_BORDER_HEIGHT, SIDE_BORDERS_HEIGHT


def create_right_border():
    top_left_x_position = TOTAL_WIDTH - RIGHT_BORDER_WIDTH
    top_left_y_position = TOP_BORDER_HEIGHT
    width = RIGHT_BORDER_WIDTH
    height = SIDE_BORDERS_HEIGHT
    rect = Rect(top_left_x_position, top_left_y_position, width, height)
    return Section(rect)

