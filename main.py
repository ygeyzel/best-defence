import pygame as pg
from utils.common import TILE_WIDTH
from sprites.tile import Tile, TileObject


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60

GRID_START_POS = (150, 200)
INIT_GRID = (
    (None, None, None, None, TileObject.TARGETING_TOWER, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None),
    (TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.ENGINEERED_ROAD,
     TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.HARD_ROAD, TileObject.HARD_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD, TileObject.HARD_ROAD, TileObject.REGULAR_ROAD, TileObject.REGULAR_ROAD)
)


def init_tiles(group):
    for i, grid_row in enumerate(INIT_GRID):
        for j, tile_object in enumerate(grid_row):
            x = GRID_START_POS[0] + TILE_WIDTH * j
            y = GRID_START_POS[1] + TILE_WIDTH * i
            tile = Tile((x, y))

            group.add(tile)

            if tile_object is not None:
                populated_obj = tile.populate_tile(tile_object)
                group.add(populated_obj)


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pg.Surface(screen.get_size())
    clock = pg.time.Clock()
    running = True

    all_sprites = pg.sprite.RenderPlain()

    init_tiles(all_sprites)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(background, (0, 0))

        all_sprites.update()
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
