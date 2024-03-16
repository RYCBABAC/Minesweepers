from typing import List

from backend.board_access.counter.iboard_counter import IBoardCounter
from backend.board_access.getter.iboard_getter import IBoardGetter
from backend.entities.grid import Grid
from backend.special_board_access.neighbors_accesser.ineighbors_accesser import INeighborsAccessor


class NeighborsAccessor(INeighborsAccessor):
    def __init__(self, board_getter: IBoardGetter, board_counter: IBoardCounter):
        self.board_getter = board_getter
        self.board_counter = board_counter
        self.num_of_right_neighbors = 4
        self.num_of_left_neighbors = 4

    def get_neighbors(self, grid: Grid) -> List[Grid]:
        index = grid.index
        neighbors_indices = self.get_neighbors_indices(index)
        return [self.board_getter.get_from_board(neighbor_index) for neighbor_index in neighbors_indices]

    def get_neighbors_indices(self, index: int) -> List[int]:
        board_size = self.board_counter.get_board_size()
        rightest_neighbor = max(index - self.num_of_right_neighbors, 0)
        leftest_neighbor = min(index + self.num_of_left_neighbors, board_size - 1)
        return [neighbor for neighbor in range(rightest_neighbor, leftest_neighbor + 1) if neighbor != index]



