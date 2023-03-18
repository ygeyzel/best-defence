from enum import auto, Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image

SOLDIER_WIDTH = 15
SOLDIER_HEIGHT = 15
MAX_HP = 100

HP_BAR_WIDTH = 15
HP_BAR_HEIGHT = 5
HP_BAR_HEIGHT_OFFSET = 5
HP_BAR_CLR = (255, 128, 0)


class SoldierState(Enum):
    ADVANCE = auto()
    ATTACK = auto()


class Soldier(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[float, float], max_hp: float, speed: float, damage: float):
        pg.sprite.Sprite.__init__(self)

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.state = SoldierState.ADVANCE
        self.pos = pos

        self.damage = 100
        self.attack_offset_flag = True
        self.animation_counter = 0
        
        self.manuverability_factor = 1

        self.image, self.rect = load_image(
            'soldiers/soldier.png', (SOLDIER_WIDTH, SOLDIER_WIDTH), (0, 0, 0))
        self.rect.x, self.rect.y = pos


    def update(self):
        if self.hp <= 0:
            self.kill_soldier()

        if not self.manuverability_factor:
            self.manuverability_factor = 1

        if self.state == SoldierState.ADVANCE:
            actual_speed = self.speed * self.manuverability_factor
            self.rect.move_ip((actual_speed, 0))

        if self.state == SoldierState.ATTACK:
            if self.animation_counter == 10:
                offset = 10 if self.attack_offset_flag else -10 
                self.rect.move_ip((offset, 0))
                self.attack_offset_flag = not self.attack_offset_flag
                self.animation_counter = 0
            else: 
                self.animation_counter += 1

    def start_movement(self):
        self.state = SoldierState.ADVANCE

    def kill_soldier(self):
        self.kill()


    def damage_castle(self, castle):
        castle.hp = castle.hp - self.damage


    def draw_hp_bar(self):
        remaining_hp_part = self.hp/self.max_hp
        hp_bar_color = [(1-remaining_hp_part) * HP_BAR_CLR[0], remaining_hp_part * HP_BAR_CLR[1], HP_BAR_CLR[2]]
        pg.draw.rect(self.image, (0, 0, 0), (0, 0, HP_BAR_WIDTH, HP_BAR_HEIGHT))
        pg.draw.rect(self.image, hp_bar_color, (0, 0, HP_BAR_WIDTH * remaining_hp_part, HP_BAR_HEIGHT))
