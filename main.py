import pygame as pg


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pg.Surface(screen.get_size())
    clock = pg.time.Clock()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(background, (0, 0))

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
