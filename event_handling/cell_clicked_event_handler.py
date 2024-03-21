from typing import List, Tuple, Optional

from pygame.event import Event

from entities.cell import Cell
from entities.cell_image import CellImage
from entities.cell_value import CellValue
from entities.game_state import GameState
from event_handling.ievent_handler import IEventHandler
from user_interface.display import Display


class CellClickedEventHandler(IEventHandler):
    def __init__(self, board: List[Cell], display: Display):
        self.board = board
        self.display = display

    def handle_event(self, event: Event) -> GameState:
        clicked_pos = event.pos
        cell = self.get_clicked_cell(clicked_pos)
        if cell is None:
            return GameState.ONGOING

        CellClickedEventHandler.update_cell(event, cell)
        self.display.update_cells([cell])
        return GameState.ONGOING

    def get_clicked_cell(self, clicked_pos: Tuple[int, int]) -> Optional[Cell]:
        for cell in self.board:
            if cell.rect.collidepoint(clicked_pos):
                return cell
        return None

    @staticmethod
    def update_cell(event: Event, cell: Cell) -> None:
        if event.button == 1 and not cell.is_flagged:  # Left click
            CellClickedEventHandler.reveal_cell(cell)
        elif event.button == 3:  # Right click
            CellClickedEventHandler.flag_cell(cell)

    @staticmethod
    def reveal_cell(cell: Cell) -> None:
        if cell.is_revealed:
            return
        elif cell.value == CellValue.MINE:
            cell.image = CellImage.MINE
        elif cell.value == CellValue.EMPTY:
            cell.image = CellImage.EMPTY
        else:
            cell.image = CellImage(f"grid{cell.value.value}")
        cell.is_revealed = not cell.is_revealed

    @staticmethod
    def flag_cell(cell: Cell) -> None:
        cell.is_flagged = not cell.is_flagged
        cell.image = CellImage.FLAG if cell.is_flagged else CellImage.CELL
