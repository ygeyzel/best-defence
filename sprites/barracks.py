from dataclasses import dataclass
from typing import Tuple
import pygame as pg
from utils.resources import load_image
from utils.common import TILE_WIDTH


class Barracks(pg.sprite.Sprite):
    def __init__(self, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        barracks_image = "tiles/barracks.png"
        self.image, self.rect = load_image(barracks_image, (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos

def barracks_factory(pos: Tuple[float, float], _) -> Barracks:
    barracks = Barracks(pos)
    return barracks
