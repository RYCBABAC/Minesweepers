from game_logic.board_creator import BoardCreator
from pipelines.ui_logic_accessor_builder import UILogicAccessorBuilder
from user_interface.builders.ui_builder import UIBuilder


def main():
    board = BoardCreator.create_board()
    ui_logic_accessor_builder = UILogicAccessorBuilder(board)
    ui_runner = UIBuilder.build_ui(ui_logic_accessor_builder)
    ui_runner.run_game()


if __name__ == "__main__":
    main()
