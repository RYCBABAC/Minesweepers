from enum import Enum


class GameState(Enum):
    USER_WON = "user won"
    USER_LOST = "user_lost"
    ONGOING = "ongoing"
    FAILED = "failed"
