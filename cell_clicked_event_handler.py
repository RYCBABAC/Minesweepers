from typing import List, Tuple, Optional

from pygame.event import Event

from cell import Cell
from cell_image import CellImage
from display import Display
from game_state import GameState
from ievent_handler import IEventHandler


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

    def update_cell(self, cell: Cell) -> None:
        cell.image = CellImage.CELL if cell.is_revealed else CellImage.MINE
        cell.is_revealed = not cell.is_revealed

