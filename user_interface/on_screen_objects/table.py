from typing import List, Tuple

from user_interface.drawables.grid import Grid
from user_interface.drawers.display import Display


class Table:
    TABLE_SIZE = (10, 10)  # (rows, cols)

    def __init__(self, table: List[Grid]):
        self.table = table

    @staticmethod
    def is_in_table(pos: Tuple[int, int]) -> bool:
        dist_from_start = Display.HORIZONTAL_BORDER_SIZE[0]
        dist_from_end = Display.DISPLAY_SIZE[0] - Display.HORIZONTAL_BORDER_SIZE[1]
        dist_from_top = Display.VERTICAL_BORDER_SIZE[0]
        dist_from_bottom = Display.DISPLAY_SIZE[1] - Display.VERTICAL_BORDER_SIZE[1]
        return dist_from_start <= pos[0] <= dist_from_end and dist_from_top <= pos[1] <= dist_from_bottom

    def get_grid_from_position(self, position: Tuple[int, int]) -> Grid:
        rows = self.TABLE_SIZE[0]
        cols = self.TABLE_SIZE[1]
        left_border = Display.HORIZONTAL_BORDER_SIZE[0]
        top_border = Display.VERTICAL_BORDER_SIZE[0]
        row = (position[1] - top_border) // rows
        col = (position[0] - left_border) // cols
        index = row * cols + col
        return self.table[index]
