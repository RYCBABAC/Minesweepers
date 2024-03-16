from backend.entities.grid import Grid
from entities.vector import Vector


class Board:
    def __init__(self,  size: Vector):
        self.size = size
        self.grids = {index: Grid(index) for index in range(0, len(self))}


    def __len__(self) -> int:
        return self.size.x * self.size.y