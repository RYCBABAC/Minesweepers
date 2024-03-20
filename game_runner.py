from typing import List

import constants
from cell import Cell
from display import Display
from game_loop import GameLoop


class GameRunner:
    def __init__(self, board: List[Cell], display: Display, game_loop: GameLoop):
        self.board = board
        self.display = display
        self.game_loop = game_loop

    def run_game(self):
        with self.display:
            self.setup_display()
            self.game_loop.run_game()

    def setup_display(self):
        self.display.set_background_color(constants.BACKGROUND_COLOR)
        self.display.update_cells(self.board)
