from enum import auto, Enum
import pygame as pg
from sprites.castle import Castle
from sprites.dice import Face, FaceType
from sprites.roads import Road, RoadState
from sprites.tower import Tower


class TileAction(Enum):
    ARTILLERY = auto()
    ENGINEERING = auto()
    RECRUIT = auto()


class GameStats:
    def __init__(self, rolls: int = 20):
        self.rolls = rolls
        self.actions_inventory = {
            action: 1 for action in TileAction
        }

    def __repr__(self):
        return f'Dashboard(rolls:{self.rolls}, artillery:{self.artillery}, engineering:{self.engineering}, recruitment:{self.recruitment})'

    def is_action_avialable(self, action: TileAction, action_sprite: pg.sprite.Sprite):
        if not self.is_can_roll:
            return False

        if self.actions_inventory[action] <= 0:
            return False

        if action == TileAction.ENGINEERING:
            return action_sprite.state != RoadState.ENGINEERED
        if action == TileAction.ARTILLERY:
            return not isinstance(action_sprite, Castle)

        return True

    def is_can_roll(self):
        return self.rolls > 0

    def preform_action(self, action: TileAction, tile_sprite: pg.sprite.Sprite):

        pass

    def update_up_by_dice_face(self, face: Face):
        match face.face_type:
            case FaceType.ARTILLERY:
                self.artillery += face.power_num

            case FaceType.ENGINEERING:
                self.engineering += face.power_num

            case FaceType.RECRUITMENT:
                self.recruitment += face.power_num
