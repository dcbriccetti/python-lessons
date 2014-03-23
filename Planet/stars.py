import pygame
from random import gauss, randint

pg = pygame
pd = pg.display

def draw_field(star_field):
    sr = star_field.get_rect()
    star_field.fill((0, 0, 0))

    for n in range(int(gauss(500, 100))):
        gray = randint(1, 255)
        bluer = redder = greener = 0

        ri = randint(1, 10)
        if ri == 1:
            bluer = randint(0, 255 - gray)
        elif ri == 2:
            redder = randint(0, 255 - gray)
        elif ri == 3: # Make yellower (red + green)
            redder = greener = randint(0, 255 - gray)

        pg.draw.circle(star_field, (gray + redder, gray + greener, gray + bluer), \
                       (randint(0, sr.width), randint(0, sr.height)), max(0, int(gauss(1, 1))))
