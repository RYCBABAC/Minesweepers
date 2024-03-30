from typing import Tuple

import pygame

from entities.cell import Cell
from entities.cell_image import CellImage
from entities.cell_value import CellValue
from game_logic.board import Board
from user_interface.display import Display


class CellCreator:

    @staticmethod
    def create_cell(index: int) -> Cell:
        cell_position = CellCreator.get_cell_position(index)
        rect = pygame.Rect(cell_position, Cell.CELL_SIZE)
        return Cell(index=index, value=CellValue.EMPTY, image=CellImage.CELL,
                    is_revealed=False, is_flagged=False, rect=rect)

    @staticmethod
    def get_cell_position(index: int) -> Tuple[int, int]:
        row = index // Board.BOARD_SIZE[1]
        col = index % Board.BOARD_SIZE[1]
        cell_x_pos = Display.HORIZONTAL_BORDER_SIZE[0] + col * Cell.CELL_SIZE[0]
        cell_y_pos = Display.VERTICAL_BORDER_SIZE[0] + row * Cell.CELL_SIZE[1]
        return cell_x_pos, cell_y_pos
