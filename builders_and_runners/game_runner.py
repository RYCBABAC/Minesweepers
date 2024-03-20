from typing import List

from builders_and_runners.game_loop import GameLoop
from entities import constants
from entities.cell import Cell
from user_interface.display import Display


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
