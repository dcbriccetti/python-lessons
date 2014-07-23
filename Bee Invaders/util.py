import os
import pygame

def loadImage(file):
    file = os.path.join('media', file)
    surface = pygame.image.load(file)
    return surface.convert_alpha()

def loadImages(*files):
    return [loadImage(file) for file in files]
