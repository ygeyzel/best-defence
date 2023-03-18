import pygame as pg
from sprites.dice import Face, FaceType
from utils.common import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.resources import load_image
from pygame import font


class Dashboard(pg.sprite.Sprite):
    def __init__(self, rolls: int = 20, artillery: int = 0, engineering: int = 0, recruitment: int = 0):
        pg.sprite.Sprite.__init__(self)
        self.rolls = rolls
        self.artillery = artillery
        self.engineering = engineering
        self.recruitment = recruitment

        self.textFont = font.SysFont("monospace", 15)

        position = (0, 280)

        self.image, self.rect = load_image('dashboard/dashboard.png', (SCREEN_WIDTH, 120))
        self.rect.x, self.rect.y = position


    def __repr__(self):
        return f'Dashboard(rolls:{self.rolls}, artillery:{self.artillery}, engineering:{self.engineering}, recruitment:{self.recruitment})'

    @property
    def is_can_roll(self):
        return self.rolls > 0

    @property
    def is_can_artillery(self):
        return self.artillery > 0

    @property
    def is_can_engineering(self):
        return self.engineering > 0

    @property
    def is_can_recruitment(self):
        return self.recruitment > 0

    def update_up_by_dice_face(self, face: Face):
        match face.face_type:
            case FaceType.ARTILLERY:
                self.artillery += face.power_num

            case FaceType.ENGINEERING:
                self.engineering += face.power_num

            case FaceType.RECRUITMENT:
                self.recruitment += face.power_num

    def update(self):
        artillery_serf = self.textFont.render(f"Artillery: {self.artillery}", 1, (255, 255, 255))
        recruitment_serf = self.textFont.render(f"Recruitment: {self.recruitment}", 1, (255, 255, 255))
        engineering_serf = self.textFont.render(f"Engineering: {self.engineering}", 1, (255, 255, 255))
        dice_amount_serf = self.textFont.render(f"Available Dice: {self.rolls}", 1, (255, 255, 255))

        self.image.blit(artillery_serf, (90,90))
        self.image.blit(recruitment_serf, (340, 90))
        self.image.blit(engineering_serf, (540, 90))
        self.image.blit(dice_amount_serf, (75, 20))

