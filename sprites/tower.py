from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image
from utils.common import TILE_WIDTH
import time
from math import dist


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
        self.damage = stats.damage

        tower_image = f"towers/{stats.tower_image}"
        self.image, self.rect = load_image(tower_image, (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos
        self.last_shot_time_stamp = time.time()

    def attack_timer(self):
        current_time = time.time()
        delta_time = current_time - self.last_shot_time_stamp
        if delta_time >= self.attack_delay:
            self.last_shot_time_stamp = current_time
            return True
        else:
            return False

    def find_target(self, soldiers):
        valid_targets = self.find_valid_targets(soldiers)
        max_x_position = 0
        for valid_target in valid_targets:
            if valid_target.rect.x > max_x_position:
                max_x_position = valid_target.rect.x
                target = valid_target
        if max_x_position > 0:
            return target

    def find_valid_targets(self, soldiers):
        valid_targets = pg.sprite.Group()
        for soldier in soldiers:
            if self.is_soldier_valid_target(soldier):
                valid_targets.add(soldier)
        return valid_targets

    def is_soldier_valid_target(self, soldier):
        tower_pos_tiles = (self.rect.x/TILE_WIDTH, self.rect.y/TILE_WIDTH)
        soldier_pos_tiles = (soldier.rect.x/TILE_WIDTH, soldier.rect.y/TILE_WIDTH)
        distance_to_target = dist(tower_pos_tiles, soldier_pos_tiles)
        if distance_to_target <= self.attack_range:
            return True
        else:
            return False

    def fire_management(self, soldiers):
        if self.attack_timer():
            target = self.find_target(soldiers)
            self.fire_on_target(target)
        else:
            pass

    def fire_on_target(self, target):
        if target:
            target.hp = target.hp - self.damage
            # TO DO: CHECK SOLDIER IS ALIVE?

    def update(self):
        pass

class TowerType(Enum):
    TARGETING = TowerStats(max_hp=150, damage=20, attack_delay=0.5,
                           attack_range=5, tower_image="tower-1.png")


def tower_factory(pos: Tuple[float, float], tower_type: TowerType) -> Tower:
    tower = Tower(pos, tower_type.value)
    return tower

