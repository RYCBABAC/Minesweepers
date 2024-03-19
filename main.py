import dataclasses
from typing import List

import pygame
from pygame import Surface
from pygame.rect import RectType

import constants
from board_creator import BoardCreator
from cell import Cell
from cell_image_mapper import CellImageMapper
from cell_value import CellValue
from display import Display
from game_state_manager import GameStateManager
from game_state import GameState

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

game_size = (10, 10)
numMine = 9
grid_size = (32, 32)
horizontal_border = (16, 16)
vertical_border = (100, 16)

cell_image = pygame.image.load("images/grid.png")
mine_image = pygame.image.load("images/mine.png")


def run_game(game_loop: GameStateManager):
    done = False
    while not done:
        game_states = game_loop.get_game_state()
        done = GameState.QUIT in game_states


def main():
    with CellImageMapper(constants.BASE_IMAGES_PATH) as cell_image_mapper:
        with Display(constants.DISPLAY_SIZE, cell_image_mapper) as display:
            display.set_background_color(constants.BACKGROUND_COLOR)
            board_creator = BoardCreator(constants.BOARD_SIZE, constants.HORIZONTAL_BORDER_SIZE,
                                         constants.VERTICAL_BORDER_SIZE, constants.CELL_SIZE)
            board = board_creator.create_board()
            display.update_cells(board)
            with GameStateManager(board, display) as game_state_manager:
                run_game(game_state_manager)


if __name__ == "__main__":
    main()
