from enum import auto, Enum
import pygame as pg


class SoldierState(Enum):
    WAIT = auto()
    ADVANCE = auto()
    ATTACK = auto()


class Soldier(pg.sprite.Sprite):

    def __init__(self, max_hp: float, speed: float, damage: float):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.location = (1, 0)
        self.state = SoldierState.WAIT
