import pygame as pg
from sprites.dice import Face, FaceType
from utils.common import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.resources import load_image
from pygame import font


class RollButton(pg.sprite.Sprite):
    def __init__(self, position: tuple = (735,300)):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('dashboard/roll_btn.png', (210, 50))
        self.rect.x, self.rect.y = position

    # def CTA:
