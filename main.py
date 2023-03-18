import pygame as pg

from gameplay.general_fire_management import towers_fire_management
from gameplay.movement import set_soldiers_manuverability
from gameplay.mouseactions import highlight_tile_under_mouse, handle_mouse_click
from sprites.soldier import Soldier
from utils.grid import init_tiles_groups

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
FPS = 60


def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pg.Surface(screen.get_size())
    clock = pg.time.Clock()
    running = True

    all_sprites, roads, towers, tiles = init_tiles_groups('docs/test_level.json')
    soldiers = pg.sprite.Group()

    soldier_0 = Soldier((150, 240), 200, 2, 50) # temp
    all_sprites.add(soldier_0)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                highlight_tile_under_mouse(tiles)
            if event.type == pg.MOUSEBUTTONDOWN:
                handle_mouse_click(tiles)

        screen.blit(background, (0, 0))

        set_soldiers_manuverability(soldiers, roads)
        towers_fire_management(towers, soldiers)

        all_sprites.update()
        all_sprites.draw(screen)
        highlight_tile_under_mouse(tiles)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
