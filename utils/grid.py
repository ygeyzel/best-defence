import json
import pygame as pg
from sprites.tile import Tile, TileObject

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
