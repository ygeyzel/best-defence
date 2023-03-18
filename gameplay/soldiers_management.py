import pygame as pg
from sprites.soldier import SoldierState


def soldiers_management(soldiers: pg.sprite.Group, roads: pg.sprite.Group, castle: pg.sprite.GroupSingle):

    set_soldiers_manuverability(soldiers, roads)
    update_soldiers_state(soldiers, castle)

    for soldier in soldiers:
        soldier.draw_hp_bar()


def set_soldiers_manuverability(soldiers_group: pg.sprite.Group, roads_group: pg.sprite.Group):
    soldiers_roads = pg.sprite.groupcollide(
        soldiers_group, roads_group, False, False)

    for soldier, roads in soldiers_roads.items():
        if roads:
            soldier.manuverability_factor = roads[0].manuverability
        else:
            soldier.manuverability_factor = 1


def update_soldiers_state(soldiers: pg.sprite.Group, castel: pg.sprite.GroupSingle):

    soldiers_castle_collide = pg.sprite.groupcollide(
        soldiers, castel, False, False)
    for soldier, castels in soldiers_castle_collide.items():
        if castels:
            soldier.state = SoldierState.ATTACK
