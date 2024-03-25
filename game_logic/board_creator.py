import random
from typing import Tuple, List

import pygame

from entities.cell import Cell
from entities.cell_image import CellImage
from entities.cell_value import CellValue
from game_logic.neighbors_accessor import NeighborsAccessor


class BoardCreator:
    def __init__(self, game_size, horizontal_boarder_size: Tuple[int, int], vertical_boarder_size: Tuple[int, int],
                 cell_size: Tuple[int, int], num_of_mines: int, neighbors_accessor: NeighborsAccessor):
        self.game_size = game_size
        self.horizontal_border_size = horizontal_boarder_size
        self.vertical_border_size = vertical_boarder_size
        self.cell_size = cell_size
        self.num_of_mines = num_of_mines
        self.neighbors_accessor = neighbors_accessor

    def create_board(self) -> List[Cell]:
        board_size = self.game_size[0] * self.game_size[1]
        board = [self.create_cell(index) for index in range(0, board_size)]
        mines = self.create_mines(board)
        self.set_cells_values(board, mines)
        return board

    def create_cell(self, index) -> Cell:
        cell_position = self.get_cell_position(index)
        rect = pygame.Rect(cell_position, self.cell_size)
        return Cell(index=index, value=CellValue.EMPTY, image=CellImage.CELL,
                    is_revealed=False, is_flagged=False, rect=rect)

    def get_cell_position(self, index: int) -> Tuple[int, int]:
        row = index // self.game_size[1]
        col = index % self.game_size[1]
        cell_x_pos = self.horizontal_border_size[0] + col * self.cell_size[0]
        cell_y_pos = self.vertical_border_size[0] + row * self.cell_size[1]
        return cell_x_pos, cell_y_pos

    def create_mines(self, empty_board: List[Cell]) -> List[Cell]:
        mines: List[Cell] = random.sample(empty_board, self.num_of_mines)
        for mine in mines:
            mine.value = CellValue.MINE
        return mines

    def set_cells_values(self, board: List[Cell], mines: List[Cell]):
        for mine in mines:
            neighbors = self.neighbors_accessor.get_neighbors(mine, board)
            for neighbor in neighbors:
                if neighbor.value == CellValue.EMPTY:
                    neighbor.value = self.get_cell_value(neighbor, board)

    def get_cell_value(self, cell: Cell, board: List[Cell]) -> CellValue:
        return CellValue(sum(neighbor.value == CellValue.MINE
                          for neighbor in self.neighbors_accessor.get_neighbors(cell, board)))