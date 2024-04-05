from enum import Enum


class GameState(Enum):
    ONGOING = "ongoing"
    USER_WON = "user_won"
    USER_LOST = "user_lost"
