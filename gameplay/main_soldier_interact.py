import pygame as pg
from sprites.soldier import SoldierState


def set_soldiers_manuverability(soldiers_group: pg.sprite.Group, roads_group: pg.sprite.Group):
    soldiers_roads = pg.sprite.groupcollide(soldiers_group, roads_group, False, False)

    for soldier, roads in soldiers_roads.items():
        if roads:
            soldier.manuverability_factor = roads[0].manuverability
        else:
            soldier.manuverability_factor = 1


def draw_soldiers_hp_bar(soldiers: pg.sprite.Group):
    for soldier in soldiers:
        soldier.draw_hp_bar()


def update_soldiers_state(soldiers: pg.sprite.Group, castels: pg.sprite.Group):
    
    soldiers_castles_collide = pg.sprite.groupcollide(soldiers, castels, False, False)
    for soldier, castels in soldiers_castles_collide.items():
        if castels:
            soldier.state = SoldierState.ATTACK
