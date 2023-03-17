import pygame as pg
from utils.resources import load_image
from typing import Tuple


TILE_WIDTH = 25
TILE_IMAGES_PATHS = [f"tiles/{image}.png" for image in ("empty", "road", "road-blocked")]


class Tile(pg.sprite.Sprite):

    def __init__(self, block_level: int, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        self.tile_images = [load_image(image, (TILE_WIDTH, TILE_WIDTH))[0] for image in TILE_IMAGES_PATHS]
        self.block_level = block_level

        self._set_image()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def _set_image(self):
        self.image = self.tile_images[self.block_level]
