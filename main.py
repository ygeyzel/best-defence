import pygame as pg

from gameplay.main_soldier_interact import draw_soldiers_hp_bar
from gameplay.tower_management import towers_management
from gameplay.mouseactions import highlight_tile_under_mouse, handle_mouse_click
from gameplay.soldiers_management import soldiers_management
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

    sprite_groups = init_tiles_groups('levels/test_level.json')
    sprite_groups["soldiers"] = pg.sprite.Group()

    soldier_0 = Soldier((150, 240), 200, 2, 50) # temp
    sprite_groups["soldiers"].add(soldier_0)
    sprite_groups["all_sprites"].add(soldier_0)


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEMOTION:
                highlight_tile_under_mouse(sprite_groups["tiles"])
            if event.type == pg.MOUSEBUTTONDOWN:
                handle_mouse_click(sprite_groups["tiles"])

        screen.blit(background, (0, 0))

        towers_management(sprite_groups["towers"], sprite_groups["soldiers"])
        soldiers_management(sprite_groups["soldiers"], sprite_groups["roads"], sprite_groups["castle"])
        sprite_groups["all_sprites"].update()
        sprite_groups["soldiers"].clear(screen, background)



        sprite_groups["all_sprites"].draw(screen)

        highlight_tile_under_mouse(sprite_groups["tiles"])
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
