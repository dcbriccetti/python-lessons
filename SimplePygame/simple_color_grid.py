import pygame
from random import randint
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((96, 96), 0)
bg_color = Color('black')
colors = ('red', 'green', 'blue')

screen.fill(bg_color)

for x in range(3):
    for y in range(3):
        pygame.draw.rect(screen, Color(colors[y]), Rect(x * 32 + 1, y * 32 + 1, 30, 30))

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        break

pygame.quit()
