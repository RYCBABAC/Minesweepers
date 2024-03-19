import dataclasses
from typing import List

import pygame
from pygame import Surface
from pygame.rect import RectType

import constants
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


@dataclasses.dataclass
class Cell:
    index: int
    rect: RectType
    is_revealed: bool


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


def add_buttons_to_display(game_display: Surface) -> List[Cell]:
    cells = []
    for index in range(0, game_size[0] * game_size[1]):
        row = int(index / game_size[1])
        col = index % game_size[1]
        rect = pygame.Rect(horizontal_border[0] + col * grid_size[0], vertical_border[0] + row * grid_size[1],
                           grid_size[0], grid_size[1])
        game_display.blit(cell_image, rect)
        cells.append(Cell(index, rect, False))
    pygame.display.update()
    return cells


def main():
    with Display(constants.DISPLAY_SIZE) as display:
        display.set_background_color(constants.BACKGROUND_COLOR)
        cells = add_buttons_to_display(display.display)
        game_loop(display.display, cells)


if __name__ == "__main__":
    main()
