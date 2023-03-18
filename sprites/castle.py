from typing import Tuple
from sprites.tower import TowerStats, Tower


class Castle(Tower):
    def __init__(self, pos: Tuple[int, int]):
        stats = TowerStats(max_hp=500, damage=40, attack_delay=10,
                           attack_range=1, tower_image="castle.png")
        super().__init__(pos, stats)


def castle_factory(pos: Tuple[float, float], _) -> Castle:
    castle = Castle(pos)
    return castle
