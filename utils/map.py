import json
import pygame as pg
# from sprites.tile import Tile, TileObject

def load_map_from_file(grop, map_file_path: str):
    with open(map_file_path, 'r') as f:
        data = json.load(f)
        print(data)
        # tiles_set = { symbol: typs_str for data['tileSet']['symbol'], data['tileSet']['type'] in data }
        grid = []
        for poz_y, poz_line in enumerate(data['positions']):
        	row = []
        	for pos_x, tile_type in enumerate(poz_line.splite(',')): 
		        row.update(Tile((pos_x, pos_y)).populate_tile(tiles_set[TileObject(tile_type)]))
	        
	        grid.update(row)


def init_tiles_groups():
    all_sprites = pg.sprite.RenderPlain()
    roads = pg.sprite.Group()
    towers = pg.sprite.Group()

    for i, grid_row in enumerate(INIT_GRID):
        for j, tile_object in enumerate(grid_row):
            x = GRID_START_POS[0] + TILE_WIDTH * j
            y = GRID_START_POS[1] + TILE_WIDTH * i
            tile = Tile((x, y))

            all_sprites.add(tile)

            if tile_object is not None:
                populated_obj = tile.populate_tile(tile_object)
                all_sprites.add(populated_obj)

                if isinstance(populated_obj, Road):
                    roads.add(populated_obj)

                if isinstance(populated_obj, Tower):
                    towers.add(populated_obj)

        return all_sprites, roads, towers


