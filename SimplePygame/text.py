import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, Color

pygame.init()
screen = pygame.display.set_mode((620, 115), 0)
pygame.display.set_caption('Text Drawing Example')

font = pygame.font.Font(None, 150)
image = font.render('Hello, world', True, Color('green'))
clock = pygame.time.Clock()
black = Color('black')

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    screen.fill(black)
    screen.blit(image, (8, 8))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
