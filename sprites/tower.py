from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image
from utils.common import TILE_WIDTH
import time
import os
from math import dist
from utils.common import DEFULTE_ARTILLERY_DAMAGE, IMAGES_DIR

HP_BAR_WIDTH = TILE_WIDTH
HP_BAR_HEIGHT = 5
HP_BAR_HEIGHT_OFFSET = 5
HP_BAR_CLR = (255, 128, 0)


@dataclass
class TowerStats:
    max_hp: float
    attack_delay: float
    damage: float
    attack_range: int
    tower_images_dir: str


class Tower(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[int, int], stats: TowerStats):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = stats.max_hp
        self.hp = stats.max_hp
        self.attack_delay = stats.attack_delay
        self.attack_range = stats.attack_range
        self.damage = stats.damage

        tower_images_dir = os.path.join(
            IMAGES_DIR, "towers", stats.tower_images_dir)
        images_names = os.listdir(tower_images_dir)
        self.images = [os.path.join(tower_images_dir, image)
                       for image in images_names]
        self.image, self.rect = load_image(
            self.images[0], (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos
        self.last_shot_time_stamp = time.time()

    @property
    def is_destroyed(self):
        return self.hp == 0

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
        soldier_pos_tiles = (soldier.rect.x/TILE_WIDTH,
                             soldier.rect.y/TILE_WIDTH)
        distance_to_target = dist(tower_pos_tiles, soldier_pos_tiles)
        return distance_to_target <= self.attack_range

    def update_image(self):
        num_of_non_destroyed_state_images = len(self.images) - 1
        hp_resolotion = self.max_hp / num_of_non_destroyed_state_images
        boundaries = [(i * hp_resolotion, (i + 1) * hp_resolotion)
                      for i in range(num_of_non_destroyed_state_images)].reverse()
        for image_num, (down, up) in enumerate(boundaries):
            if down < self.hp <= up:
                self.image, _ = load_image(
                    self.images[image_num], (TILE_WIDTH, TILE_WIDTH))

    def artillery_hit(self, hit_hp: int = DEFULTE_ARTILLERY_DAMAGE):
        self.hp = max(0, self.hp - hit_hp)
        self.update_image()

    def fire_management(self, soldiers):
        if (not self.is_destroyed) and self.attack_timer():
            target = self.find_target(soldiers)
            self.fire_on_target(target)

    def fire_on_target(self, target):
        if target:
            target.hp = target.hp - self.damage

    def draw_hp_bar(self):
        remaining_hp_part = max(self.hp, 0) / self.max_hp
        hp_bar_color = [(1-remaining_hp_part) * HP_BAR_CLR[0],
                        remaining_hp_part * HP_BAR_CLR[1], HP_BAR_CLR[2]]
        pg.draw.rect(self.image, (0, 0, 0),
                     (0, 0, HP_BAR_WIDTH, HP_BAR_HEIGHT))
        pg.draw.rect(self.image, hp_bar_color,
                     (0, 0, HP_BAR_WIDTH * remaining_hp_part, HP_BAR_HEIGHT))


class TowerType(Enum):
    TARGETING = TowerStats(max_hp=150, damage=20, attack_delay=0.5,
                           attack_range=5, tower_images_dir="tower-1")


def tower_factory(pos: Tuple[float, float], tower_type: TowerType) -> Tower:
    tower = Tower(pos, tower_type.value)
    return tower
