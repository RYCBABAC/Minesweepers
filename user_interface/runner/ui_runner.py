from user_interface.drawers.display import Display
from user_interface.entities.ui_game_state import UIGameState
from user_interface.event_handling.event_manager import EventManager
from user_interface.on_screen_objects.table import Table


class UIRunner:
    def __init__(self, table: Table, display: Display, event_manager: EventManager):
        self.table = table
        self.display = display
        self.event_manager = event_manager

    def run_game(self):
        with self.display:
            self.display.update_grids(self.table.table)
            self.game_loop()

    def game_loop(self):
        should_stop = False
        while not should_stop:
            game_states = self.event_manager.handle_events()
            should_stop = UIGameState.QUIT in game_states
            self.display.update_frame()
