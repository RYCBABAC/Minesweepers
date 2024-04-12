from typing import List

from pygame.event import Event

from user_interface.drawables.drawable import Drawable
from user_interface.event_handling.event_handler import EventHandler


class GameQuitEvent(EventHandler):
    def process_event(self, event: Event) -> List[Drawable]:
        self.display.is_game_running = False
        return []


