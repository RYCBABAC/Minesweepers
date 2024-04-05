from typing import List, Tuple

from game_logic.entities.cell import Cell
from game_logic.entities.game_state import GameState
from user_interface.entities.grid import Grid
from game_logic.board import Board
from user_interface.entities.ui_game_state import UIGameState
from user_interface.on_screen_objects.grid_updater import GridImageFinder
from user_interface.on_screen_objects.table import Table


class UILogicAccessor:
    def __init__(self, board: Board, table: Table):
        self.board = board
        self.table = table

    def click_grid(self, grid: Grid) -> Tuple[List[Grid], UIGameState]:
        clicked_index = grid.index
        cell = self.board.board[clicked_index]
        revealed_cells = self.board.click_cell(cell)
        print("Got revealed_cells")
        game_state = self.get_ui_game_state(self.board.get_game_state())
        print("Got game state")
        return [self.get_updated_grid(revealed_cell, game_state)
                for revealed_cell in revealed_cells], game_state

    def flag_grid(self, grid: Grid) -> Tuple[List[Grid], UIGameState]:
        flagged_index = grid.index
        grid = self.board.board[flagged_index]
        flagged_cells = self.board.flag_cell(grid)
        return [self.get_updated_grid(flagged_cell, UIGameState.ONGOING)
                for flagged_cell in flagged_cells], self.get_ui_game_state(GameState.ONGOING)

    def get_updated_grid(self, cell: Cell, game_state: UIGameState) -> Grid:
        revealed_index = cell.index
        grid = self.table.table[revealed_index]
        grid.image = GridImageFinder.find_grid_image(cell, game_state)
        return grid

    @staticmethod
    def get_ui_game_state(game_state: GameState) -> UIGameState:
        return UIGameState(game_state.value)
