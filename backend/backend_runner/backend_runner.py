from backend.api_funcions.game_initializer.game_initializer import GameInitializer
from backend.api_funcions.grid_clicked_event.grid_clicked_event import GridClickedEvent
from backend.backend_controller.backend_controller import BackendController
from backend.backend_controller.ibackend_controller import IBackendController
from backend.board_access.board.board import Board
from backend.board_access.counter.board_counter import BoardCounter
from backend.board_access.getter.board_getter import BoardGetter
from backend.board_access.updater.board_updater import BoardUpdater
from backend.board_access.win_checker.win_checker import WinChecker
from backend.special_board_access.board_sampler.board_sampler import BoardSampler
from backend.special_board_access.neighbors_accesser.neighbros_accessor import NeighborsAccessor
from backend.special_board_update.auto_revealer.auto_revealer import AutoRevealer
from backend.special_board_update.grids_initializer.grids_initializer import GridsInitializer
from backend.special_board_update.mines_creator.mines_creator import MinesCreator
from utils.runner.runner import Runner


class BackendRunner(Runner):
    def __init__(self):
        super().__init__()
        self.num_of_mines = 5

    def run(self) -> IBackendController:
        board = Board(self.board_size)
        board_getter = BoardGetter(board)
        board_updater = BoardUpdater(board)
        board_counter = BoardCounter(board)
        win_checker = WinChecker(board)
        board_sampler = BoardSampler(board_getter, board_counter)
        neighbors_accessor = NeighborsAccessor(board_getter, board_counter)
        mines_creator = MinesCreator(board_updater, board_sampler)
        grids_initializer = GridsInitializer(board_updater, neighbors_accessor)
        auto_revealer = AutoRevealer(board_updater, neighbors_accessor)
        game_initializer = GameInitializer(mines_creator, grids_initializer)
        grid_clicked_event = GridClickedEvent(win_checker, auto_revealer)
        return BackendController(game_initializer, grid_clicked_event, board_getter, self.num_of_mines)
