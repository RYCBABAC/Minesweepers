from typing import List

import constants
from board_creator import BoardCreator
from cell import Cell
from cell_image_mapper import CellImageMapper
from display import Display
from game_runner import GameRunner
from game_state_manager import GameStateManager


def build_display():
    cell_image_mapper = CellImageMapper(constants.BASE_IMAGES_PATH)
    return Display(constants.DISPLAY_SIZE, cell_image_mapper)


def build_board():
    board_creator = BoardCreator(constants.BOARD_SIZE, constants.HORIZONTAL_BORDER_SIZE,
                                 constants.VERTICAL_BORDER_SIZE, constants.CELL_SIZE)
    return board_creator.create_board()


def setup_display(board: List[Cell], display: Display):
    display.set_background_color(constants.BACKGROUND_COLOR)
    display.update_cells(board)


def run_game(board: List[Cell], display: Display):
    game_state_manager = GameStateManager(board, display)
    game_runner = GameRunner(game_state_manager)
    game_runner.run_game()


def run(board: List[Cell], display: Display):
    with display:
        setup_display(board, display)
        run_game(board, display)


def main():
    board = build_board()
    display = build_display()
    run(board, display)


if __name__ == "__main__":
    main()
