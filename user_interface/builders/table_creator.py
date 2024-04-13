from typing import Tuple

import pygame

from user_interface.entities.grid_image import GridImage
from user_interface.drawables.grid import Grid
from user_interface.drawers.display import Display
from user_interface.on_screen_objects.table import Table


class TableCreator:
    @staticmethod
    def create_table() -> Table:
        table_size = Table.TABLE_SIZE[0] * Table.TABLE_SIZE[1]
        return Table([TableCreator.create_grid(index) for index in range(0, table_size)])

    @staticmethod
    def create_grid(index: int) -> Grid:
        cell_position = TableCreator.get_grid_position(index)
        rect = pygame.Rect(cell_position, Grid.GRID_SIZE)
        return Grid(index=index, image=GridImage.CELL, rect=rect)

    @staticmethod
    def get_grid_position(index: int) -> Tuple[int, int]:
        row = index // Table.TABLE_SIZE[1]
        col = index % Table.TABLE_SIZE[1]
        cell_x_pos = Display.HORIZONTAL_BORDER_SIZE[0] + col * Grid.GRID_SIZE[0]
        cell_y_pos = Display.VERTICAL_BORDER_SIZE[0] + row * Grid.GRID_SIZE[1]
        return cell_x_pos, cell_y_pos
