import pygame as pg

from gameplay.general_fire_management import towers_fire_management
from utils.common import TILE_WIDTH
from gameplay.movement import set_soldiers_manuverability
from sprites.tile import Tile, TileObject
from sprites.roads import Road
from sprites.tower import Tower
from sprites.soldier import Soldier
from utils import grid

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
FPS = 60


def init_tiles_groups():
    all_sprites = pg.sprite.RenderPlain()
    roads = pg.sprite.Group()
    towers = pg.sprite.Group()
    GRID_START_POS, INIT_GRID = grid.load_map_from_file('docs/test_level.json')

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


def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pg.Surface(screen.get_size())
    clock = pg.time.Clock()
    running = True

    all_sprites, roads, towers = init_tiles_groups()
    soldiers = pg.sprite.Group()


    # soldier_0 = Soldier((150, 240), 200, 2, 50) # temp
    # soldier_0.start_movement()
    # all_sprites.add(soldier_0)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(background, (0, 0))

        set_soldiers_manuverability(soldiers, roads)
        towers_fire_management(towers, soldiers)

        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
