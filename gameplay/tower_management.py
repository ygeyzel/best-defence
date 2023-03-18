import pygame as pg


def towers_management(towers: pg.sprite.Group, soldiers: pg.sprite.Group):
    for tower in towers:
        tower.fire_management(soldiers)
        tower.draw_hp_bar()
