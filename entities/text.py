from dataclasses import dataclass
from typing import Tuple

from pygame.rect import RectType


@dataclass
class Text:
    font: str
    size: int
    content: str
    anti_alias: bool
    color: Tuple[int, int, int]
    position: Tuple[int, int]
