import pygame as pg
from sprites.dice import Face, FaceType


class Dashboard(pg.sprite.Sprite):
    def __init__(self, rolls: int = 20, artillery: int = 0, engineering: int = 0, recruitment: int = 0):
        self.rolls = rolls
        self.artillery = artillery
        self.engineering = engineering
        self.recruitment = recruitment

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
