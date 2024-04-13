import os.path

import pygame
from pygame import Surface

from user_interface.entities.grid_image import GridImage

BASE_IMAGES_PATH = "images"
IMAGES_EXTENSION = ".png"

images = {}


def __load_image(image: GridImage) -> None:
    image_path = os.path.join(BASE_IMAGES_PATH, image.value) + IMAGES_EXTENSION
    if not os.path.exists(image_path):
        raise KeyError("Image is not found")
    images[image] = pygame.image.load(image_path)


def get_grid_image(image: GridImage) -> Surface:
    if image not in images:
        __load_image(image)
    return images[image]

