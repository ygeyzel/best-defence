from dataclasses import dataclass
from enum import auto, Enum
from typing import Tuple, TypedDict
import pygame as pg
from utils.resources import load_image


@dataclass
class TowerStats:
    max_hp: float
    attack_rate: float
    damage: float
    attack_range: int
    tower_image: str


class Tower(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[int, int], stats: TowerStats):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = stats.max_hp
        self.hp = stats.max_hp
        self.attack_rate = stats.attack_rate
        self.range = stats.attack_range

        tower_image = f"towers/{stats.tower_image}"
        self.image, self.rect = load_image(tower_image)
        self.rect.x, self.rect.y = pos


class TowerType(Enum):
    TARGETING = TowerStats(max_hp=150, damage=20, attack_rate=10,
                           attack_range=5, tower_image="tower-1.png")


def tower_factory(pos: Tuple[float, float], tower_type: TowerType) -> Tower:
    tower = Tower(pos, tower_type.value)
    return tower
