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

        self.update_cell(cell)
        self.display.update_cells([cell])
        return GameState.ONGOING

    def get_clicked_cell(self, clicked_pos: Tuple[int, int]) -> Optional[Cell]:
        for cell in self.board:
            if cell.rect.collidepoint(clicked_pos):
                return cell
        return None

    @staticmethod
    def update_cell(cell: Cell) -> None:
        if cell.is_revealed:
            cell.image = CellImage.CELL
        elif cell.value == CellValue.MINE:
            cell.image = CellImage.MINE
        else:
            cell.image = CellImage.EMPTY
        cell.is_revealed = not cell.is_revealed
