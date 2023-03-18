import json
import pygame as pg
from sprites.tile import Tile, TileObject
from utils.common import TILE_WIDTH
from sprites.tile import Tile, TileObject
from sprites.roads import Road
from sprites.tower import Tower


def load_map_from_file(map_file_path: str, tile_set='docs/tile_set.json'): #grop,
    with open(tile_set, 'r') as f:
        tiles_set = json.load(f)

    with open(map_file_path, 'r') as f:
        data = json.load(f)
        grid_start_pos = data['gridStartPos']
        grid = []
        for line in data['positions']:
            row = [TileObject(tiles_set[tile_type]) for tile_type in line]
            grid.append(row)

    return grid_start_pos, grid


def init_tiles_groups(level_file_path: str):
    all_sprites = pg.sprite.RenderPlain()
    roads = pg.sprite.Group()
    towers = pg.sprite.Group()
    GRID_START_POS, INIT_GRID = load_map_from_file(level_file_path)

    for i, grid_row in enumerate(INIT_GRID):
        for j, tile_object in enumerate(grid_row):
            x = GRID_START_POS[0] + TILE_WIDTH * j
            y = GRID_START_POS[1] + TILE_WIDTH * i
            tile = Tile((x, y))

            all_sprites.add(tile)

            if tile_object is not TileObject.EMPTY:
                populated_obj = tile.populate_tile(tile_object)
                all_sprites.add(populated_obj)

                if isinstance(populated_obj, Road):
                    roads.add(populated_obj)

                if isinstance(populated_obj, Tower):
                    towers.add(populated_obj)

    return all_sprites, roads, towers


