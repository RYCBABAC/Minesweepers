from user_interface.drawers.display import Display
from user_interface.event_handling.event_manager import EventManager
from user_interface.on_screen_objects.table import Table


class UIRunner:
    def __init__(self, table: Table, display: Display, event_manager: EventManager):
        self.table = table
        self.display = display
        self.event_manager = event_manager

    def run_game(self):
        with self.display:
            self.initialize_game()
            self.game_loop()

    def initialize_game(self) -> None:
        self.display.update_display(self.table.table)

    def game_loop(self):
        while self.display.is_game_running:
            self.event_manager.handle_events()
            self.display.update_frame()
