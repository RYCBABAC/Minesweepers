from typing import Tuple, List

import pygame

from entities.cell import Cell
from entities.cell_image import CellImage
from entities.cell_value import CellValue


class BoardCreator:
    def __init__(self, game_size, horizontal_boarder_size: Tuple[int, int],
                 vertical_boarder_size: Tuple[int, int], cell_size: Tuple[int, int]):
        self.game_size = game_size
        self.horizontal_border_size = horizontal_boarder_size
        self.vertical_border_size = vertical_boarder_size
        self.cell_size = cell_size

    def create_board(self) -> List[Cell]:
        board_size = self.game_size[0] * self.game_size[1]
        return [self.create_cell(index) for index in range(0, board_size)]

    def create_cell(self, index) -> Cell:
        cell_position = self.get_cell_position(index)
        rect = pygame.Rect(cell_position, self.cell_size)
        return Cell(index=index, value=CellValue.EMPTY, image=CellImage.CELL,
                    is_revealed=False, is_flagged=False, rect=rect)

    def get_cell_position(self, index: int) -> Tuple[int, int]:
        row = int(index / self.game_size[1])
        col = index % self.game_size[1]
        cell_x_pos = self.horizontal_border_size[0] + col * self.cell_size[0]
        cell_y_pos = self.vertical_border_size[0] + row * self.cell_size[1]
        return cell_x_pos, cell_y_pos
