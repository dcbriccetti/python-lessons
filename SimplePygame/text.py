import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200, 50), 0)
pygame.display.set_caption('Text Drawing Example')

font = pygame.font.Font(None, 20)
image = font.render('Hi there', 0, Color('green'))
clock = pygame.time.Clock()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    screen.fill((0, 0, 0))
    screen.blit(image, (4, 4))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
