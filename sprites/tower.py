import pygame as pg
from typing import Tuple
from utils.resources import load_image


class Tower(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[int, int], max_hp: float, attack_rate: float, damage: float, attack_range: int, tower_image: str):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_rate = attack_rate
        self.range = attack_range

        self.image, self.rect = load_image(tower_image)
        self.rect.x, self.rect.y = pos
