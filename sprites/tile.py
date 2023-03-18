from enum import auto, Enum
from typing import Tuple, Optional
import pygame as pg
from sprites.roads import road_factory, RoadState, Road
from sprites.tower import tower_factory, TowerType, Tower
from sprites.barracks import barracks_factory, Barracks
from sprites.castle import castle_factory, Castle
from gameplay.game_stats import GameStats, TileAction
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

    def __init__(self, pos: Tuple[float, float], game_stats: GameStats):
        pg.sprite.Sprite.__init__(self)

        self.tile_object = None
        self.is_highlighted = False

        self.game_stats = game_stats
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

    def mouse_action(self) -> Optional[TileAction]:
        mouse_action_switch = {
            Road: TileAction.ENGINEERING,
            Tower: TileAction.ARTILLERY,
            Barracks: TileAction.RECRUIT
        }

        action = mouse_action_switch.get(type(self.tile_object))
        return action

    def is_mouse_action_active(self) -> bool:
        action = self.mouse_action()

        if action is None:
            return False

        return self.game_stats.is_action_avialable(action, self.tile_object)

    def preform_mouse_action(self):
        
        pass
        # if self.is_mouse_action_active():
        #     action = self.mouse_action()
        #     action, action_stats = action_switch[action]

        #     action_func(self.tile_object)
