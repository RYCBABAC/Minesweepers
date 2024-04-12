import os.path

import pygame
from pygame import Surface

from user_interface.entities.grid_image import GridImage


class GridImageMapper:
    BASE_IMAGES_PATH = "images"
    IMAGES_EXTENSION = ".png"

    def __init__(self):
        self.mapping = {image: self.load_image(image) for image in GridImage}

    def load_image(self, image: GridImage) -> Surface:
        return pygame.image.load(os.path.join(self.BASE_IMAGES_PATH, image.value) + self.IMAGES_EXTENSION)

    def __getitem__(self, image: GridImage) -> Surface:
        if image not in self.mapping:
            raise KeyError("The image wasn't loaded, did you use the with statement?")
        return self.mapping[image]
