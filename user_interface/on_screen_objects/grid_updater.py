from game_logic.entities.cell import Cell
from user_interface.entities.grid_image import GridImage
from game_logic.entities.cell_value import CellValue
from user_interface.entities.ui_game_state import UIGameState


class GridImageFinder:
    @staticmethod
    def find_grid_image(cell: Cell, game_state: UIGameState) -> GridImage:
        return GridImageFinder.find_grid_image_ongoing(cell) \
            if game_state == UIGameState.ONGOING else GridImageFinder.find_grid_image_finished(cell)

    @staticmethod
    def find_grid_image_ongoing(cell: Cell) -> GridImage:
        if not cell.is_revealed:
            return GridImage.CELL
        elif cell.is_flagged:
            return GridImage.FLAG
        elif cell.value == CellValue.MINE:
            return GridImage.MINE_CLICKED
        elif cell.value == CellValue.EMPTY:
            return GridImage.EMPTY
        else:
            return GridImage(f"grid{cell.value.value}")

    @staticmethod
    def find_grid_image_finished(cell: Cell) -> GridImage:
        if cell.is_revealed and cell.value == CellValue.MINE:
            return GridImage.MINE_CLICKED
        elif cell.value == CellValue.MINE:
            return GridImage.MINE
        elif cell.is_flagged:
            return GridImage.MINE_FALSE
        elif cell.value == CellValue.EMPTY:
            return GridImage.EMPTY
        else:
            return GridImage(f"grid{cell.value.value}")
