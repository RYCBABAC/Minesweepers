from typing import List

from builders_and_runners.game_loop import GameLoop
from builders_and_runners.game_runner import GameRunner
from entities.cell import Cell

from entities import constants

from event_handling.game_state_manager import GameStateManager
from game_logic.board_creator import BoardCreator
from user_interface.cell_image_mapper import CellImageMapper
from user_interface.display import Display


class GameBuilder:
    @staticmethod
    def build_game() -> GameRunner:
        board = GameBuilder.build_board()
        display = GameBuilder.build_display()
        game_loop = GameBuilder.build_game_loop(board, display)
        return GameRunner(board, display, game_loop)

    @staticmethod
    def build_board() -> List[Cell]:
        board_creator = BoardCreator(constants.BOARD_SIZE, constants.HORIZONTAL_BORDER_SIZE,
                                     constants.VERTICAL_BORDER_SIZE, constants.CELL_SIZE)
        return board_creator.create_board()

    @staticmethod
    def build_display() -> Display:
        cell_image_mapper = CellImageMapper(constants.BASE_IMAGES_PATH)
        return Display(constants.DISPLAY_SIZE, cell_image_mapper)

    @staticmethod
    def build_game_loop(board: List[Cell], display: Display) -> GameLoop:
        game_state_manager = GameStateManager(board, display)
        return GameLoop(game_state_manager)
