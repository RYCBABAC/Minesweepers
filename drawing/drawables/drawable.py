from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame import Surface, Rect


@dataclass
class Drawable(ABC):
    rect: Rect

    @property
    @abstractmethod
    def surface(self) -> Surface:
        raise NotImplementedError

    def draw(self, surface: Surface) -> None:
        surface.blit(self.surface, self.rect)
