import pygame
from pygame.constants import FULLSCREEN, KEYDOWN, K_ESCAPE, QUIT
from stars import draw_field

pg = pygame
pd = pg.display
pg.init()
screen = pd.set_mode((0, 0), FULLSCREEN)
sr = screen.get_rect()
planet = pg.image.load('redplanet.png')
star_field = screen.copy()
draw_field(star_field)

clock = pygame.time.Clock()
run = True

for planet_size in range(0, sr.width, 2):
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
    if not run:
        break
    planet_scaled = pg.transform.scale(planet, (planet_size, planet_size))
    x = sr.width / 2 - planet_size / 2
    y = sr.height / 2 - planet_size / 2
    screen.blit(star_field, (0, 0))
    screen.blit(planet_scaled, (x, y))
    pd.flip()
    clock.tick(40)

pg.time.wait(200)

pg.quit()
