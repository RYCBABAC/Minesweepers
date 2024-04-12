from game_logic.board import Board
from user_interface.builders.drawer_builder import DrawerBuilder
from user_interface.builders.event_manager_builder import EventManagerBuilder
from user_interface.builders.table_creator import TableCreator
from user_interface.logic_api.logic_api import LogicApi
from user_interface.runner.ui_runner import UIRunner


class UIBuilder:
    @staticmethod
    def build_ui(board: Board) -> UIRunner:
        table = TableCreator.create_table()
        display = DrawerBuilder.build_drawer()
        logic_api = LogicApi(board, table)
        event_manager = EventManagerBuilder.build_event_manager(table, display, logic_api)
        return UIRunner(table, display, event_manager)