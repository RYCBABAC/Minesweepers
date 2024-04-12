from typing import Protocol

from pygame import Surface


class Drawable(Protocol):
    def draw(self, surface: Surface) -> None:
        raise NotImplementedError
