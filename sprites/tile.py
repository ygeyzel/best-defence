import pygame as pg
from utils.resources import load_image
from typing import Tuple


TILE_WIDTH = 25


class Tile(pg.sprite.Sprite):

    def __init__(self, block_level: int, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        self.tile_images = 3 * [load_image('tiles\\empty.png', (TILE_WIDTH, TILE_WIDTH))[0]]
        self.block_level = block_level

        self._set_image()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def _set_image(self):
        self.image = self.tile_images[self.block_level]
