from pygame import Rect

from drawing.drawables.section import Section
from drawing.configurations.size_manager import TOP_BORDER_HEIGHT, LEFT_BORDER_WIDTH, SIDE_BORDERS_HEIGHT


def create_left_border():
    top_left_x_position = 0
    top_left_y_position = TOP_BORDER_HEIGHT
    width = LEFT_BORDER_WIDTH
    height = SIDE_BORDERS_HEIGHT
    rect = Rect(top_left_x_position, top_left_y_position, width, height)
    return Section(rect)
