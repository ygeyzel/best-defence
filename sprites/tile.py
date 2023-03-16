import pygame as pg


TILE_WIDTH = 5


class Tile(pg.sprite.Sprite):

    def __init__(self, block_level: int):
        self.block_level = block_level
