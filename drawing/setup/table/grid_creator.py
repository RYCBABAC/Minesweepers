from pygame import Rect

from drawing.configurations.size_manager import GRID_WIDTH, GRID_HEIGHT
from drawing.drawables.grid import Grid
from user_interface.entities.grid_image import GridImage


def create_grid(col) -> Grid:
    top_left_x_position = GRID_WIDTH * col
    top_left_y_position = 0
    width = GRID_WIDTH
    height = GRID_HEIGHT
    rect = Rect(top_left_x_position, top_left_y_position, width, height)
    return Grid(rect, GridImage.CELL)