import pygame as pg
from typing import Tuple


class Tower(pg.sprite.Sprite):

    def __init__(self, max_hp: float, attack_rate: float, damage: float, location: Tuple[int, int], attack_range: int):
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_rate = attack_rate
        self.location = location
        self.range = attack_range
