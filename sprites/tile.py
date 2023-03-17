from typing import Tuple
import pygame as pg
from enum import auto, Enum
from sprites.roads import road_factory, RoadState
from sprites.tower import tower_factory, TowerType
from utils.resources import load_image
from utils.common import TILE_WIDTH


class TileObject(Enum):
    REGULAR_ROAD = auto()
    HARD_ROAD = auto()
    ENGINEERED_ROAD = auto()
    TARGETING_TOWER = auto()


class Tile(pg.sprite.Sprite):

    def __init__(self, pos: Tuple[float, float]):
        pg.sprite.Sprite.__init__(self)

        self.tile_object = None
        self.image, self.rect = load_image(
            'tiles/empty.png', (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos

    def populate_tile(self, tile_object: TILE_WIDTH) -> pg.sprite.Sprite:
        assert self.tile_object is None

        objects_factory_dict = {
            TileObject.REGULAR_ROAD: (road_factory, RoadState.REGULAR),
            TileObject.HARD_ROAD: (road_factory, RoadState.HARD),
            TileObject.ENGINEERED_ROAD: (
                road_factory, RoadState.ENGINEERED),
            TileObject.TARGETING_TOWER: (
                tower_factory, TowerType.TARGETING)
        }

        pos = (self.rect.x, self.rect.y)
        new_sprite_type = objects_factory_dict[tile_object][0]
        new_sprite_params = objects_factory_dict[tile_object][1:]
        new_sprite = new_sprite_type(pos, *new_sprite_params)

        return new_sprite
