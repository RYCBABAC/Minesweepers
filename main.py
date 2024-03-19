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

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

game_size = (10, 10)
numMine = 9
grid_size = (32, 32)
horizontal_border = (16, 16)
vertical_border = (100, 16)

cell_image = pygame.image.load("images/grid.png")
mine_image = pygame.image.load("images/mine.png")


def game_loop(game_display: Surface, cells: List[Cell]):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked_pos = event.pos
                for cell in cells:
                    if cell.rect.collidepoint(clicked_pos):
                        new_image = cell_image if cell.is_revealed else mine_image
                        game_display.blit(new_image, cell.rect)
                        pygame.display.update()
                        cell.is_revealed = not cell.is_revealed


def main():
    with CellImageMapper(constants.BASE_IMAGES_PATH) as cell_image_mapper:
        with Display(constants.DISPLAY_SIZE, cell_image_mapper) as display:
            display.set_background_color(constants.BACKGROUND_COLOR)
            board_creator = BoardCreator(constants.BOARD_SIZE, constants.HORIZONTAL_BORDER_SIZE,
                                         constants.VERTICAL_BORDER_SIZE, constants.CELL_SIZE)
            cells = board_creator.create_board()
            display.update_cells(cells)
            game_loop(display.display, cells)


if __name__ == "__main__":
    main()
