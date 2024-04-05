import random
from typing import List

from game_logic.entities.cell import Cell
from game_logic.entities.cell_value import CellValue
from game_logic.board import Board


class BoardCreator:
    @staticmethod
    def create_board() -> Board:
        board = BoardCreator.create_empty_board()
        BoardCreator.initialize_board(board)
        return board

    @staticmethod
    def create_empty_board() -> Board:
        board_size = Board.BOARD_SIZE[0] * Board.BOARD_SIZE[1]
        return Board([BoardCreator.create_cell(index) for index in range(0, board_size)])

    @staticmethod
    def create_cell(index: int) -> Cell:
        return Cell(index=index, value=CellValue.EMPTY, is_revealed=False, is_flagged=False)

    @staticmethod
    def initialize_board(board: Board) -> None:
        mines = BoardCreator.create_mines(board)
        for mine in mines:
            BoardCreator.initialize_mine_neighbors(mine, board)

    @staticmethod
    def create_mines(empty_board: Board) -> List[Cell]:
        mines: List[Cell] = random.sample(empty_board.board, empty_board.NUM_OF_MINES)
        for mine in mines:
            mine.value = CellValue.MINE
        return mines

    @staticmethod
    def initialize_mine_neighbors(mine: Cell, board: Board) -> None:
        neighbors = board.get_neighbors(mine)
        for neighbor in neighbors:
            if neighbor.value == CellValue.EMPTY:
                neighbor.value = BoardCreator.get_cell_value(neighbor, board)

    @staticmethod
    def get_cell_value(cell: Cell, board: Board) -> CellValue:
        cell_value = sum(neighbor.value == CellValue.MINE for neighbor in board.get_neighbors(cell))
        return CellValue(cell_value)
