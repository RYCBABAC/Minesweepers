from entities.cell import Cell
from entities.cell_image import CellImage
from entities.cell_value import CellValue
from entities.update_type import CellUpdateType


class CellUpdater:
    @staticmethod
    def update_cell(cell: Cell, update_type: CellUpdateType) -> None:
        if update_type == CellUpdateType.REVEAL:
            CellUpdater.reveal_cell(cell)
        elif update_type == CellUpdateType.LOST_REVEAL:
            CellUpdater.lost_reveal_cell(cell)
        elif update_type == CellUpdateType.FLAG:
            CellUpdater.flag_cell(cell)

    @staticmethod
    def reveal_cell(cell: Cell) -> None:
        if cell.is_revealed or cell.is_flagged:
            return
        elif cell.value == CellValue.MINE:
            cell.image = CellImage.MINE
        elif cell.value == CellValue.EMPTY:
            cell.image = CellImage.EMPTY
        else:
            cell.image = CellImage(f"grid{cell.value.value}")
        cell.is_revealed = not cell.is_revealed

    @staticmethod
    def lost_reveal_cell(cell: Cell) -> None:
        if cell.is_revealed and cell.value == CellValue.MINE:
            cell.image = CellImage.MINE_CLICKED
        elif cell.value == CellValue.MINE:
            cell.image = CellImage.MINE
        elif cell.is_flagged:
            cell.image = CellImage.MINE_FALSE
        elif cell.value == CellValue.EMPTY:
            cell.image = CellImage.EMPTY
        else:
            cell.image = CellImage(f"grid{cell.value.value}")
        cell.is_revealed = not cell.is_revealed

    @staticmethod
    def flag_cell(cell: Cell) -> None:
        cell.is_flagged = not cell.is_flagged
        cell.image = CellImage.FLAG if cell.is_flagged else CellImage.CELL
