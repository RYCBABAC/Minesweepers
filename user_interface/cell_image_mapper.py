import os.path

import pygame
from pygame import Surface

from entities.cell_image import CellImage


class CellImageMapper:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.mapping = {image: self.load_image(image) for image in CellImage}

    def load_image(self, image: CellImage) -> Surface:
        return pygame.image.load(os.path.join(self.base_path, image.value) + ".png")

    def __getitem__(self, image: CellImage) -> Surface:
        if image not in self.mapping:
            raise KeyError("The image wasn't loaded, did you use the with statement?")
        return self.mapping[image]
