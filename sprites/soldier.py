from enum import auto, Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image

SOLDIER_WIDTH = 25
MAX_HP = 100

class SoldierState(Enum):
    WAIT = auto()
    ADVANCE = auto()
    ATTACK = auto()


class Soldier(pg.sprite.Sprite):

    def __init__(self, max_hp: float, speed: float, damage: float, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.location = (1, 0)
        self.state = SoldierState.WAIT
        self.pos = pos

        self.tile_images = [load_image('soldier\\empty.png', (SOLDIER_WIDTH, SOLDIER_WIDTH))[0]]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
