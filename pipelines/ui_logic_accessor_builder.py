from game_logic.board import Board
from pipelines.ui_logic_accessor import UILogicAccessor
from user_interface.on_screen_objects.table import Table


class UILogicAccessorBuilder:
    def __init__(self, board: Board):
        self.board = board

    def build_accessor(self, table: Table) -> UILogicAccessor:
        return UILogicAccessor(self.board, table)
