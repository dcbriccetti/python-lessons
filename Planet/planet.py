import pygame
from pygame.constants import FULLSCREEN, KEYDOWN, K_ESCAPE, K_UP, K_DOWN, QUIT
from stars import draw_field

pg = pygame
pd = pg.display
pg.init()
pg.key.set_repeat(1, 20)
screen = pd.set_mode((0, 0), FULLSCREEN)
sr = screen.get_rect()
planet = pg.image.load('redplanet.png')
star_field = screen.copy()
draw_field(star_field)

clock = pygame.time.Clock()
run = True

planet_size = sr.width / 20
planet_size_increment = max(5, sr.width / 500)
image_changed = True

while True:
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                planet_size += planet_size_increment
                image_changed = True
            elif event.key == K_DOWN and planet_size - planet_size_increment >= 1:
                planet_size -= planet_size_increment
                image_changed = True
    if not run:
        break

    if image_changed:
        screen.blit(star_field, (0, 0))
        planet_scaled = pg.transform.scale(planet, (planet_size, planet_size))
        x = sr.centerx - planet_size / 2
        y = sr.centery - planet_size / 2
        screen.blit(planet_scaled, (x, y))
        pd.flip()
        image_changed = False

    clock.tick(100)

pg.quit()
