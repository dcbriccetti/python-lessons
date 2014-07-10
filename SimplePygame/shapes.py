import pygame
from time import sleep
from random import randint
from pygame.locals import *

def rc():
    return randint(0, 255)

pygame.init()
screen = pygame.display.set_mode((400, 400), 0)

loop = True
while loop:
    screen.fill(Color('black'))
    for x in range(0, 400, 50):
        for y in range(0, 400, 50):
            pygame.draw.rect(screen,
                Color(rc(), rc(), rc()), Rect(x + 5, y + 5, 40, 40))

    pygame.display.flip()
    sleep(.1)

    event = pygame.event.poll()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

pygame.quit()
