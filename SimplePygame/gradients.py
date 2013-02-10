import pygame
from pygame.locals import *

gradient_height = 100
margin_height = 2

def red(intensity):
    return (intensity, 0, 0)

def green(intensity):
    return (0, intensity, 0)

def blue(intensity):
    return (0, 0, intensity)

def gradient(surface, y, color_fn):
    for i in range(256):
        pygame.draw.line(surface, color_fn(i), (i, y), (i, y + gradient_height))

color_fns = red, green, blue
pygame.init()
num_margins = len(color_fns) - 1
screen = pygame.display.set_mode((256, gradient_height * len(color_fns) + 
    num_margins * margin_height), 0)
screen.fill((255, 255, 255))
pygame.display.set_caption('Gradients')
y = 0

for fn in color_fns:
    gradient(screen, y, fn)
    y += gradient_height + margin_height

pygame.display.flip()

loop = True
while loop:
    event = pygame.event.wait()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

pygame.quit()
