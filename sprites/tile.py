from enum import auto, Enum
from typing import Tuple, Optional
import pygame as pg
from sprites.roads import road_factory, RoadState, Road
from sprites.tower import tower_factory, TowerType, Tower
from sprites.barracks import barracks_factory, Barracks
from sprites.castle import castle_factory
from utils.resources import load_image
from utils.common import TILE_WIDTH


class TileMouseAction(Enum):
    ATTACK = auto()
    ENGINEERING = auto()
    DRAFT = auto()


class TileObject(Enum):
    REGULAR_ROAD = "REGULAR_ROAD"
    HARD_ROAD = "HARD_ROAD"
    ENGINEERED_ROAD = "ENGINEERED_ROAD"
    TARGETING_TOWER = "TARGETING_TOWER"
    CASTLE = "CASTLE"
    EMPTY = "EMPTY"
    BARRACKS = "BARRACKS"


class Tile(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        self.tile_object = None
        self.is_highlighted = False
        self.image, self.rect = load_image(
            'tiles/empty.png', (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos

    def update(self):
        self.draw_frame()

    def populate_tile(self, tile_object: TILE_WIDTH) -> pg.sprite.Sprite:
        assert self.tile_object is None

        objects_factory_dict = {
            TileObject.REGULAR_ROAD: (road_factory, RoadState.REGULAR),
            TileObject.HARD_ROAD: (road_factory, RoadState.HARD),
            TileObject.ENGINEERED_ROAD: (road_factory, RoadState.ENGINEERED),
            TileObject.TARGETING_TOWER: (tower_factory, TowerType.TARGETING),
            TileObject.BARRACKS: (barracks_factory, None),
            TileObject.CASTLE: (castle_factory, None)
        }

        pos = (self.rect.x, self.rect.y)

        new_sprite_type = objects_factory_dict[tile_object][0]
        new_sprite_params = objects_factory_dict[tile_object][1:]
        new_sprite = new_sprite_type(pos, *new_sprite_params)

        self.tile_object = new_sprite
        return new_sprite

    def is_collide_with_mouse(self) -> bool:
        mouse = pg.mouse.get_pos()
        collide = self.rect.collidepoint(mouse)
        return collide

    def draw_frame(self):
        color = (0, 0, 0) if not self.is_highlighted else (
            0, 0, 255) if self.is_mouse_action_active() else (255, 0, 0)
        surface = self.tile_object.image if self.tile_object else self.image
        pg.draw.rect(surface, color, [0, 0, TILE_WIDTH, TILE_WIDTH], 1)

    def mouse_action(self) -> Optional[TileMouseAction]:
        mouse_action_switch = {
            Road: TileMouseAction.ENGINEERING,
            Tower: TileMouseAction.ATTACK,
            Barracks: TileMouseAction.DRAFT
        }

        action = mouse_action_switch.get(type(self.tile_object))
        return action

    def is_mouse_action_active(self) -> bool:
        action = self.mouse_action()

        ################  TEMP  ####################
        if action == TileMouseAction.ENGINEERING:
            return self.tile_object.state != RoadState.ENGINEERED

        return False
        ############################################

    def preform_mouse_action(self):
        action_func_switch = {
            TileMouseAction.ENGINEERING: Road.upgrade,
            TileMouseAction.ATTACK: Tower.artillery_hit
        }

        if self.is_mouse_action_active():
            action = self.mouse_action()
            action_func = action_func_switch[action]

            action_func(self.tile_object)
