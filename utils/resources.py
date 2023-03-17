import os
from typing import Optional, Tuple
import pygame as pg
from .common import IMAGES_DIR


def load_image(image_name: str, size: Optional[Tuple[float, float]] = None, colorkey: Optional[Tuple[float]] = None):
    path = os.path.join(IMAGES_DIR, image_name)
    image = pg.image.load(path)

    if size:
        image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image, image.get_rect()
