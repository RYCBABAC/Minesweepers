from typing import Tuple, Optional

import pygame
from pygame.time import Clock

from entities.game_state import GameState
from entities.text import Text
from game_logic.game_state_manager import GameStateManager
from user_interface.display import Display


class TimeManager:
    TEXT_FONT = "Calibri"
    TEXT_FONT_SIZE = 50
    TEXT_ANTI_ALIAS = True
    TEXT_COLOR = (0, 0, 0)
    TEXT_POSITION = (10, 10)

    def __init__(self, display: Display, game_state_manager: GameStateManager):
        self.current_time = 0
        self.time_text = Text(self.TEXT_FONT,
                              self.TEXT_FONT_SIZE,
                              str(self.current_time),
                              self.TEXT_ANTI_ALIAS,
                              self.TEXT_COLOR,
                              self.TEXT_POSITION)
        self.display = display
        self.game_state_manager = game_state_manager
        self.timer: Optional[Clock] = None

    def update_time(self):
        if self.game_state_manager.game_state != GameState.ONGOING:
            return

        if self.timer is None:
            self.timer = pygame.time.Clock()

        self.current_time += self.timer.tick()
        self.time_text.content = str(self.current_time // 1000)
        self.display.update_text(self.time_text)
