import os, sys, pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,200))
    pygame.display.set_caption('Hello World')
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 200))
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT or \
                event.type == KEYDOWN and event.key == K_ESCAPE:
                keepGoing = false
        screen.blit(bg, (0, 0))
        pygame.display.flip()

    pygame.quit()

main()
