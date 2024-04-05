import pygame

from pipelines.ui_logic_accessor import UILogicAccessor
from user_interface.drawers.display import Display
from user_interface.event_handling.button_clicked_event_handler import ButtonClickedEventHandler
from user_interface.event_handling.event_manager import EventManager
from user_interface.event_handling.game_quit_event_handler import GameQuitEventHandler
from user_interface.on_screen_objects.table import Table


class EventManagerBuilder:
    @staticmethod
    def build_event_manager(table: Table, display: Display,
                            ui_to_logic_pipeline: UILogicAccessor) -> EventManager:
        event_manager = EventManager()
        event_manager.subscribe_event(pygame.QUIT, GameQuitEventHandler())
        event_manager.subscribe_event(pygame.MOUSEBUTTONUP,
                                      ButtonClickedEventHandler(table, ui_to_logic_pipeline, display))
        return event_manager
