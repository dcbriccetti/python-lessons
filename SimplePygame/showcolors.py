import pygame
from pygame.constants import KEYDOWN, K_UP, K_DOWN, K_ESCAPE, QUIT

pygame.init()
pygame.key.set_repeat(100, 50)
screen = pygame.display.set_mode((200, 100))
clock = pygame.time.Clock()
framesPerSec = 10
run = True

for name, rgb in pygame.color.THECOLORS.iteritems():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN and framesPerSec > 1:
                framesPerSec -= 1
            elif event.key == K_UP:
                framesPerSec += 1

    if not run:
        break

    screen.fill(rgb)
    pygame.display.set_caption(name)
    pygame.display.flip()
    clock.tick(framesPerSec)

pygame.quit()
