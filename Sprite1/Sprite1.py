import pygame
from pygame.locals import *
from bee import Bee

pygame.init()
screen = pygame.display.set_mode((600, 600), 0)
bgColor = 0, 120, 0
screen.fill(bgColor)
pygame.display.flip()
pygame.display.set_caption('Sprite Lesson 1')
Bee.loadImage()
bee = Bee(screen.get_rect())
drawingGroup = pygame.sprite.RenderUpdates()
drawingGroup.add(bee)

def clear_callback(surf, rect):
    surf.fill(bgColor, rect)
        
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    drawingGroup.clear(screen, clear_callback)
    drawingGroup.update()
    changedRects = drawingGroup.draw(screen)
    pygame.display.update(changedRects)

pygame.quit()