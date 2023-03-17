from dataclasses import dataclass
from enum import auto, Enum
from typing import Tuple, TypedDict
import pygame as pg
from utils.resources import load_image
import time

SHOOT = 1
DONT_SHOOT = 0


@dataclass
class TowerStats:
    max_hp: float
    attack_delay: float
    damage: float
    attack_range: int
    tower_image: str


class Tower(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[int, int], stats: TowerStats):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = stats.max_hp
        self.hp = stats.max_hp
        self.attack_delay = stats.attack_delay
        self.attack_range = stats.attack_range

        tower_image = f"towers/{stats.tower_image}"
        self.image, self.rect = load_image(tower_image)
        self.rect.x, self.rect.y = pos
        self.last_shot_time_stamp = time.time()

    def attack_timer(self):
        current_time = time.time()
        delta_time = current_time - self.last_shot_time_stamp
        if delta_time >= self.attack_delay:
            self.last_shot_time_stamp = current_time
            return self.fire()
        else:
            return DONT_SHOOT

    def update(self):
        self.attack_timer()

    def fire(self):
        return print("SHOOT!")


class TowerType(Enum):
    TARGETING = TowerStats(max_hp=150, damage=20, attack_delay=0.5,
                           attack_range=5, tower_image="tower-1.png")


def tower_factory(pos: Tuple[float, float], tower_type: TowerType) -> Tower:
    tower = Tower(pos, tower_type.value)
    return tower

