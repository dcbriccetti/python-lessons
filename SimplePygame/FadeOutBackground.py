import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 400), 0)
pygame.display.set_caption('Move Bee Right and Notice the Fadeout')
bee = pygame.image.load('bee1.png').convert_alpha()
beeX = 0
beeY = 0
bgsound = pygame.mixer.Sound('groovy.wav')
bgsound.play(loops=10)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    keystate = pygame.key.get_pressed()
    if keystate[K_RIGHT]:
        bgsound.fadeout(5000)
        beeX += 5
    if keystate[K_LEFT]:
        beeX -= 5
    if keystate[K_UP]:
        beeY -= 5
    if keystate[K_DOWN]:
        beeY += 5

    screen.fill((0,180,0))
    screen.blit(bee, (beeX, beeY))
    pygame.display.flip()
            
pygame.quit()