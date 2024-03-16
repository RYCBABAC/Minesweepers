from typing import TypeVar, Generic

from entities.board_element import BoardElement
from entities.vector import Vector

T = TypeVar("T", bound=BoardElement)


class Board(Generic[T]):
    def __init__(self, size: Vector):
        self.size = size
        self.grids = {index: T for index in range(0, len(self))}

    def __len__(self) -> int:
        return self.size.x * self.size.y
