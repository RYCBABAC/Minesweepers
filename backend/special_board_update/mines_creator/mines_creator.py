from typing import List

from backend.board_access.updater.iboard_updater import IBoardUpdater
from backend.entities.grid import Grid
from backend.entities.grid_type import GridType
from backend.special_board_access.board_sampler.iboard_sampler import IBoardSampler
from backend.special_board_update.mines_creator.imines_creator import IMinesCreator


class MinesCreator(IMinesCreator):
    def __init__(self, board_updater: IBoardUpdater, board_sampler: IBoardSampler):
        self.board_updater = board_updater
        self.board_sampler = board_sampler

    def create_mines(self, num_of_mines: int) -> List[Grid]:
        mines = self.board_sampler.sample_from_board(num_of_mines)
        for mine in mines:
            mine.type = GridType.MINE
            self.board_updater.update_board(mine)
        return mines
