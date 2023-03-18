from enum import auto, Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image

SOLDIER_WIDTH = 15
SOLDIER_HEIGHT = 15
MAX_HP = 100

HP_BAR_WIDTH = 15
HP_BAR_HEIGHT = 5
HP_BAR_HEIGHT_OFFSET = 10
HP_BAR_CLR = (255, 128, 0)


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
        if self.hp <= 0:
            self.kill_soldier()

        if not self.manuverability_factor:
            self.manuverability_factor = 1

        if self.state == SoldierState.ADVANCE:
            actual_speed = self.speed * self.manuverability_factor
            self.rect.move_ip((actual_speed, 0))

    def start_movement(self):
        self.state = SoldierState.ADVANCE

    def kill_soldier(self):
        self.kill()

    def draw_hp_bar(self, screen):
        remaining_hp_part = self.hp/self.max_hp
        hp_bar_color = [(1-remaining_hp_part) * HP_BAR_CLR[0], remaining_hp_part * HP_BAR_CLR[1], HP_BAR_CLR[2]]
        pg.draw.rect(screen, hp_bar_color, (self.rect.x, self.rect.y - HP_BAR_HEIGHT_OFFSET,
                                            HP_BAR_WIDTH * remaining_hp_part, HP_BAR_HEIGHT))

