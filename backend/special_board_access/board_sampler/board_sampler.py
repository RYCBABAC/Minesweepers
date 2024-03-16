import random
from typing import List

from backend.board_access.counter.iboard_counter import IBoardCounter
from backend.board_access.getter.iboard_getter import IBoardGetter
from backend.entities.grid import Grid
from backend.special_board_access.board_sampler.iboard_sampler import IBoardSampler


class BoardSampler(IBoardSampler):
    def __init__(self, board_getter: IBoardGetter, board_counter: IBoardCounter):
        self.board_getter = board_getter
        self.board_counter = board_counter

    def sample_from_board(self, count: int) -> List[Grid]:
        board_size = self.board_counter.get_board_size()
        sampled_indices = random.sample(range(0, board_size), count)
        return [self.board_getter.get_from_board(index) for index in sampled_indices]
