import pygame
from pygame.locals import *

def draw_circle(surface, rect):
    pygame.draw.circle(surface, (255, 255, 255), rect.center, rect.width / 2)

def draw_square # you write this function

def draw_shapes(surface, draw_fns):
    rect = Rect(20, 20, 50, 50)
    # you write this line: loop over draw_fns
        # you write this line: call the function
        rect = rect.move(70, 0)

pygame.init()
screen = pygame.display.set_mode((500, 100), 0)
screen.fill((0, 60, 0))

#you write a call to draw_shapes, passing it what it needs

pygame.display.flip()

loop = True
while loop:
    event = pygame.event.wait()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        loop = False

pygame.quit()
