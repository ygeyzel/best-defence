import pygame as pg
from sprites.tile import Tile, TILE_WIDTH


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60

GRID_START_POS = (150, 200)
INIT_GRID = (
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0) 
)


def init_tiles(groups):
    for i, grid_row in enumerate(INIT_GRID):
        for j, block_level in enumerate(grid_row):
            x = GRID_START_POS[0] + TILE_WIDTH * j
            y = GRID_START_POS[1] + TILE_WIDTH * i
            tile = Tile(block_level, (x, y))
            for group in groups:
                group.add(tile)


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pg.Surface(screen.get_size())
    clock = pg.time.Clock()
    running = True

    tiles = pg.sprite.Group()
    all_sprites = pg.sprite.RenderPlain()

    init_tiles((tiles, all_sprites))

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
