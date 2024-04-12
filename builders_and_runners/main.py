from game_logic.board_creator import BoardCreator
from user_interface.builders.ui_builder import UIBuilder


def main():
    board = BoardCreator.create_board()
    ui_runner = UIBuilder.build_ui(board)
    ui_runner.run_game()


if __name__ == "__main__":
    main()
