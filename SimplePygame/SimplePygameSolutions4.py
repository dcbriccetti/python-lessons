import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400), 0)
    pygame.display.set_caption('Simple Pygame Game')
    bee = pygame.image.load('bee1.png').convert_alpha()
    beeX = 0
    beeY = 0
    bird = pygame.image.load('bird.png').convert_alpha()
    birdX = 100
    birdY = 200

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT \
                or (event.type == KEYDOWN and event.key == K_ESCAPE):
                loop = False

        keystate = pygame.key.get_pressed()
        if keystate[K_RIGHT]:
            beeX += 5
        if keystate[K_LEFT]:
            beeX -= 5
        if keystate[K_UP]:
            beeY -= 5
        if keystate[K_DOWN]:
            beeY += 5

        if keystate[K_d]:
            birdX += 5
        if keystate[K_a]:
            birdX -= 5
        if keystate[K_w]:
            birdY -= 5
        if keystate[K_s]:
            birdY += 5

        screen.fill((0,180,0))
        screen.blit(bee, (beeX, beeY))
        screen.blit(bird, (birdX, birdY))
        pygame.display.flip()
            

if __name__ == '__main__': 
    main()
