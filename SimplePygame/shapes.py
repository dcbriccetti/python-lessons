import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300), 0)
screen.fill(Color('black'))
pygame.draw.rect(screen, Color('red'), Rect(10, 10, 100, 100))
pygame.draw.circle(screen, Color('blue'), (200, 110), 50)
pygame.display.flip()

loop = True
while loop:
    event = pygame.event.wait()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

pygame.quit()
