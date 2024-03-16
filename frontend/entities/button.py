from dataclasses import dataclass

import pygame
from pygame.rect import RectType

from game.entities.resource_type import ResourceType


@dataclass
class Button:
    index: int
    resource_type: ResourceType = ResourceType.GRID
    rect: RectType = pygame.Rect(0, 0, 0, 0)
