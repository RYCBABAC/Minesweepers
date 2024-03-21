from enum import Enum


class CellUpdateType(Enum):
    REVEAL = 1
    LOST_REVEAL = 2
    FLAG = 3
