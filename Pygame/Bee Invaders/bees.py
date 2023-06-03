from time import time
from random import randint
import pygame
from pygame.locals import *
from bee import Bee
from projectile import Projectile
from monster import Monster

pygame.init()
screen = pygame.display.set_mode((700, 700), 0)
screen_rect = screen.get_rect()
background = screen.copy()
for y in range(screen_rect.height):
    color_val = 255 - 255 * y / screen_rect.height
    pygame.draw.line(background, (0, color_val, 0), (0, y), (screen_rect.width, y))
Bee.loadImages()

screen.blit(background, (0, 0))
pygame.display.flip()

invaders = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
monsters = pygame.sprite.Group()

drawing_group = pygame.sprite.OrderedUpdates()
player_bee = Bee(10, screen.get_height() - 200)

for x in range(10, screen.get_width(), 100):
    for y in range(10, screen.get_height() - 300, 100):
        auto_bee = Bee(x, y)
        auto_bee.setAngle(180)
        invaders.add(auto_bee)
        drawing_group.add(auto_bee)

drawing_group.add(player_bee)

pygame.display.set_caption('Bee Invaders')
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
angles = (( 45,   0,  -45),
          ( 90,   0,  -90),
          (135, 180, -135))

loop = True
time_last_fire = 0

while loop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    if randint(1, 800) == 1:
        monster = Monster(screen_rect, drawing_group)
        drawing_group.add(monster)
        monsters.add(monster)

    keystate = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    shift = mods & KMOD_SHIFT

    if keystate[K_SPACE]:
        time_now = time()
        time_since_fire = time_now - time_last_fire
        if time_since_fire > (.2 if shift else .5):
            time_last_fire = time()
            projectile = Projectile(player_bee.rect.x + player_bee.rect.width / 2, player_bee.rect.y)
            drawing_group.add(projectile)
            projectiles.add(projectile)

    xdir = keystate[K_RIGHT] - keystate[K_LEFT]   # -1, 0, or 1
    ydir = keystate[K_DOWN]  - keystate[K_UP]

    player_bee.setAngle(angles[ydir+1][xdir+1])
    player_bee.rect = player_bee.rect.move((xdir * 8, ydir * 8)).clamp(screen_rect)

    pygame.sprite.groupcollide(projectiles, invaders, True, True)
    pygame.sprite.groupcollide(projectiles, monsters, True, True)

    drawing_group.clear(screen, background)
    drawing_group.update()
    changed_rects = drawing_group.draw(screen)
    pygame.display.update(changed_rects)

    clock.tick(60)

pygame.quit()
