import pygame
from pygame.constants import FULLSCREEN, KEYDOWN, K_ESCAPE, QUIT

pg = pygame
pd = pg.display
pg.init()
screen = pd.set_mode((0, 0), FULLSCREEN)
screen_width = screen.get_rect().width
planet = pg.image.load('redplanet.png')
clock = pygame.time.Clock()
run = True

for planet_size in range(0, screen_width, 2):
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
    if not run:
        break
    planet_scaled = pg.transform.scale(planet, (planet_size, planet_size))
    screen.fill((0, 0, 0))
    x = screen_width / 2 - planet_size / 2
    y = screen.get_rect().height / 2 - planet_size / 2
    screen.blit(planet_scaled, (x, y))
    pd.flip()
    clock.tick(40)

pg.time.wait(200)

pg.quit()
