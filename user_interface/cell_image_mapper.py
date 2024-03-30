import os.path

import pygame
from pygame import Surface

from entities.cell_image import CellImage


class CellImageMapper:
    BASE_IMAGES_PATH = "images"
    IMAGES_EXTENSION = ".png"

    def __init__(self):
        self.mapping = {image: self.load_image(image) for image in CellImage}

    def load_image(self, image: CellImage) -> Surface:
        return pygame.image.load(os.path.join(self.BASE_IMAGES_PATH, image.value) + self.IMAGES_EXTENSION)

    def __getitem__(self, image: CellImage) -> Surface:
        if image not in self.mapping:
            raise KeyError("The image wasn't loaded, did you use the with statement?")
        return self.mapping[image]
