from typing import Tuple
import pygame as pg
from enum import auto, Enum
from sprites.roads import road_factory, RoadState
from sprites.tower import tower_factory, TowerType
from sprites.barracks import barracks_factory
from sprites.castle import castle_factory
from utils.resources import load_image
from utils.common import TILE_WIDTH


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
        self.image, self.rect = load_image(
            'tiles/empty.png', (TILE_WIDTH, TILE_WIDTH))
        self.rect.x, self.rect.y = pos

    def populate_tile(self, tile_object: TILE_WIDTH) -> pg.sprite.Sprite:
        assert self.tile_object is None

        objects_factory_dict = {
            TileObject.REGULAR_ROAD: (road_factory, RoadState.REGULAR),
            TileObject.HARD_ROAD: (road_factory, RoadState.HARD),
            TileObject.ENGINEERED_ROAD: (road_factory, RoadState.ENGINEERED),
            TileObject.TARGETING_TOWER: (tower_factory, TowerType.TARGETING),
            TileObject.BARRACKS : (barracks_factory, None),
            TileObject.CASTLE : (castle_factory, None)
        }

        pos = (self.rect.x, self.rect.y)

        new_sprite_type = objects_factory_dict[tile_object][0]
        new_sprite_params = objects_factory_dict[tile_object][1:]
        new_sprite = new_sprite_type(pos, *new_sprite_params)

        return new_sprite
