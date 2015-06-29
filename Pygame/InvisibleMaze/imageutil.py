import os
import pygame

def loadImage(file, alpha=True):
    file = os.path.join('media', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
    return surface.convert_alpha() if alpha else surface

def loadImages(*files):
    imgs = []
    for file in files:
        imgs.append(loadImage(file))
    return imgs

