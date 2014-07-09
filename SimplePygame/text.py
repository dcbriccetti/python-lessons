from time import sleep
import pygame
from pygame.locals import Color

pygame.init()
screen = pygame.display.set_mode((620, 115), 0)
font = pygame.font.Font(None, 150)
image = font.render('Hello, world', True, Color('green'))
clock = pygame.time.Clock()
screen.fill(Color('black'))
screen.blit(image, (8, 8))
pygame.display.flip()
sleep(3)
pygame.quit()
