from backend.api_funcions.game_initializer.igame_initializer import IGameInitializer
from backend.special_board_update.grids_initializer.igrids_initializer import IGridsInitializer
from backend.special_board_update.mines_creator.imines_creator import IMinesCreator


class GameInitializer(IGameInitializer):
    def __init__(self, mines_creator: IMinesCreator, grids_initializer: IGridsInitializer):
        self.mines_creator = mines_creator
        self.grids_initializer = grids_initializer

    def initialize_game(self, num_of_mines: int) -> None:
        mines = self.mines_creator.create_mines(num_of_mines)
        self.grids_initializer.initialize_grids(mines)


