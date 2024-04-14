from pygame import Surface

from user_interface.drawables.drawable import Drawable


class Border(Drawable):
    BACKGROUND_COLOR = (192, 192, 192)

    @property
    def surface(self) -> Surface:
        surface = Surface(self.rect.size)
        surface.fill(self.BACKGROUND_COLOR)
        return surface

