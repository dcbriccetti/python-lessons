import os
import pygame

def loadImage(file):
    file = os.path.join('media', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
    return surface.convert_alpha()

def loadImages(*files):
    return [loadImage(file) for file in files]
