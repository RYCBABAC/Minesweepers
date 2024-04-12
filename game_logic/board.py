from typing import List

from game_logic.entities.cell import Cell
from game_logic.entities.cell_value import CellValue
from game_logic.entities.game_state import GameState


class Board:
    BOARD_SIZE = (10, 10)
    NUM_OF_MINES = 9

    def __init__(self, board: List[Cell]):
        self.board = board
        self.num_of_valid_reveals = 0
        self.is_mine_clicked = False

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        index = cell.index
        neighbors_indices = self.get_neighbors_indices(index)
        return [self.board[neighbor_index] for neighbor_index in neighbors_indices]

    def get_neighbors_indices(self, index: int):
        cols = self.BOARD_SIZE[0]
        rows = self.BOARD_SIZE[1]
        r = index // cols
        c = index % cols
        return [(r - i) * cols + c - j for i in range(-1, 2) for j in range(-1, 2)
                if 0 <= r - i < rows and 0 <= c - j < cols and (r - i) * cols + c - j != index]

    def flag_cell(self, flagged_cell: Cell) -> List[Cell]:
        if not self.should_flag(flagged_cell):
            return []

        flagged_cell.is_flagged = not flagged_cell.is_flagged
        return [flagged_cell]

    def should_flag(self, cell: Cell) -> bool:
        return self.get_game_state() == GameState.ONGOING and not cell.is_revealed

    def click_cell(self, clicked_cell: Cell) -> List[Cell]:
        if not self.should_reveal(clicked_cell):
            return []
        elif clicked_cell.value == CellValue.MINE:
            return self.user_lost_reveal(clicked_cell)
        else:
            return self.reveal(clicked_cell)

    def should_reveal(self, cell: Cell) -> bool:
        return self.get_game_state() == GameState.ONGOING and not cell.is_flagged

    def user_lost_reveal(self, cell: Cell) -> List[Cell]:
        cell.is_revealed = True
        self.is_mine_clicked = True
        return self.board

    def reveal(self, cell: Cell) -> List[Cell]:
        if cell.is_revealed:
            return []
        cell.is_revealed = True
        self.num_of_valid_reveals += 1
        if cell.value != CellValue.EMPTY:
            return [cell]

        neighbors = self.get_neighbors(cell)
        revealed_cells = []
        for neighbor in neighbors:
            if self.should_reveal_neighbor(neighbor):
                revealed_cells += self.reveal(neighbor)
        return revealed_cells + [cell]

    @staticmethod
    def should_reveal_neighbor(cell) -> bool:
        return cell.value != CellValue.MINE and not cell.is_flagged and not cell.is_revealed

    def get_game_state(self) -> GameState:
        if self.is_mine_clicked:
            return GameState.USER_LOST
        elif self.num_of_valid_reveals == self.BOARD_SIZE[0] * self.BOARD_SIZE[1] - self.NUM_OF_MINES:
            return GameState.USER_WON
        else:
            return GameState.ONGOING
