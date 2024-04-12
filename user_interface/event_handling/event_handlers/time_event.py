from typing import List, Optional

import pygame
from pygame.event import Event
from pygame.time import Clock

from user_interface.drawables.drawable import Drawable
from user_interface.drawables.text import Text
from user_interface.drawers.display import Display
from user_interface.event_handling.event_handler import EventHandler
from user_interface.logic_api.logic_api import LogicApi


class TimeEvent(EventHandler):
    def __init__(self, display: Display, logic_api: LogicApi):
        super().__init__(display)
        self.logic_api = logic_api
        self.timer: Optional[Clock] = None
        self.current_time = 0
        self.time_text = Text(
            font="Calibri",
            size=50,
            content="",
            anti_alias=True,
            color=(0, 0, 0),
            position=(0, 0))

    def process_event(self, event: Event) -> List[Drawable]:
        if self.logic_api.is_game_locked():
            return []

        if self.timer is None:
            self.timer = pygame.time.Clock()

        self.current_time += self.timer.tick()
        self.time_text.content = str(self.current_time // 1000)
        return [self.time_text]
