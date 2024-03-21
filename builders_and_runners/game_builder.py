from typing import List, Optional

from builders_and_runners.game_loop import GameLoop
from builders_and_runners.game_runner import GameRunner
from entities.cell import Cell

from entities import constants
from event_handling.cell_clicked_event_handler import CellClickedEventHandler
from event_handling.game_quit_event_handler import GameQuitEventHandler

from event_handling.game_state_manager import GameStateManager
from game_logic.auto_revealer import AutoRevealer
from game_logic.board_creator import BoardCreator
from game_logic.neighbors_accessor import NeighborsAccessor
from user_interface.cell_image_mapper import CellImageMapper
from user_interface.display import Display


class GameBuilder:
    def __init__(self):
        self.board: Optional[List[Cell]] = None
        self.display: Optional[Display] = None
        self.game_loop: Optional[GameLoop] = None
        self.neighbors_accessor: Optional[NeighborsAccessor] = None
        self.game_state_manager: Optional[GameStateManager] = None
        self.auto_revealer: Optional[AutoRevealer] = None

    def build_game(self) -> GameRunner:
        self.build_neighbors_accessor()
        self.build_board()
        self.build_display()
        self.build_auto_revealer()
        self.build_game_state_manager()
        self.build_game_loop()
        return GameRunner(self.board, self.display, self.game_loop)

    def build_neighbors_accessor(self) -> None:
        self.neighbors_accessor = NeighborsAccessor(constants.BOARD_SIZE)

    def build_board(self) -> None:
        self.board = BoardCreator(constants.BOARD_SIZE, constants.HORIZONTAL_BORDER_SIZE,
                                  constants.VERTICAL_BORDER_SIZE, constants.CELL_SIZE, constants.NUM_OF_MINES,
                                  self.neighbors_accessor).create_board()

    def build_display(self) -> None:
        self.display = Display(constants.DISPLAY_SIZE, CellImageMapper(constants.BASE_IMAGES_PATH))

    def build_auto_revealer(self) -> None:
        self.auto_revealer = AutoRevealer(self.neighbors_accessor)

    def build_game_state_manager(self) -> None:
        self.game_state_manager = GameStateManager(GameQuitEventHandler(),
                                                   CellClickedEventHandler(self.board,
                                                                           self.display, self.auto_revealer))

    def build_game_loop(self) -> None:
        self.game_loop = GameLoop(self.game_state_manager)
