from enum import Enum


class UIGameState(Enum):
    ONGOING = "ongoing"
    USER_WON = "user_won"
    USER_LOST = "user_lost"
    QUIT = "quit"
