import os

CUR_DIR = os.path.split(os.path.abspath(__file__))[0]
BASE_DIR = os.path.dirname(CUR_DIR)
RES_DIR = os.path.join(BASE_DIR, "res")
IMAGES_DIR = os.path.join(RES_DIR, "images")
SOUNDS_DIR = os.path.join(RES_DIR, "sounds")

TILE_WIDTH = 25
