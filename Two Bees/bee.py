import pygame
from util import loadImages

class Bee(pygame.sprite.Sprite):
    images = []

    @staticmethod
    def loadImages():
        Bee.images = loadImages('bee1.png', 'bee2.png', 'bee3.png')

    def __init__(self, screenRect):
        pygame.sprite.Sprite.__init__(self)
        self.imagesRotated = Bee.images
        self.image = self.images[0]
        imgRect = self.image.get_rect()
        self.rect = imgRect.move(screenRect.centerx - imgRect.centerx, 
            screenRect.centery - imgRect.centery)
        self.animIdx = 0
        
    def update(self):
        self.animIdx = (self.animIdx + 1) % len(self.images)
        self.image = self.imagesRotated[self.animIdx]

    def setAngle(self, angle):
        self.imagesRotated = []
        for image in Bee.images:
            self.imagesRotated.append(pygame.transform.rotate(image, angle))