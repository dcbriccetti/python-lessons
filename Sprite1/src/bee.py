import pygame, os
from pygame.locals import *

class Bee(pygame.sprite.Sprite):
    
    @staticmethod
    def loadImage():
        surface = pygame.image.load('bee1.png')
        Bee.image = surface.convert_alpha()
        
    def __init__(self, screenRect):
        pygame.sprite.Sprite.__init__(self)
        self.screenRect = screenRect
        self.image = Bee.image
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(screenRect.centerx - imgRect.centerx, 
            screenRect.centery - imgRect.centery)
        
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[K_RIGHT]:
            self.rect = self.rect.move((8, 0)).clamp(self.screenRect)
