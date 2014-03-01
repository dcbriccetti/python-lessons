from time import sleep
import pygame
from pygame.locals import Color

pygame.init()
screen = pygame.display.set_mode((620, 115), 0)
pygame.display.set_caption('Text Drawing Example')
font = pygame.font.Font(None, 150)
image = font.render('Hello, world', True, Color('green'))
clock = pygame.time.Clock()
black = Color('black')
screen.fill(black)
screen.blit(image, (8, 8))
pygame.display.flip()
sleep(3)
pygame.quit()
