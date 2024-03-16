from dataclasses import dataclass

@dataclass
class Buttons:
    index: int
    resource_type: ResourceType = ResourceType.GRID
    rect: RectType = pygame.Rect(0, 0, 0, 0)
