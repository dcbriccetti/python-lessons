import pygame
from pygame.locals import *

GRADIENT_HEIGHT = 100
MARGIN_HEIGHT = 2

def red(intensity):
    return (intensity, 0, 0)

def green(intensity):
    return (0, intensity, 0)

def blue(intensity):
    return (0, 0, intensity)

def gradient(surface, y, color_fn):
    for i in range(256):
        pygame.draw.line(surface, color_fn(i), (i, y), (i, y + GRADIENT_HEIGHT))

color_fns = red, green, blue
pygame.init()
num_margins = len(color_fns) - 1
screen = pygame.display.set_mode((256, GRADIENT_HEIGHT * len(color_fns) + 
    num_margins * MARGIN_HEIGHT), 0)
screen.fill((255, 255, 255))
pygame.display.set_caption('Gradients')
y = 0

for fn in color_fns:
    gradient(screen, y, fn)
    y += GRADIENT_HEIGHT + MARGIN_HEIGHT

pygame.display.flip()

loop = True
while loop:
    event = pygame.event.wait()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

pygame.quit()
