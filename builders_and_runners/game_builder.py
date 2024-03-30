from builders_and_runners.game_loop import GameLoop
from builders_and_runners.game_runner import GameRunner
from event_handling.button_clicked_event_handler import ButtonClickedEventHandler
from event_handling.event_manager import EventManager
from event_handling.game_quit_event_handler import GameQuitEventHandler
from game_logic.board_creator import BoardCreator
from game_logic.cell_clicked_event import CellClickedEvent
from game_logic.cell_flagged_event import CellFlaggedEvent
from game_logic.game_state_manager import GameStateManager
from user_interface.cell_image_mapper import CellImageMapper
from user_interface.display import Display
from user_interface.time_manager import TimeManager


class GameBuilder:

    @staticmethod
    def build_game() -> GameRunner:
        board = BoardCreator.create_board()
        cell_image_mapper = CellImageMapper()
        display = Display(cell_image_mapper)
        game_state_manager = GameStateManager()

        cell_clicked_event = CellClickedEvent(board, display, game_state_manager)
        cell_flagged_event = CellFlaggedEvent(display, game_state_manager)
        event_manager = EventManager(GameQuitEventHandler(game_state_manager),
                                     ButtonClickedEventHandler(board, cell_clicked_event, cell_flagged_event))
        time_manager = TimeManager(display, game_state_manager)
        game_loop = GameLoop(event_manager, game_state_manager, time_manager)
        return GameRunner(board, display, game_loop)
