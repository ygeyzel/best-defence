import pygame as pg


def highlight_tile_under_mouse(tiles_group: pg.sprite.Group):
    is_at_least_one_highlighted = False

    for tile in tiles_group: 
        if tile.is_collide_with_mouse() and not is_at_least_one_highlighted:
            tile.is_highlighted = True
            is_at_least_one_highlighted = False
        else:
            tile.is_highlighted = False
        
        tile.draw_frame()
