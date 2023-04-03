import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 400), 0)
pygame.display.set_caption('Collision Detection Demo')
bee = pygame.image.load('bee1.png')
beeRect = bee.get_rect()
beeRect.topleft = (0, 0)
bird = pygame.image.load('bird.png')
birdRect = bird.get_rect()
birdRect.topleft = (100, 200)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
                or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        beeRect = beeRect.move(5, 0)
    if keys[K_LEFT]:
        beeRect = beeRect.move(-5, 0)
    if keys[K_UP]:
        beeRect = beeRect.move(0, -5)
    if keys[K_DOWN]:
        beeRect = beeRect.move(0, 5)

    if keys[K_d]:
        birdRect = birdRect.move(5, 0)
    if keys[K_a]:
        birdRect = birdRect.move(-5, 0)
    if keys[K_w]:
        birdRect = birdRect.move(0, -5)
    if keys[K_s]:
        birdRect = birdRect.move(0, 5)
        
    if birdRect.colliderect(beeRect):
        print("Ouch!")

    screen.fill((0,180,0))
    screen.blit(bee, beeRect.topleft)
    screen.blit(bird, birdRect.topleft)
    pygame.display.flip()
            
pygame.quit()
