from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import pygame as pg
from utils.resources import load_image
from utils.common import TILE_WIDTH


class RoadState(Enum):
    HARD = 0
    REGULAR = 1
    ENGINEERED = 2


def _load_road_image(image_name: str) -> pg.surface.Surface:
    image = load_image(f"roads/{image_name}.png", (TILE_WIDTH, TILE_WIDTH))[0]
    return image


class Road(pg.sprite.Sprite):

    @dataclass
    class RoadStats:
        image: pg.surface.Surface
        manuverability: float

    def __init__(self, pos: Tuple[float, float], init_state: RoadState):
        pg.sprite.Sprite.__init__(self)

        self.state_stats_dict = {
            RoadState.REGULAR: Road.RoadStats(_load_road_image("road"), 1),
            RoadState.HARD: Road.RoadStats(_load_road_image("road-blocked"), 0.75),
            RoadState.ENGINEERED: Road.RoadStats(
                _load_road_image("road-eng"), 1.5)
        }

        self.manuverability: float
        self._state: RoadState
        self.state = init_state

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    @property
    def state(self) -> RoadState:
        return self._state

    @state.setter
    def state(self, val: RoadState):
        self._state = val
        self.image = self.state_stats_dict[val].image
        self.manuverability = self.state_stats_dict[val].manuverability

    def upgrade(self):
        assert self.state.value < RoadState.ENGINEERED.value
        self.state = RoadState(self.state.value + 1)


def road_factory(pos: Tuple[float, float], init_state: RoadState) -> Road:
    road = Road(pos, init_state)
    return road
