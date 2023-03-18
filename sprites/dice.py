import pygame as pg
from enum import auto, Enum
from dataclasses import dataclass
import random


class FaceType(Enum):
    ARTILLERY = auto()
    ENGINEERING = auto()
    RECRUITMENT = auto()


@dataclass
class Face:
    face_type: FaceType
    power_num: int = 1


class Dice(pg.sprite.Sprite):
    def __init__(self, faces: list[Face]):
        self.faces = faces

    def __repr__(self):
        return f'Dice({self.faces})'

    def roll(self):
        return random.choice(self.faces)


class DiceType(Enum):
    FLAT = auto()
    ARTILLERY_HEAVY = auto()
    ENGINEERING_HEAVY = auto()
    RECRUITMENT_HEAVY = auto()


def dice_factory(dice_type: DiceType):
    dice_faces = {
        DiceType.FLAT: [Face(FaceType.ARTILLERY), Face(FaceType.ARTILLERY, 2),
                        Face(FaceType.ENGINEERING), Face(FaceType.ENGINEERING, 2),
                        Face(FaceType.RECRUITMENT), Face(FaceType.RECRUITMENT, 2)],

        DiceType.ARTILLERY_HEAVY: [Face(FaceType.ARTILLERY, 3), Face(FaceType.ARTILLERY, 2),
                                   Face(FaceType.ARTILLERY, 2), Face(FaceType.ARTILLERY, 1),
                                   Face(FaceType.ENGINEERING), Face(FaceType.RECRUITMENT)],

        DiceType.ENGINEERING_HEAVY: [Face(FaceType.ENGINEERING, 3), Face(FaceType.ENGINEERING, 2),
                                     Face(FaceType.ENGINEERING, 2), Face(FaceType.ENGINEERING, 1),
                                     Face(FaceType.ARTILLERY), Face(FaceType.RECRUITMENT)],

        DiceType.RECRUITMENT_HEAVY: [Face(FaceType.RECRUITMENT, 3), Face(FaceType.RECRUITMENT, 2),
                                     Face(FaceType.RECRUITMENT, 2), Face(FaceType.RECRUITMENT, 1),
                                     Face(FaceType.ARTILLERY), Face(FaceType.ENGINEERING)]
    }

    dice = Dice(dice_faces[dice_type])
    return dice
