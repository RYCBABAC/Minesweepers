from backend.api_funcions.game_initializer.igame_initializer import IGameInitializer
from backend.api_funcions.grid_clicked_event.igrid_clicked_event import IGridClickedEvent
from backend.backend_controller.ibackend_controller import IBackendController
from backend.board_access.getter.board_getter import BoardGetter
from entities.backend_controller_response import BackendControllerResponse
from entities.game_state import GameState


class BackendController(IBackendController):
    def __init__(self, game_initializer: IGameInitializer, grid_clicked_event: IGridClickedEvent,
                 board_getter: BoardGetter, num_of_mines: int):
        self.game_initializer = game_initializer
        self.grid_clicked_event = grid_clicked_event
        self.board_getter = board_getter
        self.num_of_mines = num_of_mines

    def initialize_game(self) -> BackendControllerResponse:
        response = BackendControllerResponse()
        try:
            self.game_initializer.initialize_game(self.num_of_mines)
        except KeyError as e:
            response.game_state = GameState.FAILED
            response.error_message = f"Failed accessing grid from board with error {e}"
        except Exception as e:
            response.game_state = GameState.FAILED
            response.error_message = f"Failed with error {e}"
        finally:
            return response

    def grid_clicked_event(self, grid_index: int) -> BackendControllerResponse:
        response = BackendControllerResponse()
        try:
            grid = self.board_getter.get_from_board(grid_index)
            response.game_state, response.revealed_grids = self.grid_clicked_event.grid_clicked_event(grid)
        except KeyError as e:
            response.game_state = GameState.FAILED
            response.error_message = f"Failed accessing grid from board with error {e}"
        except Exception as e:
            response.game_state = GameState.FAILED
            response.error_message = f"Failed with error {e}"
        finally:
            return response
