from enum import auto, Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image

SOLDIER_WIDTH = 15
SOLDIER_HEIGHT = 15
MAX_HP = 100


class SoldierState(Enum):
    WAIT = auto()
    ADVANCE = auto()
    ATTACK = auto()


class Soldier(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[float, float], max_hp: float, speed: float, damage: float):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.state = SoldierState.WAIT
        self.pos = pos

        self.manuverability_factor = 1

        self.image, self.rect = load_image(
            'soldiers/soldier.png', (SOLDIER_WIDTH, SOLDIER_WIDTH), (0, 0, 0))
        self.rect.x, self.rect.y = pos

    def update(self):
        if not self.manuverability_factor:
            self.manuverability_factor = 1

        if self.state == SoldierState.ADVANCE:
            actual_speed = self.speed * self.manuverability_factor
            self.rect.move_ip((actual_speed, 0))

    def start_movement(self):
        self.state = SoldierState.ADVANCE

